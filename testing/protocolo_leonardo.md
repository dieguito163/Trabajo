# Pruebas del detector de humedad

## Objetivo

Nuestro objetivo es comprobar que el sensor detecta cambios asociados a la humedad del suelo y que el Arduino Leonardo comunica el resultado mediante el LED RGB. También queremos comprobar que podemos registrar el valor en el computador y analizar su evolución.

## Funcionamiento observado

En nuestras primeras pruebas **el dispositivo funciona en general** y obtuvimos **81 % de clasificaciones correctas del estado de humedad**. Hemos podido utilizar el sensor y el indicador luminoso, pero la **calibración todavía necesita ajustes**. Por ahora utilizamos una referencia de 892 al aire y 350 en agua; estos valores nos permiten calcular un índice, aunque necesitamos relacionarlo mejor con condiciones de suelo seco y húmedo. Para repetir la evaluación del 81 % registraremos el total de pruebas, el número de clasificaciones correctas y el criterio usado para establecer el estado esperado. Calcularemos la tasa de aciertos con `correctas / total × 100`.

## Condiciones de prueba

Para comparar las lecturas trabajaremos con el mismo sensor, el mismo sustrato y una profundidad de inserción constante. Registraremos la fecha, el estado del suelo, las condiciones de la muestra y las observaciones durante la prueba. Evitaremos que el agua alcance el conector o la electrónica de la sonda.

## Procedimiento

1. Encendemos el Arduino Leonardo y verificamos que el sensor entregue una lectura analógica.
2. Dejamos el sensor en una condición estable y registramos las lecturas durante unos segundos.
3. Repetimos la prueba con el sensor al aire, en suelo seco y en suelo húmedo, sin cambiar la profundidad entre las muestras de suelo.
4. Comprobamos que el LED indique **rojo (0–19 %), verde (20–39 %) o azul (40–100 %)** según la lectura.
5. Conectamos el Arduino al computador por USB y guardamos las mediciones en CSV.
6. Abrimos el dashboard y observamos el valor actual, el promedio y la gráfica histórica.
7. Repetimos las mediciones para comprobar si los valores son consistentes o fluctúan cerca de los umbrales.

## Criterios de evaluación

| Prueba | Criterio |
|---|---|
| Lectura del sensor | Obtenemos mediciones ADC dentro de 0 a 1023 |
| Cambios de humedad | La lectura cambia de forma consistente cuando modificamos la humedad |
| Colores | Rojo para 0–19 %, verde para 20–39 %, azul desde 40 % |
| Registro | El CSV conserva fecha, valor crudo, índice y estado |
| Dashboard | Podemos observar el histórico, el promedio y los cambios en el tiempo |
| Estabilidad | Calculamos variación entre lecturas en una condición fija |
| Reparación | Podemos abrir la tapa sin romper la carcasa y acceder al circuito |

## Calibración

Necesitamos completar la calibración fina usando nuestro tipo de tierra. Para cada condición tomaremos **10 mediciones** una vez que la lectura se estabilice. Calcularemos el promedio y la desviación estándar de cada grupo. La comparación entre tierra seca y tierra húmeda permitirá comprobar si las referencias actuales son apropiadas.

El índice calculado con \`map(lectura, 892, 350, 0, 100)\` sirve para comparar condiciones, pero **no equivale directamente al porcentaje de agua contenido en el suelo**.

## Registro y análisis

Guardamos los registros en \`testing/datos/lecturas.csv\`. Podemos generar un resumen estadístico con:

~~~bash
python testing/analizar_datos.py --archivo testing/datos/lecturas.csv
~~~

El resumen incluye cantidad de registros, promedio, mínimo, máximo, dispersión, intervalo entre muestras y proporción de estados. Esos valores se calculan únicamente a partir de un CSV efectivamente registrado, no de datos ficticios.

## Dificultades y mejoras

Uno de nuestros cambios de diseño fue pasar de Arduino UNO a Leonardo y quitar la protoboard. Esto simplificó el montaje dentro de la caja, pero nos obligó a actualizar el código y revisar la distribución de pines.

La **calibración** es la principal mejora que tenemos identificada. Repetiremos mediciones bajo condiciones controladas y ajustaremos los parámetros según los resultados. Si observamos cambios de color demasiado frecuentes cerca de 20 % o 40 %, evaluaremos un filtro o histéresis para estabilizar la indicación.

## Relación con el problema

Buscamos reconocer cuándo conviene revisar el riego de una planta. El prototipo transforma una lectura en una señal rápida por colores y el dashboard nos permite observar una tendencia. Estas funciones nos ayudan a tomar una decisión informada, siempre considerando las necesidades de cada planta y las limitaciones de calibración de nuestro sensor.

[Resultados y análisis preliminar](reportes/resultados_preliminares.md) · [Registros](datos/)
