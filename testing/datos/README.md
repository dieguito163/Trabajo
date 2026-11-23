# Mediciones de humedad

Guardamos nuestras mediciones del Arduino Leonardo en `lecturas.csv`. Cada registro incluye la hora, la lectura analógica, el índice calculado y el estado del LED.

Podemos complementar estos registros con la [plantilla](plantilla_validacion.csv), donde anotamos el tipo de tierra, su estado y las observaciones durante la calibración.

Para analizar una sesión ejecutamos `python testing/analizar_datos.py --archivo testing/datos/lecturas.csv`. Los resultados dependen de las lecturas que registremos con el prototipo físico.
