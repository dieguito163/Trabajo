"""Dashboard local para mediciones REALES registradas en CSV por el Leonardo.

Ejecucion desde la raiz:
    python -m streamlit run software/dashboard/panel.py
No contiene datos falsos ni simulados. El grafico se actualiza cada 2 s.
"""

import os
from pathlib import Path

import pandas as pd
import streamlit as st

RUTA_DEFECTO = Path(__file__).resolve().parents[2] / "testing" / "datos" / "lecturas.csv"
RUTA = Path(os.getenv("HUMEDAD_CSV", str(RUTA_DEFECTO))).expanduser()
COLUMNAS = {"fecha_hora", "lectura_adc", "humedad_pct", "estado"}

st.set_page_config(page_title="Detector de humedad | TEI201", page_icon="🌱", layout="wide")
st.title("🌱 Detector de humedad del suelo")
st.caption("Arduino Leonardo · Sensor capacitivo A0 · Registro local mediante USB serial")
st.info(
    "Porcentaje = índice relativo entre calibraciones aire 892 y agua 350. "
    "No representa una medición certificada de contenido volumétrico de agua."
)


def consejo(estado):
    return {
        "Seco": "Revisar la tierra y evaluar el riego.",
        "Algo seco": "Observar la evolución; revisar necesidades de la planta.",
        "Humedo": "Humedad intermedia según los umbrales del equipo.",
        "Muy humedo": "Evitar regar automáticamente: confirmar con la planta y el sustrato.",
    }.get(estado, "Estado sin clasificar")


def leer_csv():
    if not RUTA.is_file():
        return pd.DataFrame()
    try:
        datos = pd.read_csv(RUTA, on_bad_lines="skip")
    except (OSError, pd.errors.EmptyDataError):
        return pd.DataFrame()
    if not COLUMNAS.issubset(datos.columns):
        st.error("El CSV no tiene las columnas esperadas; revisa lector_serial.py.")
        return pd.DataFrame()
    datos["fecha_hora"] = pd.to_datetime(datos["fecha_hora"], errors="coerce", utc=True)
    datos["humedad_pct"] = pd.to_numeric(datos["humedad_pct"], errors="coerce")
    datos["lectura_adc"] = pd.to_numeric(datos["lectura_adc"], errors="coerce")
    datos = datos.dropna(subset=["fecha_hora", "humedad_pct", "lectura_adc"])
    datos = datos[datos["humedad_pct"].between(0, 100)]
    return datos.sort_values("fecha_hora")


@st.fragment(run_every="2s")
def mostrar():
    datos = leer_csv()
    if datos.empty:
        st.warning(
            "Todavía no hay registros reales. Conecta el Leonardo, inicia "
            "lector_serial.py y mantén ese proceso abierto."
        )
        st.code(str(RUTA))
        return

    ultimo = datos.iloc[-1]
    a, b, c, d = st.columns(4)
    a.metric("Humedad relativa de calibración", f"{int(ultimo['humedad_pct'])} %")
    b.metric("Estado actual", str(ultimo["estado"]))
    c.metric("Promedio histórico", f"{datos['humedad_pct'].mean():.1f} %")
    d.metric("Muestras registradas", f"{len(datos):,}")

    st.markdown("**Decisión sugerida:** " + consejo(str(ultimo["estado"])))
    st.caption("Última muestra: " + str(ultimo["fecha_hora"]) + " · ADC: " + str(int(ultimo["lectura_adc"])))

    st.subheader("Evolución de la humedad")
    graficar = datos[["fecha_hora", "humedad_pct"]].set_index("fecha_hora")
    st.line_chart(graficar, y="humedad_pct", y_label="Índice de humedad (%)")

    st.subheader("Resumen del histórico")
    st.write(
        f"Mínimo: {datos['humedad_pct'].min():.0f} % · "
        f"Máximo: {datos['humedad_pct'].max():.0f} % · "
        f"Periodo registrado: {datos['fecha_hora'].min()} a {datos['fecha_hora'].max()}"
    )
    st.bar_chart(datos["estado"].value_counts().rename_axis("Estado").to_frame("Muestras"))
    with st.expander("Ver últimas 50 lecturas"):
        st.dataframe(datos.tail(50).iloc[::-1], use_container_width=True)


mostrar()
