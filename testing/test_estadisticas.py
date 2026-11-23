"""Probamos el cálculo de estadísticas con valores de control, no con datos físicos."""
import importlib.util
import unittest
from datetime import datetime, timedelta
from pathlib import Path

ARCHIVO = Path(__file__).resolve().parent / "analizar_datos.py"
spec=importlib.util.spec_from_file_location("analizar_datos",ARCHIVO)
modulo=importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo)


class PruebasAnalisis(unittest.TestCase):
    def test_resumen_y_frecuencia(self):
        inicio=datetime.fromisoformat("2026-11-22T10:00:00-03:00")
        filas=[
            (inicio,892,0,"Seco"),
            (inicio+timedelta(seconds=1),784,20,"Humedo"),
            (inicio+timedelta(seconds=2),675,40,"Muy humedo"),
        ]
        r=modulo.resumen(filas)
        self.assertEqual(r["muestras"],3)
        self.assertAlmostEqual(r["promedio"],20)
        self.assertEqual(r["minimo"],0)
        self.assertEqual(r["maximo"],40)
        self.assertAlmostEqual(r["intervalo_medio_s"],1)
        self.assertAlmostEqual(r["intervalo_medio_estimado_hz"],1)
        self.assertEqual(r["estados"]["Humedo"],1)

    def test_no_permite_muestras_vacias(self):
        with self.assertRaises(ValueError):
            modulo.resumen([])


if __name__ == "__main__":
    unittest.main()
