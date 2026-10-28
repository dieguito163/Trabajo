Manual de instalación y uso

Instalación

1. Instalar Arduino IDE 2.x desde la página oficial de Arduino.
2. Descargar el repositorio y abrir software/src/detector_humedad.ino. Si el programa pide crear una carpeta llamada detector_humedad, aceptamos.
3. Si Arduino UNO no aparece entre las placas disponibles, instalar el paquete Arduino AVR Boards desde el gestor de placas.
4. Conectar el Arduino al computador con un cable USB de datos. Seleccionar la placa Arduino UNO y el puerto que corresponda.
5. Presionar Verificar y, si no aparece ningún error, presionar Subir.
6. Abrir el Monitor Serie y seleccionar 9600 baudios para ver las lecturas.

El código que tenemos usa tres salidas para controlar el LED. Como nuestro LED RGB tiene un solo cable de señal, todavía necesitamos identificar su modelo y ajustar el código antes de probar los colores.

Calibración

El código tiene dos valores de referencia: 895 para seco y 767 para húmedo. Hay que revisarlos con nuestro sensor y la tierra que vamos a usar.

1. Tomar al menos diez lecturas con la sonda en una condición seca. Anotar si la prueba se hizo al aire o en tierra seca, porque no son lo mismo.
2. Tomar al menos diez lecturas con la sonda en tierra húmeda. Mantener la parte electrónica y el conector fuera del agua.
3. Tratar de poner la sonda a la misma profundidad y esperar a que la lectura deje de cambiar. Anotar el tipo de tierra y las condiciones de la prueba.
4. Sacar el promedio de las lecturas secas y de las húmedas. Cambiar valorSeco y valorHumedo en el código por esos promedios. Los dos valores tienen que ser distintos para que el cálculo funcione.
5. Volver a subir el código y revisar que el número mostrado suba cuando la tierra esté más húmeda.
6. Revisar si los límites de 25 y 45 sirven para la planta que estamos usando. Si los cambiamos, anotar los nuevos valores.

El número que entrega el programa sirve para comparar la lectura con las referencias que elegimos. No es una medición exacta del porcentaje de agua en la tierra.

Uso

Con el sistema apagado, revisar las conexiones y poner la sonda en la tierra sin enterrar la parte electrónica. Después de ajustar el código al LED y conectarlo correctamente, encender el sistema y observar el color:

- Rojo: nivel bajo; revisar si la tierra necesita agua.
- Amarillo: nivel intermedio; observar cómo está la tierra.
- Verde: la lectura está sobre el límite de 45 definido en el código.

Antes de regar, considerar el tipo de planta y revisar la tierra. El detector no dice cuánta agua agregar ni distingue por sí solo si hay demasiada. Mantener el Arduino y el LED lejos del agua.

Para apagarlo, desconectar la alimentación. Después podemos sacar la sonda y limpiar la parte que estuvo en la tierra, sin mojar el conector.

Funciones del programa

| Función | Qué hace |
| setup() | Inicia la comunicación con el computador y configura los pines del LED. |
| loop() | Lee el sensor, calcula el nivel y elige el color. |
| setColor(rojo, verde, azul) | En el código actual, controla los tres canales de color. Esta parte debe adaptarse al LED de un cable de señal. |

El diagrama de flujo muestra los pasos del programa actual.

Si algo no funciona

| Problema | Qué podemos revisar |
| No aparece el puerto | Revisar el cable USB, la conexión y el controlador de la placa. |
| No se carga el programa | Revisar que la placa y el puerto estén bien seleccionados. Cerrar otros programas que estén usando el puerto. |
| El Monitor Serie muestra símbolos raros | Revisar que esté configurado en 9600 baudios. |
| El LED no enciende o muestra otro color | Revisar el modelo del LED, sus conexiones y que el código esté adaptado a su cable de señal. |
| La lectura siempre muestra 0 o 100 | Revisar la conexión del sensor a A0, su alimentación y los valores de calibración. |
| El color cambia seguido | Revisar si la sonda está bien puesta y si la lectura está cerca de un límite entre colores. |
| Las dos referencias de calibración son iguales | Repetir las mediciones y usar dos valores distintos. |

- Arduino UNO R3.
- Función map() de Arduino.
