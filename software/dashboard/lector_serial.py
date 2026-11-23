#!/usr/bin/env python3
"""Registra lecturas REALES del Leonardo por USB serial en CSV persistente.

Ejemplo desde la raiz del repositorio:
    python software/dashboard/lector_serial.py --puerto COM5
En Linux la ruta suele ser /dev/ttyACM0.
"""

import argparse
import csv
from datetime import datetime
from pathlib import Path
import re
import sys

PATRON = re.compile(
    r"Lectura cruda:\s*(\d+)\s*->\s*Humedad:\s*(\d+)%\s*\|\s*Estado:\s*(.+)$"
)
COLUMNAS = ["fecha_hora", "lectura_adc", "humedad_pct", "estado"]
ESTADOS = {"Seco", "Humedo", "Muy humedo"}
RUTA_DEFECTO = Path(__file__).resolve().parents[2] / "testing" / "datos" / "lecturas.csv"


def interpretar(linea):
    """Devuelve (adc, porcentaje, estado) o None si la linea es invalida."""
    coincidencia = PATRON.fullmatch(linea.strip())
    if not coincidencia:
        return None
    adc = int(coincidencia.group(1))
    porcentaje = int(coincidencia.group(2))
    estado = coincidencia.group(3).strip()
    if not (0 <= adc <= 1023 and 0 <= porcentaje <= 100):
        return None
    if estado not in ESTADOS:
        return None
    esperado = (
        "Seco" if porcentaje < 20 else
        "Humedo" if porcentaje < 40 else "Muy humedo"
    )
    if estado != esperado:
        return None
    return adc, porcentaje, estado


def registrar(puerto, salida, baudios=9600):
    try:
        import serial
    except ImportError as exc:
        raise SystemExit("Falta pyserial. Instala requirements.txt primero.") from exc

    salida = Path(salida).expanduser().resolve()
    salida.parent.mkdir(parents=True, exist_ok=True)
    archivo_nuevo = not salida.exists() or salida.stat().st_size == 0

    # Asegura persistencia: los datos quedan en disco aun si se cierra el panel.
    try:
        with serial.Serial(puerto, baudios, timeout=2) as enlace, salida.open(
            "a", newline="", encoding="utf-8"
        ) as archivo:
            escritor = csv.writer(archivo)
            if archivo_nuevo:
                escritor.writerow(COLUMNAS)
                archivo.flush()
            print(f"Conectado: {puerto} @ {baudios} baudios")
            print(f"Guardando lecturas reales en: {salida}")
            print("Ctrl+C para detener. Cierra antes el Monitor Serie de Arduino IDE.")
            while True:
                texto = enlace.readline().decode("utf-8", errors="replace").strip()
                if not texto:
                    continue
                muestra = interpretar(texto)
                if muestra is None:
                    print(f"Linea descartada: {texto}", file=sys.stderr)
                    continue
                fecha = datetime.now().astimezone().isoformat(timespec="seconds")
                escritor.writerow([fecha, *muestra])
                archivo.flush()
                print(f"{fecha} | ADC {muestra[0]} | {muestra[1]} % | {muestra[2]}")
    except KeyboardInterrupt:
        print("\nRegistro detenido; el CSV se conserva.")
    except Exception as exc:
        raise SystemExit(f"No fue posible leer el puerto o guardar el CSV: {exc}") from exc


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Registro serial del sensor de humedad")
    parser.add_argument("--puerto", required=True, help="Ej. COM5 o /dev/ttyACM0")
    parser.add_argument("--salida", default=str(RUTA_DEFECTO), help="Archivo CSV")
    parser.add_argument("--baudios", type=int, default=9600)
    argumentos = parser.parse_args()
    registrar(argumentos.puerto, argumentos.salida, argumentos.baudios)
