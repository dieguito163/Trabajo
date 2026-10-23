# Diseño 3D — caja para detector de humedad

**Carcasa preliminar** para Arduino UNO R3/clon de la fotografía, sensor capacitivo v1.2 y LED RGB (un solo módulo luminoso con tres canales).
El Arduino queda dentro; la sonda se coloca en la tierra y su cable atraviesa una ranura lateral. El LED RGB se asoma a través de la tapa; su control se realiza por tres pines PWM (D11, D10, D9).

## Archivos
- [CAD editable OpenSCAD](fusion360/caja_sensor_humedad.scad) — **no es un .f3d nativo de Fusion 360**.
- [Plano técnico SVG](planos/plano_caja.svg).
- **[Abrir y girar la base 3D](stl/base_arduino_uno.stl)** o **[abrir la tapa 3D](stl/tapa_led.stl)** directamente en GitHub.
- [Carpeta STL](stl/), archivos generados automáticamente por GitHub Actions y disponibles para descargar sin «Artifacts».
- [Vista ilustrativa](renders/).

## Medidas nominales (mm)
Caja: 104 × 82 × 41 (38 base + 3 tapa); pared 2,6; piso 3; postes de 6 para Arduino; paso LED Ø 6,2; cuatro tornillos M3 en tapa; agujeros guía UNO Ø 2,2 aproximados. Cotas provisionales y tolerancia inicial 0,25 mm.

## Cómo imprimir
1. En OpenSCAD abrir el archivo .scad, cambiar `pieza="vista"` por `"base"`, pulsar F6 y exportar STL. Repetir con `"tapa"` y `"calibracion"`.
2. También puedes abrir directamente los enlaces STL de esta página en GitHub, sin instalar programas. El proceso automático deja los STL en el repositorio y además adjunta una copia ZIP en Actions.
3. Importar STL a Cura, PrusaSlicer o Bambu Studio en milímetros. PLA interior / PETG ambiente húmedo, 0,2 mm capa, 3 perímetros, 15–25 % infill.
4. Imprimir **primero** la probeta de calibración: comprobar tornillos y LED.
5. Medir puertos y alturas; ajustar parámetros; imprimir carcasa y tapa.

**IMPORTANTE:** La foto no permite determinar medidas exactas. El módulo LED pequeño no tiene soporte interno específico; se debe medir antes de fijarlo. La caja no protege contra agua directa. No se ha verificado el ensamble físico. El modelo muestra el Arduino en modo ilustrativo `vista`; solo `base`/`tapa` son piezas imprimibles.
