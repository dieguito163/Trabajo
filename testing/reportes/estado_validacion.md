# Estado de las pruebas

Todavía no tenemos resultados cuantitativos del montaje Leonardo publicados en este repositorio. Ya agregamos el código del dashboard y el registrador, pero aún debemos comprobarlos con nuestro dispositivo.

- **Pruebas unitarias disponibles:** testing/test_parser.py valida que las cadenas del firmware se interpretan y se rechazan entradas inválidas. Los datos de esa prueba son **sintéticos**, no registros de suelo.
- **Pruebas físicas pendientes:** registro de muestras reales, LED de 3 colores, latencia, persistencia del archivo y acceso interno de caja.
- **Próximo paso de validación:** ejecutar el protocolo, guardar testing/datos/lecturas.csv y capturas del panel, calcular medias y desviaciones, reportar una falla observada y su solución.

No describir la carcasa como impermeable ni afirmar precisión/calibración volumétrica sin mediciones independientes.
