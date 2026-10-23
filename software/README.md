# Código real del detector de humedad

**Archivo principal:** [`src/detector_humedad.ino`](src/detector_humedad.ino).

Este es el código compartido por el equipo para el prototipo que aparece en la fotografía, y reemplaza el ejemplo anterior.

## Pines usados

- Sensor capacitivo: señal analógica **A0**.
- LED RGB: rojo **D11**, verde **D10**, azul **D9** (salidas PWM).
- El circuito debe compartir **GND** con Arduino.

## Comportamiento

| Humedad calculada | Color | Interpretación del programa |
|---|---|---|
| 0–24 % | Rojo | Riego urgente |
| 25–44 % | Amarillo | Advertencia |
| 45–100 % | Verde | Humedad óptima |

La conversión utiliza `map(lecturaCruda, 895, 767, 0, 100)` y restringe el resultado a 0–100 %. Los valores **895** (seco) y **767** (húmedo) son referencias de calibración del código recibido, no mediciones que hayamos verificado. Los umbrales son criterios de este prototipo, no estándares para todas las plantas.

## Importante: tipo de LED RGB

El programa controla canales con `analogWrite` suponiendo que un PWM alto enciende ese color (circuito compatible con **cátodo común**, o un módulo que opere con esa lógica). Si tu módulo es **ánodo común** o activo en bajo, el resultado será diferente y hay que invertir las salidas o adaptar `setColor()`. Verifica conexiones y resistencias limitadoras del módulo real antes de conectarlo.

Para cargarlo: abre el `.ino` en Arduino IDE, selecciona placa UNO y puerto, súbelo y abre Monitor Serie a **9600 baudios**. Consulta [docs](docs/README.md) para calibrar.
