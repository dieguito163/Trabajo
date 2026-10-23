# Cableado asociado al código real

| Elemento | Pin Arduino UNO | Precauciones |
|---|---|---|
| Sensor de humedad: salida analógica | **A0** | Verificar tensión admitida por la sonda |
| Sensor: alimentación | VCC según módulo | Confirmar serigrafía/pinout |
| Sensor: tierra | GND | Masa común |
| Canal **rojo** del LED RGB | **D11 (PWM)** | Resistencia limitadora o módulo con resistencias |
| Canal **verde** del LED RGB | **D10 (PWM)** | Resistencia limitadora o módulo con resistencias |
| Canal **azul** del LED RGB | **D9 (PWM)** | Resistencia limitadora o módulo con resistencias |
| Común LED RGB | GND si cátodo común | Si ánodo común/activo bajo, adaptar cableado y firmware |

**Fuente:** código Arduino facilitado por el equipo. La fotografía permite identificar los dispositivos, pero no confirmar todos los contactos eléctricos; validar físicamente antes de encender. El diseño actual de caja lleva un **único orificio para un LED RGB**, no tres LEDs individuales. Medir el diámetro y módulo LED real antes de imprimir.
