# Registro de datos y dashboard

En nuestro proyecto utilizamos el puerto USB del Arduino Leonardo para enviar al computador los datos del sensor de humedad. Creamos un registrador serial que guarda cada lectura en un CSV y un dashboard en Streamlit que nos permite observar el estado actual y el histórico.

## Instalación en Windows

1. Conectamos el Leonardo por USB y cargamos el [firmware](../../firmware/detector_humedad/detector_humedad.ino).
2. Abrimos el Monitor Serie a **9600 baudios** para comprobar la salida y luego lo cerramos.
3. Instalamos Python 3.10 o superior y abrimos PowerShell en la carpeta del proyecto.
4. Instalamos las dependencias y buscamos el puerto:

~~~powershell
py -m pip install -r software/dashboard/requirements.txt
py -m serial.tools.list_ports
~~~

5. Iniciamos el registro en una terminal, reemplazando **COM5** por el puerto de nuestro Leonardo:

~~~powershell
py software/dashboard/lector_serial.py --puerto COM5
~~~

6. Abrimos otra terminal y ejecutamos:

~~~powershell
py -m streamlit run software/dashboard/panel.py
~~~

7. Entramos a la dirección local indicada por Streamlit, normalmente **http://localhost:8501**.

El puerto serial solo puede estar abierto en una aplicación a la vez. El registrador conserva las muestras en \`testing/datos/lecturas.csv\`, por lo que podemos volver a revisar registros anteriores incluso después de cerrar el programa.

## Datos guardados

| Columna | Qué registramos |
|---|---|
| fecha_hora | Fecha y hora de la lectura |
| lectura_adc | Valor analógico del sensor |
| humedad_pct | Índice calculado con la calibración 892/350 |
| estado | Seco / Humedo / Muy humedo |

En el dashboard mostramos índice actual, estado, promedio, cantidad de muestras, mínimo, máximo y dos gráficas. El panel se actualiza leyendo el CSV aproximadamente cada dos segundos.

## Interpretación

Nuestra referencia al aire es 892 y la referencia en agua es 350. El índice que calculamos es relativo y seguimos ajustando la calibración para representar mejor nuestro sustrato.

Los estados son **rojo de 0 a 19 %, verde de 20 a 39 % y azul desde 40 %**.

## Problemas que podemos revisar

| Situación | Solución |
|---|---|
| No aparece el puerto | Revisamos el cable USB, la placa Leonardo y la selección de puerto |
| Puerto ocupado | Cerramos el Monitor Serie antes de ejecutar Python |
| No aparecen datos | Comprobamos que el capturador esté recibiendo y guardando las lecturas |
| El LED muestra otro color | Revisamos las conexiones RGB y el tipo de módulo |
| El índice queda siempre en 0 o 100 | Revisamos A0, alimentación y calibración |

Nuestro dashboard funciona localmente en el computador conectado por USB. No usamos WiFi ni enviamos datos a la nube.
