# Cómo abrir las figuras 3D, sin buscar «Artifacts»

Cuando estén generados, GitHub permite **abrir directamente los STL**, girarlos y acercarlos desde el navegador:

- [**Ver la base 3D**](base_arduino_uno.stl)
- [**Ver la tapa 3D**](tapa_led.stl)
- [**Ver probeta de prueba**](probeta_ajuste.stl)

Haz clic en la pieza para verla. También puedes descargar el `.stl` mediante **Download raw file**, o abrirlo en [3DViewer.net](https://3dviewer.net/), Cura o Bambu Studio.

Los tres STL se generan automáticamente desde el archivo CAD `.scad` mediante GitHub Actions y se **guardan dentro de esta carpeta del repositorio**, sin depender de la sección temporal «Artifacts». Si no aparecen, abre [Actions](https://github.com/dieguito163/Trabajo/actions) y revisa la ejecución «Generar STL imprimibles».

**Advertencia:** estos archivos son un primer prototipo. Verificar encaje real, diámetro del LED RGB y distancias USB/cables antes de imprimir una versión final.
