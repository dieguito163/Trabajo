# Detector de humedad del suelo — TEI201 | Avance 3

En este proyecto construimos un detector de humedad del suelo con **Arduino Leonardo**, un sensor capacitivo y un **LED RGB que muestra tres colores: rojo, verde y azul**. Usamos una carcasa impresa en 3D con tapa atornillada y dejamos el sensor fuera de la caja, conectado directamente. **No usamos protoboard** en esta versión.

Queremos saber cuándo conviene revisar el riego de una planta sin depender solamente de observar la tierra. Medimos el sensor una vez por segundo y transformamos la lectura en un índice de humedad y una señal de color. También preparamos un sistema para guardar el histórico en un computador y verlo mediante un dashboard.

> **Estado del proyecto:** ya subimos el firmware, la estructura del dashboard, el esquema funcional, la documentación y los modelos 3D referenciales. Todavía tenemos que realizar y documentar las pruebas con el prototipo físico, completar costos y adjuntar el ensamble final de Fusion 360.

## Cómo funciona

1. Conectamos el sensor capacitivo a la entrada analógica **A0** del Arduino Leonardo.
2. Convertimos la lectura usando los puntos de calibración que obtuvimos para el prototipo: **892 al aire** y **350 en agua**.
3. Mostramos el estado de la humedad mediante el LED RGB.
4. Cuando conectamos el Leonardo por USB a un computador, podemos registrar los datos en un **CSV** y visualizarlos en un dashboard local.

El porcentaje de humedad que calculamos es **relativo a esos dos valores de calibración**: no corresponde a un porcentaje volumétrico medido con instrumentos de laboratorio.

## Colores y criterios de riego

| Índice de humedad | Color del LED | Interpretación |
|---|---|---|
| **0–19 %** | 🔴 Rojo | Suelo seco: revisar si necesita riego |
| **20–39 %** | 🟢 Verde | Suelo húmedo: observar evolución |
| **40–100 %** | 🔵 Azul | Suelo muy húmedo: revisar antes de añadir más agua |

Estos intervalos son parte de nuestro prototipo. No sirven como recomendación universal para todas las plantas y tipos de tierra.

## Componentes y conexiones

| Elemento | Conexión |
|---|---|
| Sensor capacitivo | A0 del Leonardo + alimentación compatible + GND |
| LED RGB — rojo | Pin **D9** (PWM) |
| LED RGB — verde | Pin **D10** (PWM) |
| LED RGB — azul | Pin **D11** (PWM) |
| Computador | Puerto USB del Leonardo |

Las tres salidas PWM controlan **un LED RGB**, no tres luces diferentes. Antes de encender, debemos comprobar si el LED es de cátodo común o ánodo común y si incluye resistencias limitadoras. El esquema actual muestra conexiones funcionales, pero falta compararlo con el cableado interno de nuestro montaje.

- [Esquema funcional Leonardo](hardware/esquemas/esquema_leonardo.svg)
- [Lista de materiales](hardware/bom/BOM_leonardo.csv)
- [Fotografías y evidencias pendientes](hardware/fotos/README.md)

## Código e instalación

Nuestro código principal está en [firmware/detector_humedad/detector_humedad.ino](firmware/detector_humedad/detector_humedad.ino).

1. Instalamos [Arduino IDE](https://www.arduino.cc/en/software) y conectamos el Leonardo con un cable USB de datos.
2. Abrimos el archivo `detector_humedad.ino`.
3. Seleccionamos la placa **Arduino Leonardo** y el puerto correspondiente.
4. Verificamos y subimos el programa.
5. Para revisar las lecturas, abrimos el Monitor Serie a **9600 baudios**. Antes de iniciar el registrador de Python tenemos que **cerrar el Monitor Serie**.

## Guardado de datos y dashboard

Nuestro Leonardo no tiene conexión WiFi integrada. Para almacenar y visualizar datos conectamos el dispositivo por **USB** a un computador. Desarrollamos un lector serial en Python que escribe los datos en `testing/datos/lecturas.csv` y un panel local en Streamlit que muestra evolución temporal, estado actual y estadísticas.

Desde la carpeta principal del proyecto instalamos:

```bash
python -m pip install -r software/dashboard/requirements.txt
python -m serial.tools.list_ports
```

Con el puerto real identificado, en una terminal ejecutamos (el ejemplo usa COM5):

```bash
python software/dashboard/lector_serial.py --puerto COM5
```

Y en otra terminal abrimos el dashboard:

```bash
python -m streamlit run software/dashboard/panel.py
```

El dashboard funciona localmente en el computador. **No subimos datos ficticios como pruebas:** nos falta obtener una sesión real con el dispositivo y guardar capturas del gráfico.

[Manual del dashboard](software/dashboard/README.md) · [Protocolo de pruebas](testing/protocolo_leonardo.md)

## Diseño 3D

Diseñamos una carcasa con una tapa que se puede desmontar para acceder a los componentes. Tenemos modelos referenciales en OpenSCAD, STL y un plano PDF para la versión Leonardo. También conservamos archivos anteriores del diseño con Arduino UNO como parte del historial de desarrollo.

Antes de entregar necesitamos comparar las medidas reales del montaje con el CAD y añadir el **ensamble nativo de Fusion 360 (.f3d o .f3z)** que pide la pauta. No consideramos que los STL sean un reemplazo de ese archivo.

[Modelos, STL, planos y renders](diseno_3d/README.md)

## Pruebas y estado de entrega

Preparamos un protocolo para comprobar las lecturas, las transiciones entre los **tres colores**, el almacenamiento del CSV, el dashboard y la apertura de la tapa. Las pruebas de interpretación del puerto serial ya pasaron automáticamente en GitHub; eso **no sustituye** las mediciones reales del suelo ni la demostración del prototipo.

Nuestra lista de pendientes está en [docs/ESTADO_ENTREGA.md](docs/ESTADO_ENTREGA.md). El guion para explicar el proyecto está en [documentacion/presentacion/guion_avance3.md](documentacion/presentacion/guion_avance3.md).

## Equipo y fuentes

**Integrantes:** [agregar nombres y roles reales].

**Asignatura:** TEI201 — Taller de Diseño en Ingeniería, Universidad Adolfo Ibáñez.

Nuestra referencia de organización fue el [repositorio de ejemplo de TEI201](https://github.com/jgarcia-dec/sensor-calidad-suelo-TEI201). Documentamos las herramientas, bibliografía y asistencia utilizada en [FUENTES.md](FUENTES.md), como exige la pauta.
