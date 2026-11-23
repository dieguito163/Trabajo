# Guion sugerido de presentación (8–10 minutos)

**Todos los integrantes participan.** Las duraciones son sugeridas, ajustarlas al número real de personas. Mostrar resultados reales, nunca datos generados para ilustrar.

| Tramo | Qué mostrar | Mensaje clave |
|---|---|---|
| 0:00–1:00 | Problema y usuario | Evitar decisiones de riego únicamente por intuición |
| 1:00–2:00 | Foto del montaje y arquitectura | Sensor A0 → Leonardo → LED RGB y USB |
| 2:00–5:30 | Demo en vivo | Cambiar condición del sensor; mostrar el color, el CSV y el dashboard actualizándose |
| 5:30–6:30 | Construcción y reparación | Abrir la tapa atornillada con el sistema desconectado y explicar conexiones sin protoboard |
| 6:30–7:30 | Diseño 3D | Mostrar ensamble, volúmenes internos y planos actuales; señalar límites verificados |
| 7:30–9:00 | Validación real | Mostrar gráfico, número de muestras, promedio, dispersión, una falla y su mejora |
| 9:00–9:30 | GitHub y fuentes | README, firmware, protocolo, FUENTES.md |
| 9:30–10:00 | Cierre | Qué decisión facilita y qué no puede determinar el sensor |

## Preparación indispensable

- Placa correcta en Arduino IDE: **Leonardo**; código cargado y puerto anotado.
- Cerrar el **Monitor Serie** antes de abrir el capturador Python.
- Abrir terminal de captura y Streamlit; comprobar **nuevo punto en la curva** durante la demo.
- Comprobar tomas de corriente, cable USB de datos y que el equipo funcione en la sala sin WiFi.
- Ensayar tres veces la demostración completa y tener un segundo cable USB.
- Tener el enlace público: https://github.com/dieguito163/Trabajo .

## Preguntas técnicas probables

**¿Por qué Leonardo?** Tiene A0, PWM 9/10/11 y USB serial; no trae WiFi integrado y necesita el PC para dashboard.

**¿Qué representa el porcentaje?** Interpolación entre lectura 892 al aire y 350 en agua; es índice relativo, no humedad volumétrica validada.

**¿Cómo persisten las mediciones?** Python escribe un registro con fecha/hora por cada lectura a un archivo CSV, que se conserva al cerrar la aplicación.

**¿Por qué sin protoboard?** Montaje más compacto, pero exige aislamiento y fijación de cables; se verifica abriendo la tapa.

**¿Qué falla encontraron?** Responder únicamente con un problema que hayan observado de verdad, documentando el antes/después. La migración UNO→Leonardo es una iteración, no una falla cuantificada por sí sola.
