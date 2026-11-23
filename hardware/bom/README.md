# Lista de materiales y presupuesto

Para nuestro detector utilizamos un Arduino Leonardo, una sonda capacitiva, un LED RGB y una carcasa impresa en 3D. Al eliminar la protoboard, disminuimos el espacio ocupado por las conexiones.

En [BOM_leonardo.csv](BOM_leonardo.csv) dejamos el detalle por componente, cantidad, especificación, valor unitario y subtotal. Los valores corresponden a un **presupuesto de referencia en pesos chilenos**, no necesariamente al precio que pagamos por nuestro montaje.

## Presupuesto de referencia

| Componente | Cantidad | Valor unitario de referencia | Subtotal |
|---|---:|---:|---:|
| Arduino Leonardo compatible | 1 | $12.000 | $12.000 |
| Sensor capacitivo de humedad v1.2 | 1 | $2.390 | $2.390 |
| LED RGB | 1 | $1.500 | $1.500 |
| Resistencias para LED (si son necesarias) | 3 | $69 | $207 |
| Cables y conectores | 1 conjunto | $1.500 | $1.500 |
| Cable USB de datos | 1 | $1.500 | $1.500 |
| Impresión 3D (material de base y tapa) | 1 conjunto | $2.500 | $2.500 |
| Tornillos y fijaciones | 1 conjunto | $800 | $800 |
| **Total referencial** | | | **$22.397 CLP** |

Tomamos como referencia el precio de una [placa Leonardo compatible de AFEL](https://afel.cl/collections/placas-compatibles) y el de un [sensor capacitivo v1.2 en Pinout](https://pinout.cl/producto/sensor-capacitivo-de-humedad-de-suelo-v12?from=bestsellers). Para los componentes sin cotización exacta del montaje utilizamos valores estimados. El cálculo de resistencias corresponde a repartir el precio de un pack de diez unidades; verificaremos si nuestro módulo RGB las incorpora.

El valor del material de impresión es una estimación y no incluye horas de trabajo, herramientas o costo de electricidad. Antes de utilizar el total como costo real debemos contrastarlo con los materiales y precios efectivamente utilizados.

La [planilla y el PDF de la versión anterior](historico/) forman parte de nuestro historial de desarrollo.
