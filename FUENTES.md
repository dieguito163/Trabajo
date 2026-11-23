# Fuentes y herramientas del proyecto

En este archivo reunimos las librerías, la documentación consultada, los ejemplos de código y la asistencia de inteligencia artificial que utilizamos durante el desarrollo del detector de humedad del suelo.

## Librerías y herramientas

| Herramienta o librería | Versión | Para qué la usamos | Fuente |
|---|---|---|---|
| Arduino AVR Boards | Core de Arduino; versión instalada en nuestro IDE | Compilar el programa del Leonardo y utilizar Serial, analogRead, analogWrite, map y constrain | https://github.com/arduino/ArduinoCore-avr |
| Arduino IDE | Versión utilizada en nuestro computador | Programar y cargar el código en el Leonardo | https://www.arduino.cc/en/software |
| Python | 3.10 o superior | Registrar datos y procesar las mediciones del computador | https://www.python.org/ |
| pyserial | >=3.5,<4 | Recibir lecturas por USB serial | https://pyserial.readthedocs.io/ |
| pandas | >=2.1,<3 | Leer y analizar el histórico de mediciones | https://pandas.pydata.org/ |
| Streamlit | >=1.37,<2 | Mostrar el dashboard con gráficas e indicadores | https://docs.streamlit.io/ |
| OpenSCAD | Versión utilizada para generar el CAD | Modelar carcasa, tapa y volúmenes referenciales | https://openscad.org/ |
| CadQuery | >=2.5,<3 | Construir un ensamble STEP de sólidos importables en Fusion 360 | https://cadquery.readthedocs.io/ |
| GitHub Actions | Servicio de GitHub | Compilar el firmware y generar STL, renders, planos y STEP | https://docs.github.com/en/actions |

El código del Arduino Leonardo usa las funciones incluidas en el core AVR. No utilizamos librerías Arduino adicionales. En Python reunimos las dependencias del dashboard en [requirements.txt](software/dashboard/requirements.txt).

## Código y referencias utilizadas

**Programa del sensor.** Partimos de nuestro firmware con la lectura en A0, el LED RGB en D9, D10 y D11, y las referencias de calibración 892 al aire y 350 en agua. Ajustamos la salida para trabajar únicamente con **tres colores**, usando los intervalos 0–19 %, 20–39 % y 40–100 %.

**Documentación de Arduino.** Consultamos las funciones de entrada analógica, PWM y comunicación serial: https://docs.arduino.cc/language-reference/.

**Comunicación y dashboard.** Utilizamos la documentación de [pyserial](https://pyserial.readthedocs.io/en/latest/shortintro.html) para recibir las líneas seriales y la de [Streamlit](https://docs.streamlit.io/develop/api-reference) para representar el histórico.

**Ejemplo de estructura de repositorio.** Revisamos el proyecto público [sensor-calidad-suelo-TEI201](https://github.com/jgarcia-dec/sensor-calidad-suelo-TEI201) como referencia de organización, documentación y categorías de entregables. Nuestro montaje, código y decisiones de diseño son distintos.

**Diseño 3D.** Conservamos las versiones iniciales del CAD y sus STL en el historial del repositorio. Adaptamos el modelo a Leonardo y preparamos un ensamble STEP con volúmenes geométricos. Las dimensiones se verifican con el montaje físico cuando sea necesario.

**Precios de referencia.** Para nuestro presupuesto consultamos una [placa Leonardo compatible en AFEL](https://afel.cl/collections/placas-compatibles), un [sensor v1.2 en Pinout](https://pinout.cl/producto/sensor-capacitivo-de-humedad-de-suelo-v12?from=bestsellers) y precios de componentes básicos. Distinguimos estos valores de las estimaciones utilizadas para los ítems que no tienen cotización del componente exacto.

## Uso de inteligencia artificial

### Organización y documentación del proyecto — noviembre de 2026

- **Herramienta:** ChatGPT de OpenAI (GPT-6).
- **Uso:** pedimos ayuda para ordenar nuestro repositorio, adaptar la documentación a Arduino Leonardo y revisar los entregables del Avance 3.
- **Archivos elaborados o revisados con asistencia:** README, guías de hardware, esquema explicativo, BOM de referencia, informe, protocolo de pruebas, guías 3D y este archivo de fuentes.
- **Adaptación:** revisamos la información para que refleje nuestro montaje real: sin protoboard, con sensor externo, tapa atornillada y tres estados del LED RGB.

### Código Python del registro, dashboard y pruebas

- **Herramienta:** ChatGPT de OpenAI (GPT-6).
- **Uso:** solicitamos apoyo para desarrollar \`software/dashboard/lector_serial.py\`, \`software/dashboard/panel.py\`, \`testing/test_parser.py\` y \`testing/analizar_datos.py\`.
- **Adaptación:** utilizamos el formato serial de nuestro código Leonardo, agregamos guardado con fecha y hora, definimos los tres estados de humedad y separamos las pruebas automáticas de las mediciones físicas.
- **Comprensión:** podemos explicar cómo se lee A0, cómo se calcula el índice, cómo se selecciona el color y cómo se guarda el histórico en CSV. Las pruebas del software no sustituyen la calibración del sensor con tierra.

### Diseño CAD y automatización

- **Herramienta:** ChatGPT de OpenAI (GPT-6).
- **Uso:** apoyo para organizar modelos OpenSCAD, crear el script de CadQuery para STEP y preparar la exportación de renders y planos desde GitHub Actions.
- **Adaptación:** usamos dimensiones nominales de nuestro diseño y representamos componentes mediante volúmenes simples que podemos ajustar al importarlos en Fusion 360.

La asistencia de IA nos ayudó a desarrollar y documentar el proyecto. Seguimos siendo responsables de comprender el funcionamiento, revisar las conexiones y validar experimentalmente nuestras mediciones.
