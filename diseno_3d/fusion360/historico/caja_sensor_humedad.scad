// Detector de humedad TEI201 — carcasa paramétrica (mm)
// MODELO PRELIMINAR. Medir Arduino, USB, jack, LED y cables antes de imprimir.
// Exportar seleccionando pieza="base", "tapa" o "calibracion" y F6.
pieza="vista"; $fn=48;
caja_x=104; caja_y=82; caja_alto=38;
pared=2.6; piso=3; radio=4.5; tapa_grosor=3; tolerancia=.25;
placa_x=13; placa_y=14; soporte_alto=6;
led_x=90; led_y=44; led_diam=6.2;
agujeros_uno=[[14,2.54],[15.24,50.8],[66.04,7.62],[66.04,35.56]];
tornillos=[[8,8],[caja_x-8,8],[8,caja_y-8],[caja_x-8,caja_y-8]];
module rect_redondeado(x,y,r) {translate([r,r]) offset(r=r) square([x-2*r,y-2*r]);}
module casco() {
    linear_extrude(height=piso) rect_redondeado(caja_x,caja_y,radio);
    difference() {
        translate([0,0,piso]) linear_extrude(height=caja_alto-piso) rect_redondeado(caja_x,caja_y,radio);
        translate([0,0,piso-.01]) linear_extrude(height=caja_alto-piso+.02)
            offset(delta=-pared) rect_redondeado(caja_x,caja_y,radio);
    }
}
module base() {
    difference() {
        union() {
            casco();
            for(p=tornillos) translate([p[0],p[1],piso]) cylinder(d=9,h=caja_alto-piso);
            for(p=agujeros_uno) translate([placa_x+p[0],placa_y+p[1],piso]) cylinder(d=7,h=soporte_alto);
            for(y0=[32,52]) translate([caja_x-13,y0,piso]) cube([5,3,7]);
        }
        for(p=tornillos) translate([p[0],p[1],caja_alto-10]) cylinder(d=2.7,h=10.2);
        for(p=agujeros_uno) translate([placa_x+p[0],placa_y+p[1],piso+1.1]) cylinder(d=2.2,h=soporte_alto-1+.05);
        // Aperturas aproximadas para USB-B y jack DC (lado X negativo)
        translate([-1,10,7]) cube([pared+2.2,24,21]);
        translate([-1,38,7]) cube([pared+2.2,31,22]);
        // Salida cable sensor (parte superior lateral)
        translate([caja_x-pared-.5,36,caja_alto-11]) cube([pared+1.5,12,11.4]);
    }
}
module tapa() {
    difference() {
        union() {
            linear_extrude(height=tapa_grosor) rect_redondeado(caja_x,caja_y,radio);
            // pestañas guía interiores
            p=pared+tolerancia;
            translate([caja_x/2-8,p,tapa_grosor]) cube([16,1.4,1.5]);
            translate([caja_x/2-8,caja_y-p-1.4,tapa_grosor]) cube([16,1.4,1.5]);
            translate([p,caja_y/2-7,tapa_grosor]) cube([1.4,14,1.5]);
            translate([caja_x-p-1.4,caja_y/2-7,tapa_grosor]) cube([1.4,14,1.5]);
            translate([39,42,tapa_grosor]) linear_extrude(height=.5) text("HUMEDAD",size=7.7,font="Liberation Sans:style=Bold",halign="center",valign="center");
            translate([led_x,59,tapa_grosor]) linear_extrude(height=.5) text("LED",size=5.1,font="Liberation Sans:style=Bold",halign="center",valign="center");
        }
        for(p=tornillos) {
            translate([p[0],p[1],-.2]) cylinder(d=3.4,h=tapa_grosor+.5);
            translate([p[0],p[1],-.05]) cylinder(d=6,h=1.05);
        }
        translate([led_x,led_y,-.1]) cylinder(d=led_diam,h=tapa_grosor+.8);
    }
}
module arduino_ref(){
    color([.05,.22,.53]) translate([placa_x,placa_y,piso+soporte_alto]) cube([68.6,53.4,1.6]);
    color([.7,.73,.75]) translate([placa_x-6,placa_y+33.5,piso+soporte_alto+1.6]) cube([17,14,11]);
    color([.1,.1,.12]) translate([placa_x-2,placa_y+1.5,piso+soporte_alto+1.6]) cube([18,12,11]);
}
module sensor_ref(){
    color([.12,.17,.17]) translate([caja_x+37,36,10])
        linear_extrude(height=1.6) polygon([[0,-11],[12,-11],[74,-5],[83,0],[74,5],[12,11],[0,11]]);
}
if(pieza=="base") base();
else if(pieza=="tapa") tapa();
else if(pieza=="calibracion") difference(){
    cube([42,14,5]);
    for(p=[[9,2.2],[21,2.7],[34,led_diam]]) translate([p[0],7,-.1]) cylinder(d=p[1],h=5.2);
}
else if(pieza=="ambas"){base();translate([0,0,caja_alto+6]) tapa();}
else if(pieza=="vista"){
    color([.12,.23,.21]) base(); arduino_ref();
    color([.25,.69,.47,.75]) translate([0,0,caja_alto+15]) tapa();
    color([.95,.20,.15]) translate([led_x,led_y,caja_alto+14]) sphere(d=4.6);
    sensor_ref();
}