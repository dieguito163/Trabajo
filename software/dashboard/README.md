# Dashboard y registro de datos del Arduino Leonardo

El **Leonardo no tiene WiFi integrado**. Se usa su conexión **USB serial a 9600 baudios** para enviar al computador las lecturas del sensor cada ~1 segundo. El registro las escribe en **testing/datos/lecturas.csv** y Streamlit las presenta en una página web **local** con histórico persistente.

## Instalación (Windows)

1. Conectar el Arduino Leonardo con un **cable USB de datos**, cargar firmware/detector_humedad/detector_humedad.ino y comprobar una lectura por Monitor Serie a 9600.
2. Cerrar el Monitor Serie antes de ejecutar Python, pues **solo un programa puede abrir el puerto a la vez**.
3. Instalar Python 3.10+ y abrir PowerShell en la raíz del repositorio.
4. Ejecutar:

~~~powershell
py -m pip install -r software/dashboard/requirements.txt
py -m serial.tools.list_ports
~~~

5. Buscar el puerto (por ejemplo COM5) y, **en la primera terminal**:

~~~powershell
py software/dashboard/lector_serial.py --puerto COM5
~~~

6. Sin cerrar el registrador, **en otra terminal**:

~~~powershell
py -m streamlit run software/dashboard/panel.py
~~~

7. Abrir la dirección local indicada por Streamlit, comúnmente http://localhost:8501.

En Linux reemplazar el puerto por /dev/ttyACM0, si corresponde. Para detener, Ctrl+C en el capturador. El CSV queda guardado en disco. No se crean mediciones de ejemplo.

## Datos almacenados

| Columna CSV | Significado |
|---|---|
| fecha_hora | Hora local del PC con zona horaria |
| lectura_adc | Valor crudo leído en A0 (0 a 1023) |
| humedad_pct | Índice relativo derivado de la calibración 892/350 |
| estado | Seco / Humedo / Muy humedo |

El lector descarta líneas incompletas, fuera de rango o incoherentes con el estado y escribe en disco después de cada muestra válida. El dashboard no requiere que el Arduino esté encendido para **consultar mediciones ya almacenadas**.

## Si falla

| Síntoma | Qué comprobar |
|---|---|
| Port busy / Permission denied | Cerrar Monitor Serie, Serial Plotter u otra instancia del capturador |
| No aparece COM | Cable USB de datos, selección de Leonardo, drivers, reiniciar conexión |
| No hay datos en dashboard | Confirmar que el capturador sigue activo, archivo CSV y puerto correcto |
| Gráfico no cambia | Observar nueva línea en capturador, verificar que el CSV está actualizándose |
| LED color incorrecto | Tipo de LED RGB y orden de canales; verificar resistencias y GND |
| 0%/100% permanentes | Pin A0, VCC, contacto de sonda y referencias de calibración |
| Python: module not found | Instalar software/dashboard/requirements.txt en el mismo Python |
| El Leonardo se reinicia al abrir puerto | Esperar unos segundos; el registrador ignora mensajes distintos de datos |

La aplicación es una opción **local**, no una web alojada públicamente. La disponibilidad depende de mantener el computador encendido. No se almacenan valores en la nube.
