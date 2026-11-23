"""Generamos un ensamble STEP en milímetros para abrirlo en Fusion 360.

La geometría de los componentes es referencial; el ensamble final debe
compararse con las medidas del montaje antes de exportar a .f3d/.f3z.
Requisitos: pip install cadquery
"""
from pathlib import Path
import cadquery as cq

OUT = Path(__file__).resolve().parent
LX, LY, H = 104.0, 82.0, 38.0
W, BASE = 2.6, 3.0
MOUNT = [(8, 8), (96, 8), (8, 74), (96, 74)]
PCB_HOLES = [(14, 2.54), (15.24, 50.8), (66.04, 7.62), (66.04, 35.56)]

caja = cq.Workplane('XY').box(LX, LY, H, centered=(False,False,False)).edges('|Z').fillet(4.5)
hueco = cq.Workplane('XY').box(LX-2*W, LY-2*W, H-BASE+0.1, centered=(False,False,False)).translate((W,W,BASE))
caja = caja.cut(hueco)
for x,y in MOUNT:
    caja = caja.union(cq.Workplane('XY').center(x,y).circle(4.5).extrude(H-BASE).translate((0,0,BASE)))
    caja = caja.cut(cq.Workplane('XY').center(x,y).circle(1.35).extrude(11).translate((0,0,H-11)))
for x,y in PCB_HOLES:
    sx,sy=x+13,y+14
    caja=caja.union(cq.Workplane('XY').center(sx,sy).circle(3.5).extrude(6).translate((0,0,BASE)))
    caja=caja.cut(cq.Workplane('XY').center(sx,sy).circle(1.10).extrude(5.9).translate((0,0,BASE+0.5)))
caja=caja.cut(cq.Workplane('XY').box(W+3,18,12,centered=(False,False,False)).translate((-1,24,10)))
caja=caja.cut(cq.Workplane('XY').box(W+4,12,11,centered=(False,False,False)).translate((LX-W-0.6,36,H-11)))

tapa=cq.Workplane('XY').box(LX,LY,3,centered=(False,False,False)).edges('|Z').fillet(4.5)
for x,y in MOUNT:
    tapa=tapa.cut(cq.Workplane('XY').center(x,y).circle(1.7).extrude(4))
tapa=tapa.cut(cq.Workplane('XY').center(90,44).circle(3.1).extrude(4)).translate((0,0,H))

leonardo=cq.Workplane('XY').box(68.6,53.4,1.6,centered=(False,False,False)).translate((13,14,9))
micro=cq.Workplane('XY').box(14,14,2,centered=(False,False,False)).translate((38,34,10.6))
usb=cq.Workplane('XY').box(11,10,6,centered=(False,False,False)).translate((12,33,10.6))
led=cq.Workplane('XY').center(90,44).circle(2.6).extrude(6).translate((0,0,H-4))
sensor=cq.Workplane('XY').box(98,23,1.6,centered=(False,False,False)).translate((LX+35,28,9))

ensamble=cq.Assembly(name='Detector_humedad_Leonardo')
ensamble.add(caja,name='Base',color=cq.Color(0.85,0.86,0.84))
ensamble.add(tapa,name='Tapa',color=cq.Color(0.94,0.94,0.91))
ensamble.add(leonardo,name='Arduino_Leonardo',color=cq.Color(0.06,0.26,0.58))
ensamble.add(micro,name='Chip_referencial',color=cq.Color(0.14,0.14,0.14))
ensamble.add(usb,name='Puerto_USB',color=cq.Color(0.57,0.60,0.60))
ensamble.add(led,name='Modulo_RGB',color=cq.Color(0.85,0.22,0.21))
ensamble.add(sensor,name='Sensor_externo',color=cq.Color(0.12,0.15,0.15))

destino=OUT/'ensamble_leonardo.step'
ensamble.save(str(destino),exportType='STEP')
print('Ensamble STEP generado:',destino)
