# Conexiones previstas | Arduino Leonardo (sin protoboard)

| Función | Pin Leonardo | Señal en código | Observación |
|---|---|---|---|
| Salida sensor | A0 | sensorPin | Lectura ADC 10 bits |
| Sensor alimentación | 5 V / tensión admitida por el sensor | — | Verificar pinout VCC del modelo real |
| Sensor retorno | GND | — | Masa común |
| LED rojo | D9 PWM | pinRojo | Resistencia limitadora si no existe en el módulo |
| LED verde | D10 PWM | pinVerde | Resistencia limitadora si no existe en el módulo |
| LED azul | D11 PWM | pinAzul | Resistencia limitadora si no existe en el módulo |
| Común LED | GND, **solo si cátodo común** | — | Si ánodo común, ajustar firmware y alimentación |
| Computador | USB de datos | Serial 9600 | Transmite lecturas para CSV + dashboard |

No se utiliza protoboard. Se recomienda asegurar conexiones con conectores o soldadura electrónica aislada y alivio de tensión en la salida de cable del sensor.

**Comprobaciones obligatorias antes de energizar:**
1. Confirmar el tipo de LED RGB y sus terminales; el código supone salida activa en alto.
2. Confirmar si el módulo LED posee resistencias en los canales.
3. Identificar pines del sensor por su **serigrafía real**, no solo por colores del cable.
4. Verificar ausencia de cortocircuitos, polaridad, tensión y fijación de los conductores.
5. Confirmar que la apertura de USB y cableado no dañen piezas al cerrar.

El [esquema SVG](esquema_leonardo.svg) representa la **arquitectura del firmware**; no debe interpretarse como esquemático de fabricación validado sin revisar las conexiones interiores.
