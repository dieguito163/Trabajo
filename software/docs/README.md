# Calibración y lógica del detector

## Configuración implementada

- **Placa:** Arduino Leonardo.
- **Sensor capacitivo:** lectura analógica en A0, escala del ADC 0 a 1023.
- **LED RGB:** rojo D9, verde D10, azul D11 (PWM), siempre que sea compatible con salidas activas en alto.
- **Calibración suministrada por el equipo:** aire = 892 y agua = 350.
- **Frecuencia nominal:** una lectura por segundo, mediante delay(1000) más tiempo de ejecución.
- **Salida serial:** 9600 baudios.

## ¿Qué significa 0–100 %?

La conversión **map(lecturaCruda, 892, 350, 0, 100)** corresponde a una **escala relativa** definida por los dos puntos elegidos. El 100 % es la referencia sumergida en agua, **no un contenido volumétrico real de 100 % en el sustrato**. Fuera de ese rango se limita el valor con **constrain**.

## Tabla de decisiones

| Intervalo | Nombre serial | Color PWM (R,G,B) |
|---|---|---|
| 0–11 | Seco | 255, 0, 0 |
| 12–19 | Algo seco | 255, 255, 0 |
| 20–39 | Humedo | 0, 255, 0 |
| 40–100 | Muy humedo | 0, 0, 255 |

Estos umbrales son de la versión entregada por el equipo; **no han sido validados para una especie o sustrato determinados**. Debe contrastarse visualmente la condición del suelo y documentar los resultados.

## Propuesta de validación física (no representa resultados ejecutados)

1. Identificar fecha, tipo de suelo, planta, profundidad de inserción y alimentación.
2. Tomar 10 lecturas estabilizadas con la sonda al aire, procurando no tocar los contactos.
3. Tomar 10 con sonda en agua **sin mojar la electrónica** y anotar dispersión.
4. Tomar 10 en tierra seca y 10 en tierra húmeda, a igual profundidad.
5. Comparar media, variación y tiempo de respuesta, registrando los cuatro colores observados.
6. Usar los resultados para decidir si se mantiene o cambia la calibración/umbrales.

Consultar [protocolo completo](../../testing/protocolo_leonardo.md). Al conectar el sistema, la **fuente de verdad** sobre las entradas del LED debe ser el esquema real (revisado con multímetro), no el color del cable por intuición.
