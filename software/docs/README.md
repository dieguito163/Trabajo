# Calibración del sensor y estados del LED

En nuestro detector utilizamos el sensor capacitivo conectado al pin A0 del Arduino Leonardo. El código toma una lectura aproximadamente cada segundo y calcula un índice relativo de humedad a partir de dos referencias.

| Condición de referencia | Lectura analógica |
|---|---:|
| Sensor al aire | 892 |
| Sensor en agua | 350 |

El Arduino realiza el cálculo con \`map(lecturaCruda, 892, 350, 0, 100)\` y \`constrain(porcentaje, 0, 100)\`. El valor aumenta cuando la lectura cruda disminuye hacia la referencia húmeda.

## Colores

| Índice relativo | Estado | Color RGB |
|---|---|---|
| 0–19 % | Seco | 255, 0, 0 |
| 20–39 % | Húmedo | 0, 255, 0 |
| 40–100 % | Muy húmedo | 0, 0, 255 |

Para obtener estos colores utilizamos D9 (rojo), D10 (verde) y D11 (azul). El código asume que el módulo RGB es compatible con intensidad activa en alto.

## Ajuste de calibración

En nuestras pruebas iniciales el dispositivo funciona en general, pero necesitamos mejorar la calibración para el sustrato que utilizamos. Repetiremos lecturas estabilizadas al aire, en tierra seca y en tierra húmeda, manteniendo la misma profundidad y tomando varias muestras de cada condición.

Compararemos promedios y dispersión para evaluar si los puntos de referencia y los umbrales de 20 % y 40 % representan correctamente el estado de la tierra. Este índice es relativo y no corresponde automáticamente a una medición de humedad volumétrica.

[Protocolo de pruebas](../../testing/protocolo_leonardo.md).
