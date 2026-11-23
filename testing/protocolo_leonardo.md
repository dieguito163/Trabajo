# Protocolo de pruebas y validación | Arduino Leonardo

**Situación:** definimos este procedimiento y sus criterios antes de medir; **todavía no son resultados experimentales**. Los registros deben obtenerse con el prototipo físico, y las pruebas del parser son una verificación de software, no una medición del suelo.

## Pregunta a validar

¿El sensor y el indicador LED permiten distinguir condiciones de humedad del sustrato y registrar los datos reales de manera que una persona pueda evaluar el riego?

## Condiciones controladas

Registrar: fecha, tipo de suelo, cantidad de agua aplicada, profundidad de inserción, tiempo de espera para estabilizar, modelo del sensor, alimentación USB, versión del firmware y cualquier desconexión. Mantener la electrónica fuera de agua o tierra húmeda.

## Pruebas y criterios

| ID | Objetivo | Procedimiento | Criterio de éxito | Evidencia exigida |
|---|---|---|---|---|
| P1 | Lectura continua | Registrar 5 min con sensor fijo | ~300 mediciones a 1/s, sin desconexiones; cuantificar diferencia frente a ideal | CSV real y conteo |
| P2 | Respuesta a humedad | Medir 10 muestras en aire, 10 en sustrato seco y 10 en húmedo | Lecturas reproducibles y cambio consistente al humedecer; informar medias y desviación | Tabla y gráfico |
| P3 | Tres colores | Llevar la lectura a condiciones que crucen 20% y 40% sin mojar la electrónica | Rojo, verde y azul coinciden con el firmware | Fotos o registro de observación |
| P4 | Persistencia | Capturar 2 min; cerrar registrador; abrir CSV y dashboard | El histórico sigue consultable después de cerrar capturador | Captura CSV + dashboard |
| P5 | Actualización del panel | Con capturador y panel abiertos, variar condición del sensor | Se muestra nueva lectura e historial dentro de algunos segundos; medir latencia real | Video de demo y captura con reloj |
| P6 | Reparabilidad | Apagar, retirar los tornillos y abrir tapa | Acceso a Arduino y conexiones sin romper carcasa | Fotos del interior |
| P7 | Seguridad básica | Inspección desenergizada de cables y conexiones | Sin conductores sueltos, polaridades y resistencias correctas | Foto y lista de verificación |

El criterio de 300 muestras en P1 es un **objetivo nominal** (delay de 1 s + tiempo de proceso). No debe reportarse como cantidad observada sin contar el CSV.

## Pasos de captura y cálculo

1. Conectar el Leonardo, elegir puerto, subir el firmware y cerrar Monitor Serie.
2. Iniciar **python software/dashboard/lector_serial.py --puerto COM5** (ajustar COM).
3. Abrir Streamlit por separado y confirmar que el archivo CSV se actualiza.
4. Registrar los datos bajo condiciones repetibles y anotar observaciones en [planilla](datos/plantilla_validacion.csv).
5. Con Python o Excel calcular: N, media, desviación estándar, mínimo/máximo, tasa de captura N/tiempo y latencia respecto a cambios de condición observados.
6. Mostrar al evaluador el CSV y la gráfica **reales**. No utilizar las cadenas sintéticas del test de parser como mediciones.

## Falla y mejora a investigar

En nuestra primera versión usamos Arduino UNO y una calibración diferente (895/767); al migrar a Leonardo se requiere actualizar pines, código, documentación y CAD. Esto es una **iteración de diseño identificada**, no una falla de ensayo cuantificada.

Si los datos fluctúan mucho cerca de los umbrales, **posible** mejora: filtro de promedio móvil o histéresis, pero solo implementarla tras medir la variación y sus consecuencias sobre la latencia.

## Conexión con el problema original

La señal analógica aislada no explica al usuario qué hacer. Se transforma en un estado LED y en una serie temporal: la gráfica permite conocer si el sustrato está cambiando hacia un estado relativamente más seco o más húmedo, y recomendar la revisión del riego. **No sustituye** el criterio por especie de planta ni demuestra un ahorro de agua sin un experimento de comparación.

## Resultados

**A completar con datos reales:** [plantilla de validación](datos/plantilla_validacion.csv). Adjuntar CSV registrado por el sistema, fotos del interior, captura del dashboard y análisis de al menos un error real y su solución.
