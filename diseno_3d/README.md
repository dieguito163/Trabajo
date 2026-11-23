# Diseño 3D de nuestro detector

Modelamos una carcasa para alojar el Arduino Leonardo y el indicador LED, dejando la sonda capacitiva fuera de la caja. Diseñamos una tapa desmontable, aperturas para las conexiones y espacio para acceder a los componentes.

## Modelos

- [Diseño paramétrico en OpenSCAD](fusion360/caja_sensor_leonardo.scad).
- [Ensamble STEP para Fusion 360](fusion360/ensamble_leonardo.step).
- [Script para reconstruir el STEP](fusion360/generar_ensamble_step.py).
- [Base, tapa y pieza de comprobación en STL](stl/README.md).
- [Planos con vistas y dimensiones](planos/README.md).
- [Renders de exterior, interior y vista explosionada](renders/README.md).

## Medidas nominales del modelo

| Parámetro | Dimensión |
|---|---:|
| Largo exterior | 104 mm |
| Ancho exterior | 82 mm |
| Altura total | 41 mm |
| Base | 38 mm |
| Tapa | 3 mm |
| Espesor de pared | 2,6 mm |
| Espesor del fondo | 3 mm |
| Paso del LED RGB | Ø 6,2 mm |
| Volumen de placa Leonardo | 68,6 × 53,4 × 1,6 mm |
| Tolerancia inicial del modelo | 0,25 mm |

Las medidas corresponden al CAD. Usamos volúmenes geométricos simples para representar la placa, el sensor y el LED. Para terminar el ensamble definitivo necesitamos comprobar el ajuste de la placa real, el puerto USB y el tipo exacto de módulo RGB.

## Cómo abrir el modelo en Fusion 360

1. Descargamos [ensamble_leonardo.step](fusion360/ensamble_leonardo.step).
2. Lo importamos en Fusion 360 como diseño nuevo.
3. Revisamos la posición y tamaño de la caja, tapa, Leonardo, LED y sonda.
4. Comprobamos interferencias y acceso a las conexiones.
5. Guardamos y exportamos el proyecto desde Fusion 360 como **.f3d o .f3z**, según corresponda.

El STEP sirve para trasladar los sólidos geométricos a Fusion 360, aunque **no reemplaza un archivo nativo de Fusion** hasta que lo abramos y guardemos desde allí. Conservamos además el código paramétrico con el que generamos el ensamble.

## Reparación y fabricación

Nuestra tapa se retira mediante tornillos. Esto nos permite acceder al circuito sin romper la pieza. La sonda sale por una abertura lateral y el puerto USB dispone de un espacio en la pared de la caja.

Para imprimir podemos utilizar PLA en condiciones de interior o PETG si buscamos mayor resistencia del material a ambientes húmedos. La carcasa no es impermeable. Antes de fabricar una nueva unidad contrastamos las dimensiones y tolerancias con el hardware real.

La primera versión de la caja se desarrolló para Arduino UNO. La conservamos en el historial, pero el modelo actual está preparado para el Leonardo.
