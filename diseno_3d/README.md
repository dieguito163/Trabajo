# Diseño 3D | detector de humedad

## Versión actual y archivos

- [CAD paramétrico Leonardo (OpenSCAD)](fusion360/caja_sensor_leonardo.scad) — base, tapa, probeta y vista con volúmenes representativos de Leonardo, LED y sonda.
- [Plano Leonardo (SVG)](planos/plano_leonardo.svg) — cotas **nominales**. La automatización intenta exportarlo también a PDF.
- [STL y referencias](stl/README.md) — generados automáticamente por GitHub Actions desde el CAD Leonardo al llegar a main.
- [Renders](renders/README.md) — render referencial generado a partir del CAD, **no fotografía**.
- [Fotografías reales](../hardware/fotos/README.md) — evidencia de la carcasa ensamblada.

La versión anterior **caja_sensor_humedad.scad** y los STL **base_arduino_uno.stl** son históricos; no deben identificarse como el CAD final del Leonardo.

## Parámetros nominales del archivo Leonardo

| Parámetro | Valor referencial |
|---|---|
| Dimensiones de caja | 104 × 82 × 41 mm (38 base + 3 tapa) |
| Pared lateral | 2,6 mm |
| Piso | 3 mm |
| LED frontal | Agujero Ø6,2 mm |
| Placa Leonardo | Volumen 68,6 × 53,4 × 1,6 mm |
| Tolerancia inicial CAD | 0,25 mm |
| Montaje tapa | 4 tornillos modelados |

Se reutilizó una distribución **referencial** de orificios tipo UNO/Leonardo del proyecto anterior. **No se han medido los centros reales del Leonardo instalado**. Las fotografías exteriores muestran una carcasa atornillada, pero no establecen las dimensiones ni garantizan que el archivo CAD encaje exactamente con la pieza ya impresa. Verificar también el número real y posición de tornillos.

## Generar e inspeccionar

En OpenSCAD abrir el CAD Leonardo, seleccionar una pieza cambiando la variable **pieza**, ejecutar **F6** y exportar como STL. Para el ensamble visual usar **pieza="vista"**; allí se muestran volúmenes aproximados del Leonardo, módulo RGB y sonda, con tapa separada para ver el interior.

El flujo [Generar STL](../.github/workflows/generar-stl.yml) crea modelos STL, render referencial y PDF del plano en GitHub tras incorporar los cambios a la rama principal.

## Requisito de Fusion 360

La pauta solicita un ensamble **Fusion 360 nativo .f3d o .f3z** con representación de componentes internos y planos. **Este archivo NO existe todavía en el repositorio y no sería correcto renombrar un STL como .f3d.** El equipo debe montar el gemelo en Fusion 360 y exportarlo, verificando tamaños y accesos reales.

## Reparabilidad y material

Carcasa desmontable con tornillos; desconectar USB antes de abrir. PLA o PETG como ejemplos de materiales de impresión, sin afirmar impermeabilidad. Mantener la electrónica y conectores secos. Revisar tolerancias, alivio de tensión del cable y fijación del módulo LED.
