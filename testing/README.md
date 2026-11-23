# Pruebas y análisis

En nuestras pruebas iniciales, el prototipo funciona en general. El sensor entrega lecturas y el LED RGB muestra los tres colores previstos. La principal mejora es terminar de ajustar la calibración de humedad para nuestro sustrato.

- [Procedimiento de pruebas](protocolo_leonardo.md)
- [Resultados y mejoras](reportes/resultados_preliminares.md)
- [Análisis de datos](analizar_datos.py)
- [Plantilla para mediciones](datos/plantilla_validacion.csv)

Cuando registramos una sesión con el Leonardo guardamos los datos en `testing/datos/lecturas.csv`. Podemos generar un análisis real con `python testing/analizar_datos.py --archivo testing/datos/lecturas.csv` y consultar la evolución en el dashboard.
