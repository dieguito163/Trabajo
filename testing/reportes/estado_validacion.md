# Estado de las pruebas

No hay resultados cuantitativos del nuevo montaje Leonardo documentados en este repositorio al momento de preparar esta versión. El código del dashboard y el registrador se agregaron, pero **su ejecución en el prototipo físico no se ha certificado desde esta conversación**.

- **Pruebas unitarias disponibles:** testing/test_parser.py valida que las cadenas del firmware se interpretan y se rechazan entradas inválidas. Los datos usados en esa prueba son **sintéticos**, no registros de suelo.
- **Pruebas físicas pendientes:** registro de muestras reales, LED 4 colores, latencia, persistencia del archivo y acceso interno de caja.
- **Próximo paso de validación:** ejecutar el protocolo, guardar testing/datos/lecturas.csv y capturas del panel, calcular medias y desviaciones, reportar una falla observada y su solución.

No describir la carcasa como impermeable ni afirmar precisión/calibración volumétrica sin mediciones independientes.
