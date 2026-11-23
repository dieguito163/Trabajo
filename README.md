# 🌱 Detector de humedad del suelo | TEI201 — Avance 3

**Prototipo físico:** Arduino Leonardo, sensor capacitivo de humedad del suelo, indicador LED RGB de cuatro estados y carcasa impresa en 3D desmontable. **Sin protoboard:** el montaje final utiliza conexiones directas dentro de la caja. El sensor se introduce en el sustrato desde el exterior.

El sistema toma una lectura aproximadamente cada segundo, calcula un **índice relativo de humedad** con las referencias de calibración del equipo y permite decidir cuándo revisar el riego. Los datos pueden registrarse en un **CSV persistente en el computador** mediante el USB serial del Leonardo y visualizarse en un **dashboard local**. No usa WiFi ni envía datos de forma autónoma a la nube.

> **Estado verificable:** firmware y programa de registro/dashboard incorporados al repositorio; la ejecución con el hardware real y los resultados cuantitativos deben verificarse en la demo. Los modelos CAD existentes contienen archivos históricos para Arduino UNO; ver estado 3D antes de presentarlos como finales.

## Equipo

- **Integrantes:** completar con los nombres reales del equipo y sus roles antes de entregar.
- **Asignatura:** TEI201, Taller de Diseño en Ingeniería, UAI.
- **Referencia de evaluación:** Avance 3, 23 de noviembre de 2026.

## Problema y propuesta

El exceso o la falta de riego puede afectar el cuidado de plantas. Sin una medición del suelo, una persona debe decidir principalmente por observación. Este prototipo entrega una indicación comprensible mediante un LED y un registro temporal de mediciones que permite observar la tendencia. **No determina por sí solo la cantidad de agua necesaria ni tiene umbrales universales para todas las especies.**

## Arquitectura real del sistema

~~~text
Tierra → Sensor capacitivo (A0) → Arduino Leonardo
                                      ├─ PWM D9/D10/D11 → LED RGB
                                      └─ USB serial 9600 baudios
                                           ↓
                               Computador + lector_serial.py
                                           ↓
                                    CSV persistente
                                           ↓
                                    Dashboard Streamlit
                                 (gráfica + estado + promedio)
~~~

**Importante:** para el dashboard deben estar conectados por USB el Leonardo y el computador. El Monitor Serie de Arduino IDE debe cerrarse antes de abrir el capturador; no pueden usar simultáneamente el mismo puerto.

## Estados del LED

| Índice relativo | Estado | Color | Interpretación orientativa |
|---|---|---|---|
| 0 a 11 % | Seco | 🔴 Rojo | Revisar el sustrato y evaluar riego |
| 12 a 19 % | Algo seco | 🟡 Amarillo | Seguir observando |
| 20 a 39 % | Húmedo | 🟢 Verde | Estado intermedio según la calibración |
| 40 a 100 % | Muy húmedo | 🔵 Azul | Evitar añadir agua sin revisar la planta |

La función del firmware es **map(lecturaCruda, 892, 350, 0, 100)** y luego **constrain(..., 0, 100)**. El 0 % es la referencia al aire y 100 % la referencia en agua que facilitó el equipo. **Esto no mide humedad volumétrica real** y los umbrales son decisiones de diseño que deben validarse con el sustrato y la planta concretos.

## Hardware y conexiones

| Elemento | Conexión prevista |
|---|---|
| Sensor capacitivo, señal analógica | A0 del Leonardo |
| Sensor, alimentación y tierra | Alimentación compatible y GND (verificar serigrafía del módulo) |
| Canal rojo del LED RGB | D9 (PWM) |
| Canal verde del LED RGB | D10 (PWM) |
| Canal azul del LED RGB | D11 (PWM) |
| Común del LED / retorno | Según módulo: cátodo común a GND si activo en alto |
| Alimentación y datos | Cable USB de datos al computador |

**No hay protoboard en la versión final.** Verificar el tipo de LED (cátodo común/ánodo común), el orden real de sus terminales y si tiene resistencias integradas; un LED RGB discreto necesita resistencia limitadora en cada canal. El color correcto no puede confirmarse únicamente con las fotos de la caja cerrada. [Documentación de hardware](hardware/README.md) · [Esquema funcional](hardware/esquemas/esquema_leonardo.svg) · [BOM actualizada](hardware/bom/BOM_leonardo.csv).

## Cómo cargar el código en el Leonardo

1. Instalar [Arduino IDE](https://www.arduino.cc/en/software) y conectar el Leonardo con **USB de datos**.
2. Abrir [firmware/detector_humedad/detector_humedad.ino](firmware/detector_humedad/detector_humedad.ino) en Arduino IDE.
3. Seleccionar **Herramientas → Placa → Arduino AVR Boards → Arduino Leonardo** y el puerto correcto.
4. Pulsar **Verificar** y **Subir**.
5. Abrir brevemente **Monitor Serie a 9600 baudios** para comprobar que se reciben lecturas cada segundo. **Cerrarlo** antes de iniciar el registrador.

El firmware no requiere librerías externas adicionales al core de Arduino AVR.

## Cómo guardar los datos y abrir el dashboard

Requiere **Python 3.10 o posterior**. Desde la carpeta raíz de este repositorio:

~~~bash
python -m pip install -r software/dashboard/requirements.txt
python -m serial.tools.list_ports
~~~

Con el puerto identificado, en una primera terminal:

~~~bash
python software/dashboard/lector_serial.py --puerto COM5
~~~

Reemplazar **COM5** por el puerto real (en Linux puede ser **/dev/ttyACM0**). En una **segunda terminal**, sin cerrar la primera:

~~~bash
python -m streamlit run software/dashboard/panel.py
~~~

Streamlit abre un navegador local (habitualmente **http://localhost:8501**). El capturador registra la fecha/hora, lectura ADC, índice de humedad y estado en **testing/datos/lecturas.csv**. El dashboard lee ese CSV aproximadamente cada 2 segundos: muestra estado actual, promedio, historial, mínimo/máximo y gráfica. El archivo persiste después de apagar el Leonardo, aunque el PC debe permanecer conectado mientras se adquieren muestras.

**No se incluyen muestras inventadas:** si todavía no hay archivo CSV, el dashboard mostrará un aviso. Para entregar evidencia cuantitativa, deben ejecutar una prueba real, conservar el CSV resultante y subir capturas del dashboard. [Guía de instalación y problemas](software/dashboard/README.md).

## Carpeta del proyecto

~~~text
README.md
FUENTES.md                  ← declaración obligatoria de librerías, código e IA
firmware/detector_humedad/  ← versión actual: Leonardo
software/dashboard/         ← lector USB serial, dashboard y dependencias
hardware/                   ← materiales, conexiones y fotos
diseno_3d/                  ← CAD, STL, plano y notas de compatibilidad
testing/                    ← protocolos, plantilla, pruebas y resultados reales
documentacion/              ← informe y presentación del equipo
docs/                       ← checklist honesto de entrega
iteraciones/                ← registro de cambios de prototipo
~~~

## Diseño 3D, reparabilidad y evidencia

La carcasa fotografiada usa tornillos para retirar la tapa, de manera que puede abrirse sin romper la pieza; el sensor externo se conecta mediante cable. **La resistencia de conexiones, accesibilidad interna, tolerancias y dimensiones no pueden validarse únicamente con las imágenes exteriores.** Los STL previos del repositorio están asociados al diseño UNO; existe una versión CAD referencial para Leonardo, pero sigue pendiente comparar el gemelo 3D con medidas del montaje real y adjuntar un archivo Fusion 360 **.f3d o .f3z** completo.

[Ver documentos 3D](diseno_3d/README.md) · [Ver protocolo de pruebas](testing/protocolo_leonardo.md) · [Ver estado frente a pauta](docs/ESTADO_ENTREGA.md).

## Honestidad técnica y académica

- **Probado en software:** se proporcionan pruebas unitarias del parser de tramas, diferentes de una validación del hardware. Ejecutar con **python -m unittest discover -s testing -p "test_*.py"**.
- **No afirmamos pruebas que no se han ejecutado:** las mediciones, latencia real, comparación de suelo seco/húmedo y demo deben medirse con el equipo.
- **Fuentes e IA:** ver [FUENTES.md](FUENTES.md), **obligatorio en la evaluación**.
- Se tomó como referencia de organización el [ejemplo de TEI201](https://github.com/jgarcia-dec/sensor-calidad-suelo-TEI201), sin atribuir su hardware o sus resultados a este proyecto.
