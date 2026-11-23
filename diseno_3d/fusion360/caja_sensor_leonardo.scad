// Detector humedad suelo TEI201 - referencia CAD para Arduino Leonardo (mm)
// NO es el archivo Fusion 360 nativo; verificar dimensiones y fijaciones del montaje real.
// Modos: pieza="base", "tapa", "calibracion", "ambas", "vista", "cerrada", "interior", "explosion".
pieza="vista"; $fn=48;
caja_x=104; caja_y=82; caja_alto=38; pared=2.6; piso=3; radio=4.5;
tapa_grosor=3; tolerancia=0.25; soporte_alto=6;
placa_x=13; placa_y=14; placa_largo=68.6; placa_ancho=53.4;
led_x=90; led_y=44; led_diam=6.2;
// Referencia geometrica de los orificios de placas tipo UNO/Leonardo; medir Leonardo real.
agujeros_leonardo=[[14,2.54],[15.24,50.8],[66.04,7.62],[66.04,35.56]];
tornillos=[[8,8],[caja_x-8,8],[8,caja_y-8],[caja_x-8,caja_y-8]];
module rect_redondeado(x,y,r){translate([r,r]) offset(r=r) square([x-2*r,y-2*r]);}
module casco(){
    linear_extrude(height=piso) rect_redondeado(caja_x,caja_y,radio);
    difference(){
        translate([0,0,piso]) linear_extrude(height=caja_alto-piso) rect_redondeado(caja_x,caja_y,radio);
        translate([0,0,piso-0.01]) linear_extrude(height=caja_alto-piso+0.02)
          offset(delta=-pared) rect_redondeado(caja_x,caja_y,radio);
    }
}
module base(){
    difference(){
        union(){
            casco();
            for(p=tornillos) translate([p[0],p[1],piso]) cylinder(d=9,h=caja_alto-piso);
            for(p=agujeros_leonardo) translate([placa_x+p[0],placa_y+p[1],piso]) cylinder(d=7,h=soporte_alto);
        }
        for(p=tornillos) translate([p[0],p[1],caja_alto-10]) cylinder(d=2.7,h=10.2);
        for(p=agujeros_leonardo) translate([placa_x+p[0],placa_y+p[1],piso+1.1]) cylinder(d=2.2,h=soporte_alto-1+0.05);
        // Puerto USB de Leonardo: ranura nominal, NO medida contra el conector real.
        translate([-1,24,10]) cube([pared+2.2,18,12]);
        // Salida lateral de cable de la sonda.
        translate([caja_x-pared-0.5,36,caja_alto-11]) cube([pared+1.5,12,11.4]);
    }
}
module tapa(){
    difference(){
        union(){
            linear_extrude(height=tapa_grosor) rect_redondeado(caja_x,caja_y,radio);
            p=pared+tolerancia;
            translate([caja_x/2-8,p,tapa_grosor]) cube([16,1.4,1.5]);
            translate([caja_x/2-8,caja_y-p-1.4,tapa_grosor]) cube([16,1.4,1.5]);
            translate([p,caja_y/2-7,tapa_grosor]) cube([1.4,14,1.5]);
            translate([caja_x-p-1.4,caja_y/2-7,tapa_grosor]) cube([1.4,14,1.5]);
            translate([39,42,tapa_grosor]) linear_extrude(height=0.5) text("HUMEDAD",size=7.7,font="Liberation Sans:style=Bold",halign="center",valign="center");
            translate([led_x,59,tapa_grosor]) linear_extrude(height=0.5) text("LED",size=5.1,font="Liberation Sans:style=Bold",halign="center",valign="center");
        }
        for(p=tornillos){
            translate([p[0],p[1],-0.2]) cylinder(d=3.4,h=tapa_grosor+0.5);
            translate([p[0],p[1],-0.05]) cylinder(d=6,h=1.05);
        }
        translate([led_x,led_y,-0.1]) cylinder(d=led_diam,h=tapa_grosor+0.8);
    }
}
module leonardo_ref(){
    color([0.08,0.30,0.55]) translate([placa_x,placa_y,piso+soporte_alto]) cube([placa_largo,placa_ancho,1.6]);
    color([0.72,0.76,0.81]) translate([placa_x-3,placa_y+15,piso+soporte_alto+1.6]) cube([10,8,4]);
    color([0.12,0.12,0.14]) translate([placa_x+26,placa_y+18,piso+soporte_alto+1.6]) cube([12,12,2]);
}
module rgb_ref(){
    color([0.15,0.28,0.17]) translate([led_x-7,led_y-7,caja_alto-6]) cube([14,14,2]);
    color([0.9,0.85,0.79]) translate([led_x,led_y,caja_alto-4]) sphere(d=5.5);
}
module sensor_ref(){
    color([0.15,0.18,0.18]) translate([caja_x+30,36,10])
      linear_extrude(height=1.6) polygon([[0,-11],[12,-11],[73,-5],[83,0],[73,5],[12,11],[0,11]]);
}
if(pieza=="base") base();
else if(pieza=="tapa") tapa();
else if(pieza=="calibracion") difference(){
    cube([42,14,5]);
    for(p=[[9,2.2],[21,2.7],[34,led_diam]]) translate([p[0],7,-0.1]) cylinder(d=p[1],h=5.2);
}
else if(pieza=="ambas"){base();translate([0,0,caja_alto+6]) tapa();}
else if(pieza=="cerrada"){
    color([0.80,0.82,0.82]) base();
    color([0.96,0.96,0.94]) translate([0,0,caja_alto]) tapa();
    color([0.88,0.24,0.22]) translate([led_x,led_y,caja_alto+tapa_grosor+1.2]) sphere(d=5.5);
    sensor_ref();
}
else if(pieza=="interior"){
    color([0.81,0.82,0.79]) base();
    leonardo_ref();
    rgb_ref();
    sensor_ref();
}
else if(pieza=="explosion"){
    color([0.82,0.83,0.80]) base();
    translate([0,0,13]) leonardo_ref();
    color([0.95,0.95,0.93]) translate([0,0,caja_alto+38]) tapa();
    color([0.1,0.25,0.17]) translate([0,0,18]) rgb_ref();
    sensor_ref();
}
else if(pieza=="vista"){
    color([0.72,0.77,0.77]) base(); leonardo_ref(); rgb_ref();
    color([0.95,0.95,0.91,0.55]) translate([0,0,caja_alto+14]) tapa();
    sensor_ref();
}
