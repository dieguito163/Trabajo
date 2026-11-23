#!/usr/bin/env python3
"""Resumen estadístico de las mediciones reales guardadas por el Leonardo.

Uso: python testing/analizar_datos.py --archivo testing/datos/lecturas.csv
El programa NO crea datos de ejemplo ni reemplaza una medición física.
"""

import argparse
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path
from statistics import mean, median, stdev

ESTADOS = {"Seco", "Humedo", "Muy humedo"}
COLUMNAS = {"fecha_hora", "lectura_adc", "humedad_pct", "estado"}


def leer_lecturas(archivo):
    ruta = Path(archivo)
    if not ruta.is_file():
        raise FileNotFoundError(f"No encontramos el CSV de mediciones: {ruta}")
    with ruta.open(newline="", encoding="utf-8-sig") as f:
        lector = csv.DictReader(f)
        if not COLUMNAS.issubset(lector.fieldnames or ()):
            raise ValueError("El archivo debe tener fecha_hora, lectura_adc, humedad_pct y estado")
        filas = []
        for n, fila in enumerate(lector, start=2):
            try:
                fecha = datetime.fromisoformat(fila["fecha_hora"].replace("Z", "+00:00"))
                adc = int(fila["lectura_adc"])
                humedad = int(fila["humedad_pct"])
                estado = fila["estado"].strip()
            except (ValueError, TypeError, AttributeError):
                continue
            if not (0 <= adc <= 1023 and 0 <= humedad <= 100 and estado in ESTADOS):
                continue
            esperado = "Seco" if humedad < 20 else ("Humedo" if humedad < 40 else "Muy humedo")
            if estado != esperado:
                continue
            filas.append((fecha, adc, humedad, estado))
    return sorted(filas, key=lambda x: x[0])


def resumen(filas):
    if not filas:
        raise ValueError("No hay registros válidos para analizar")
    hum = [f[2] for f in filas]
    conteo = Counter(f[3] for f in filas)
    deltas = [(b[0]-a[0]).total_seconds() for a,b in zip(filas,filas[1:])]
    deltas = [d for d in deltas if d >= 0]
    return {
        "muestras": len(filas),
        "promedio": mean(hum),
        "mediana": median(hum),
        "minimo": min(hum),
        "maximo": max(hum),
        "desviacion": stdev(hum) if len(hum) > 1 else 0.0,
        "intervalo_medio_s": mean(deltas) if deltas else None,
        "intervalo_medio_estimado_hz": 1/mean(deltas) if deltas and mean(deltas)>0 else None,
        "inicio": filas[0][0].isoformat(),
        "fin": filas[-1][0].isoformat(),
        "estados": conteo,
    }


def texto_reporte(r, fuente):
    intervalo = "sin suficientes muestras" if r["intervalo_medio_s"] is None else f'{r["intervalo_medio_s"]:.2f} s'
    frecuencia = "sin suficientes muestras" if r["intervalo_medio_estimado_hz"] is None else f'{r["intervalo_medio_estimado_hz"]:.2f} Hz'
    return "\n".join([
        "# Análisis de mediciones del detector",
        "",
        f"Datos de origen: \`{fuente}\`.",
        f"Periodo: {r['inicio']} — {r['fin']}.",
        "",
        "| Indicador | Resultado |",
        "|---|---:|",
        f"| Cantidad de muestras | {r['muestras']} |",
        f"| Promedio del índice | {r['promedio']:.2f} % |",
        f"| Mediana | {r['mediana']:.2f} % |",
        f"| Desviación estándar | {r['desviacion']:.2f} puntos |",
        f"| Mínimo | {r['minimo']} % |",
        f"| Máximo | {r['maximo']} % |",
        f"| Intervalo promedio entre registros | {intervalo} |",
        f"| Frecuencia media registrada | {frecuencia} |",
        f"| Lecturas estado seco | {r['estados'].get('Seco', 0)} |",
        f"| Lecturas estado húmedo | {r['estados'].get('Humedo', 0)} |",
        f"| Lecturas estado muy húmedo | {r['estados'].get('Muy humedo', 0)} |",
        "",
        "Los valores de humedad son índices relativos a nuestra calibración (892/350),",
        "no porcentajes volumétricos medidos con un instrumento de referencia.",
        "La precisión y la latencia ante un cambio de suelo requieren un ensayo controlado adicional.",
        "",
    ]) + "\n"


def main():
    p = argparse.ArgumentParser(description="Analiza el CSV real de humedad")
    p.add_argument("--archivo", default="testing/datos/lecturas.csv")
    p.add_argument("--salida", default="testing/reportes/analisis_de_mediciones.md")
    args = p.parse_args()
    try:
        filas = leer_lecturas(args.archivo)
        resultado = resumen(filas)
    except (FileNotFoundError, ValueError) as exc:
        raise SystemExit(str(exc))
    destino = Path(args.salida)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(texto_reporte(resultado, args.archivo), encoding="utf-8")
    print(f"Analizamos {resultado['muestras']} mediciones reales. Resumen: {destino}")


if __name__ == "__main__":
    main()
