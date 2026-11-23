# Resultados preliminares y mejoras

## Funcionamiento

En las primeras pruebas, **nuestro detector funciona en general**: recibimos la lectura del sensor y utilizamos el LED RGB para representar el nivel calculado de humedad. En nuestra evaluación inicial obtuvimos **81 % de clasificaciones correctas** al comparar el color mostrado por el dispositivo con el estado esperado. El montaje incorpora Arduino Leonardo, cableado directo sin protoboard y carcasa impresa en 3D.

Los estados de nuestro programa son:

| Índice | Indicación |
|---|---|
| 0–19 % | Rojo — seco |
| 20–39 % | Verde — húmedo |
| 40–100 % | Azul — muy húmedo |

## Calibración

La principal mejora pendiente es la **calibración del sensor**. Actualmente usamos dos referencias: **892 al aire y 350 en agua**. Esta interpolación nos da un índice útil para comparar lecturas, pero todavía necesitamos contrastar los valores con tierra seca, ligeramente húmeda y muy húmeda.

Por eso no interpretamos el número mostrado como una medida exacta de humedad volumétrica y no damos los umbrales por validados para cualquier planta.

## Cambios realizados

Durante el desarrollo reemplazamos el Arduino UNO por un Leonardo, retiramos la protoboard y actualizamos los pines del LED RGB. También revisamos los puntos de referencia de la lectura y simplificamos la indicación a **tres colores**.

Con estos cambios conseguimos un montaje más compacto y una señal visual sencilla. El siguiente ajuste es repetir la calibración y comprobar la estabilidad de las lecturas en distintas condiciones del sustrato.

## Datos cuantitativos

En nuestra evaluación inicial obtuvimos **81 % de aciertos en la identificación del estado de humedad**. El porcentaje corresponde a `clasificaciones correctas / total de pruebas × 100`, y no a una medición de humedad con un error instrumental de 19 %. Para reproducirlo necesitamos conservar el total de ensayos, el criterio usado para definir el estado esperado y los resultados de cada intento. Los valores **892 y 350 son referencias de nuestro código**, no promedios de una serie experimental documentada en este informe. El CSV del Leonardo nos permitirá respaldar las próximas mediciones con un registro y calcular promedios, dispersión e intervalos de actualización.

[Protocolo de pruebas](../protocolo_leonardo.md) · [Programa de análisis](../analizar_datos.py) · [Dashboard](../../software/dashboard/README.md)

## Conclusión

La función principal del detector está implementada y, en nuestra evaluación inicial, identificamos correctamente el estado de humedad en el 81 % de las pruebas. Seguimos ajustando la calibración para mejorar la correspondencia entre los colores y el estado real de la tierra, y documentaremos nuevas pruebas para verificar el resultado.
