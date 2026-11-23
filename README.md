# Detector de humedad del suelo

Proyecto TEI201 — Taller de Diseño en Ingeniería, Universidad Adolfo Ibáñez.

Construimos un detector de humedad del suelo para facilitar el cuidado de las plantas. Utilizamos un **Arduino Leonardo**, un **sensor capacitivo** y un **LED RGB** que indica tres niveles mediante los colores rojo, verde y azul. Armamos el circuito **sin protoboard** y lo incorporamos en una carcasa impresa en 3D, con tapa desmontable y el sensor hacia el exterior.

![Nuestro prototipo desde tres ángulos](hardware/fotos/vistas_del_montaje.jpg)

## Problema y solución

En el cuidado de una planta, regar únicamente por intuición puede provocar falta o exceso de agua. Con nuestro prototipo buscamos complementar esa observación con una lectura del sensor y una señal visual fácil de interpretar. El LED permite reconocer rápidamente cuándo conviene revisar la tierra, mientras que el registro histórico del computador permite observar cómo cambia la lectura con el tiempo.

## Funcionamiento

Conectamos el sensor a la entrada analógica **A0** del Arduino Leonardo. El programa lee la señal cada **1 segundo aproximadamente**, la transforma a un índice entre 0 y 100 y selecciona el color del LED RGB.

| Índice calculado | Color | Estado |
|---|---|---|
| 0–19 % | 🔴 Rojo | Seco |
| 20–39 % | 🟢 Verde | Húmedo |
| 40–100 % | 🔵 Azul | Muy húmedo |

En nuestro código usamos **892** como referencia al aire y **350** como referencia en agua. Seguimos ajustando la calibración para relacionar mejor los resultados con el sustrato real. El porcentaje mostrado es **relativo a estas referencias**, no una medición certificada de humedad volumétrica.

### Arquitectura

~~~text
Sensor capacitivo ── A0 ──> Arduino Leonardo ── D9/D10/D11 ──> LED RGB
                                  │
                            USB serial 9600
                                  │
                              Computador
                                  │
                         Registro CSV local
                                  │
                         Dashboard Streamlit
~~~

La versión final del montaje no utiliza protoboard. El Leonardo se comunica con el computador a través del cable USB, que permite registrar los datos sin agregar otro módulo de comunicación.

## Componentes

| Componente | Función |
|---|---|
| Arduino Leonardo | Lee la señal analógica, calcula el índice y controla el LED |
| Sensor capacitivo de humedad | Detecta cambios asociados a la humedad del suelo |
| LED RGB | Representa visualmente tres estados |
| Cableado y conectores | Une los componentes sin usar protoboard |
| Cable USB de datos | Alimenta y comunica el Leonardo con el computador |
| Carcasa impresa en 3D | Aloja la electrónica y permite abrir la tapa con tornillos |

La [lista de materiales y presupuesto](hardware/bom/README.md) reúne cantidades y valores de referencia. En [hardware](hardware/README.md) explicamos nuestra elección de componentes y sus conexiones.

## Código Arduino

El programa principal está en [firmware/detector_humedad/detector_humedad.ino](firmware/detector_humedad/detector_humedad.ino).

1. Instalamos [Arduino IDE](https://www.arduino.cc/en/software).
2. Conectamos el Arduino Leonardo mediante un cable USB de datos.
3. Abrimos el archivo **detector_humedad.ino**.
4. Seleccionamos **Arduino Leonardo** y el puerto correspondiente.
5. Verificamos, subimos el programa y abrimos el Monitor Serie a **9600 baudios**.

El firmware utiliza funciones del core de Arduino AVR, sin librerías externas adicionales.

## Registro histórico y dashboard

Para guardar las mediciones en el computador, utilizamos Python y un registrador que lee la salida serial. Los registros se agregan a un archivo CSV con fecha, lectura analógica, índice calculado y estado. Luego los visualizamos en un dashboard local con gráficas y estadísticas.

Instalamos las dependencias desde la raíz del proyecto:

~~~bash
python -m pip install -r software/dashboard/requirements.txt
python -m serial.tools.list_ports
~~~

Cerramos el Monitor Serie de Arduino IDE y comenzamos a registrar datos con el puerto correspondiente (por ejemplo, COM5):

~~~bash
python software/dashboard/lector_serial.py --puerto COM5
~~~

En otra terminal abrimos el panel:

~~~bash
python -m streamlit run software/dashboard/panel.py
~~~

El panel se abre en el navegador del computador (normalmente en **http://localhost:8501**). Incluye el valor actual, el estado, el promedio histórico, el mínimo y máximo, y gráficas que permiten ver tendencias.

[Instrucciones del dashboard](software/dashboard/README.md) · [Análisis de los registros](testing/README.md)

## Encapsulado y diseño 3D

La carcasa mantiene la placa en su interior, permite sacar el cable de la sonda y tiene una tapa con tornillos. Podemos abrirla para acceder a los componentes sin tener que romper la impresión.

Preparamos un [modelo 3D para Arduino Leonardo](diseno_3d/README.md) con sus piezas, volúmenes referenciales de los componentes, renders y planos. Incluimos modelos STL y un ensamble en formato STEP importable en Fusion 360. Las medidas del CAD son **nominales** y deben compararse con nuestro montaje; para disponer del formato nativo de Fusion 360 debemos abrir el ensamble allí y exportarlo como **.f3d o .f3z**.

## Pruebas y mejoras

En nuestras primeras pruebas, **el prototipo funciona en general**: responde a los cambios de lectura del sensor y utiliza el LED para representar el estado. La mejora principal es la **calibración**, ya que necesitamos contrastar los valores con distintos niveles de humedad del suelo y ajustar los límites para obtener indicaciones más consistentes.

Dejamos documentados el [protocolo](testing/protocolo_leonardo.md), el [análisis de funcionamiento](testing/reportes/resultados_preliminares.md) y las herramientas para analizar los datos que registremos.

## Archivos del proyecto

| Carpeta | Contenido |
|---|---|
| [firmware](firmware/) | Programa del Arduino Leonardo |
| [software](software/) | Registro CSV, dashboard, manual de uso |
| [hardware](hardware/) | Conexiones, esquema, componentes, fotografías y presupuesto |
| [diseno_3d](diseno_3d/) | CAD, STEP, STL, renders y planos |
| [testing](testing/) | Protocolo, análisis y archivos de datos |
| [documentacion](documentacion/) | Informe del proyecto |
| [iteraciones](iteraciones/) | Cambios realizados durante el desarrollo |
| [FUENTES.md](FUENTES.md) | Librerías, referencias y uso de IA |

**Integrantes:** completar con los nombres y roles de nuestros integrantes.

La documentación del proceso y las herramientas utilizadas está en [FUENTES.md](FUENTES.md).
