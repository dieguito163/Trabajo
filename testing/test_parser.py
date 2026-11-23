"""Pruebas automáticas de PARSEO. No sustituyen pruebas con sensor real."""
import importlib.util
from pathlib import Path
import unittest

ARCHIVO = Path(__file__).resolve().parents[1] / "software" / "dashboard" / "lector_serial.py"
spec = importlib.util.spec_from_file_location("lector_serial", ARCHIVO)
modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo)


class TestParser(unittest.TestCase):
    def test_intervalos(self):
        muestras = [
            ("Lectura cruda: 892  ->  Humedad: 0%  |  Estado: Seco", (892, 0, "Seco")),
            ("Lectura cruda: 827  ->  Humedad: 12%  |  Estado: Algo seco", (827, 12, "Algo seco")),
            ("Lectura cruda: 784  ->  Humedad: 20%  |  Estado: Humedo", (784, 20, "Humedo")),
            ("Lectura cruda: 675  ->  Humedad: 40%  |  Estado: Muy humedo", (675, 40, "Muy humedo")),
        ]
        for texto, esperado in muestras:
            with self.subTest(texto=texto):
                self.assertEqual(modulo.interpretar(texto), esperado)

    def test_rechaza_valores_incoherentes(self):
        lineas = [
            "Texto no reconocido",
            "Lectura cruda: 1024  ->  Humedad: 23%  |  Estado: Humedo",
            "Lectura cruda: 700  ->  Humedad: 101%  |  Estado: Muy humedo",
            "Lectura cruda: 700  ->  Humedad: 10%  |  Estado: Muy humedo",
        ]
        for linea in lineas:
            with self.subTest(linea=linea):
                self.assertIsNone(modulo.interpretar(linea))


if __name__ == "__main__":
    unittest.main()
