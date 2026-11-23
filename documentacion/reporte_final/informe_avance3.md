# Detector de humedad del suelo — Informe del Avance 3

**TEI201 · Taller de Diseño en Ingeniería · Universidad Adolfo Ibáñez**

Desarrollamos el proyecto entre cinco integrantes, distribuyendo las tareas de diseño, construcción, electrónica, programación y pruebas.

| Integrante | Área de trabajo |
|---|---|
| Nicolas Bajwol | Diseño 3D |
| Vicente Romero | Ensamblaje |
| Samuel Gutierrez | Hardware |
| Diego Osorio | Software |
| Clemente Alfonos | Ensamblaje y pruebas |

## 1. Problema

En el cuidado de las plantas, uno de los problemas más comunes es no saber con claridad cuándo regar. La tierra puede verse seca en la superficie y conservar humedad en profundidad, o recibir demasiada agua cuando todavía no la necesita. Por eso decidimos desarrollar un dispositivo sencillo que nos ayude a interpretar el estado del suelo antes de tomar una decisión.

Nuestro objetivo es complementar la observación de la planta mediante una lectura electrónica y una indicación visual. No buscamos automatizar el riego ni calcular directamente cuántos litros agregar, sino entregar información que nos permita decidir si conviene revisar el suelo.

## 2. Propuesta de solución

Construimos un detector con un sensor capacitivo, una placa **Arduino Leonardo**, un **LED RGB** y una carcasa impresa en 3D. El sensor se inserta en la tierra, mientras que el resto de la electrónica permanece dentro de la caja. No utilizamos protoboard en el montaje final.

El LED indica tres niveles:

| Color | Humedad relativa del programa | Estado |
|---|---:|---|
| Rojo | 0–19 % | Seco |
| Verde | 20–39 % | Húmedo |
| Azul | 40–100 % | Muy húmedo |

La conexión USB permite enviar las lecturas al computador. Añadimos un programa en Python que puede guardar un histórico en CSV y un dashboard local para observar los valores y su evolución.

## 3. Diseño y selección de componentes

### Arduino Leonardo

Elegimos el Leonardo porque permite leer una entrada analógica, controlar el LED RGB mediante tres canales PWM y enviar lecturas a un computador por USB. Utilizamos **A0** para el sensor y **D9, D10 y D11** para los canales rojo, verde y azul. El microcontrolador ATmega32U4 cuenta con las funciones necesarias para nuestro programa sin incorporar otro procesador.

### Sensor capacitivo

Utilizamos un sensor de humedad de salida analógica. Elegimos el principio capacitivo porque nos permite detectar cambios en la humedad del suelo sin depender de dos electrodos metálicos directamente expuestos como ocurre en algunos sensores resistivos. La señal no equivale por sí sola a una medida volumétrica exacta: necesitamos calibrarla para nuestro suelo.

### Indicador LED RGB

Elegimos un LED RGB para comunicar el estado de manera rápida. Con un solo componente luminoso podemos representar tres estados, sin incorporar una pantalla y sin exigir que la persona interprete números en todo momento.

### Alimentación, cableado y encapsulado

Alimentamos el Leonardo por USB cuando está conectado al computador. Eliminamos la protoboard para reducir el volumen del montaje. Utilizamos una carcasa impresa en 3D con salida para la sonda, acceso al USB y tapa sujeta con tornillos. El diseño nos permite abrirla para acceder a la electrónica. No consideramos la carcasa impermeable; mantenemos los conectores y la placa alejados del agua.

El detalle de cantidades, especificaciones y presupuesto está en [hardware/bom](../../hardware/bom/README.md). Las [fotografías](../../hardware/fotos/README.md) muestran nuestro prototipo ensamblado.

## 4. Funcionamiento del programa

El programa se ejecuta de manera cíclica:

1. Leemos el valor analógico del sensor mediante A0.
2. Convertimos la lectura a una escala relativa entre 0 y 100.
3. Comparamos el resultado con los límites de los tres estados.
4. Encendemos el canal correspondiente del LED RGB.
5. Escribimos la lectura y el estado en el puerto serial.
6. Esperamos aproximadamente un segundo antes de repetir el proceso.

Utilizamos una frecuencia cercana a **1 Hz**, suficiente para seguir cambios que normalmente ocurren de forma gradual en un sustrato y que evita enviar demasiados datos innecesarios.

### Cálculo del índice de humedad

Tomamos **892** como lectura de referencia al aire y **350** como referencia en agua. Con estos valores, el programa realiza una interpolación lineal:

$
h_{\text{relativa}}=\operatorname{limitar}_{[0,100]}\left(\frac{892-\text{ADC}}{892-350}\times100\right)
$

En Arduino implementamos este cálculo mediante `map()` y `constrain()`. El valor mostrado es un **índice relativo**, no una medición certificada de humedad volumétrica en porcentaje.

En nuestra versión actual utilizamos un LED de **tres colores**: rojo hasta 19 %, verde entre 20 y 39 %, y azul a partir de 40 %.

## 5. Registro de datos y visualización

Además de la indicación luminosa, preparamos un sistema de registro utilizando el cable USB del Arduino Leonardo. Nuestro programa `lector_serial.py` recibe las lecturas y guarda cada registro con fecha y hora en un CSV local.

El dashboard desarrollado con Streamlit lee ese archivo y nos permite visualizar:

- El índice de humedad más reciente y su estado.
- El promedio de las mediciones registradas.
- El mínimo y máximo del histórico.
- La evolución del índice en una gráfica temporal.
- La cantidad de registros y la distribución de estados.

Así podemos pasar de una lectura puntual a una evolución histórica. Por ejemplo, una disminución gradual del índice permitiría identificar que el sustrato se está acercando al estado seco. El dashboard se ejecuta en el computador conectado; nuestro Leonardo no incorpora WiFi.

[Manual de ejecución](../../software/dashboard/README.md) · [Código fuente](../../software/dashboard/)

## 6. Diseño 3D y fabricación

Construimos una caja para mantener el circuito protegido y ordenado. Dejamos el sensor fuera de la carcasa para que pueda introducirse en la tierra, mientras la placa y el LED quedan dentro. Utilizamos una tapa desmontable con tornillos para acceder a las conexiones.

Nuestro CAD contiene la base, la tapa y volúmenes representativos del Leonardo y del indicador. También incluimos el sensor como componente exterior. Los archivos del diseño se encuentran en [diseno_3d](../../diseno_3d/README.md), junto con los STL, planos, renders y el ensamble STEP para importarlo en Fusion 360.

Las medidas del modelo son nominales, por lo que necesitamos contrastar el montaje físico con el CAD antes de considerar definitivo el modelo en Fusion 360. El archivo STEP se puede importar y guardar como documento de Fusion 360, pero no es un archivo nativo `.f3d` por sí mismo.

## 7. Pruebas de funcionamiento

Durante las primeras pruebas observamos que **el prototipo funciona en general**: el sensor permite obtener lecturas y el indicador responde mediante los colores programados. Al contar las veces que el detector clasificó correctamente el estado de humedad, obtuvimos un **81 % de aciertos**. Calculamos este resultado dividiendo las clasificaciones correctas por el total de pruebas y multiplicando por 100. El dato representa la **exactitud de la clasificación de estados**, no la precisión de una medición física de humedad. No disponemos en este informe del total de ensayos ni del registro individual que permita verificar nuevamente el porcentaje.

El aspecto que todavía debemos mejorar es la **calibración**. Aunque usamos referencias de 892 al aire y 350 en agua, necesitamos realizar ensayos sistemáticos con tierra seca y húmeda para verificar que esos valores sean representativos de nuestro sustrato. También debemos estudiar si los límites de 20 % y 40 % separan adecuadamente las condiciones que queremos mostrar.

El protocolo de pruebas se encuentra en [testing/protocolo_leonardo.md](../../testing/protocolo_leonardo.md). Preparamos una herramienta que calcula promedio, dispersión, frecuencia de muestreo y otros indicadores a partir de un archivo de datos reales; el informe cuantitativo dependerá de que registremos una sesión experimental.

### Dificultad y mejora

Durante el desarrollo cambiamos el microcontrolador anterior por un Arduino Leonardo y eliminamos la protoboard. Eso nos llevó a revisar las conexiones y actualizar el código. También modificamos los valores utilizados para convertir la lectura del sensor en un índice.

La principal dificultad que seguimos trabajando es evitar que la escala de humedad dependa de referencias poco representativas del suelo. Para mejorarla proponemos repetir mediciones con el mismo sustrato y profundidad, calcular promedios y ajustar la calibración y los umbrales en función de esos resultados. Una mejora posterior, si encontramos oscilaciones cerca de los límites, sería agregar un promedio móvil o histéresis.

## 8. Relación con el problema original

Nuestro problema inicial era la dificultad para determinar cuándo revisar el riego de una planta. La información que entrega el sistema responde a ese objetivo porque permite detectar cambios en la lectura del sensor y convertirlos en un estado comprensible. El color rojo indica que debemos revisar si la tierra necesita agua; el verde y el azul permiten reconocer estados de mayor humedad.

El histórico del dashboard complementa la señal luminosa, porque muestra la tendencia en el tiempo y no solo una medición aislada. La utilidad de esta información depende de calibrar correctamente el sensor y comprobar los umbrales en el tipo de suelo que usaremos.

## 9. Conclusiones

Logramos integrar el sensor, el Arduino Leonardo, el LED RGB y una carcasa impresa en 3D para construir un detector de humedad de uso sencillo. La indicación por colores nos permite interpretar la lectura sin depender directamente del computador, y el registro por USB nos da la posibilidad de revisar la evolución de los datos.

Nuestro principal siguiente paso técnico es **mejorar la calibración** y respaldar con mediciones repetidas los intervalos utilizados. Esto permitirá que la señal visual sea más consistente con el estado real del suelo y que las conclusiones del dashboard tengan mayor utilidad.

## 10. Fuentes

Las librerías, documentación técnica, referencias y el uso de herramientas de IA se encuentran detallados en [FUENTES.md](../../FUENTES.md).
