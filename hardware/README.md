# Hardware

## Montaje

Utilizamos un Arduino Leonardo, un sensor capacitivo de humedad y un indicador LED RGB. Realizamos las conexiones de forma directa, sin protoboard, para reducir el espacio ocupado dentro de la carcasa. Ubicamos el sensor fuera de la caja para insertarlo en la tierra y dejamos una apertura para el cable.

Nuestro encapsulado está impreso en 3D y utiliza tornillos en la tapa. Podemos retirar la tapa para acceder a los componentes y realizar ajustes o reparaciones.

![Montaje exterior](fotos/vista_lateral.jpg)

## Selección de componentes

| Componente | ¿Por qué lo elegimos? | Características relevantes |
|---|---|---|
| Arduino Leonardo | Nos permite leer una señal analógica, controlar los tres canales RGB y comunicarnos por USB | ATmega32U4; entrada A0 de 10 bits; PWM D9, D10 y D11 |
| Sensor capacitivo de humedad | Nos permite identificar cambios en el estado del suelo sin utilizar dos electrodos metálicos expuestos como en un sensor resistivo | Salida analógica; alimentación según el módulo (referencia habitual 3,3–5 V) |
| LED RGB | Muestra el resultado directamente, sin incorporar una pantalla adicional | Tres canales de color con salidas PWM |
| Conectores y cables | Podemos conectar los elementos dentro de la caja sin utilizar una protoboard | Masas compartidas y conexiones aisladas |
| Carcasa impresa en 3D | Protege la electrónica de golpes y facilita mantener el montaje ordenado | Tapa atornillada, salida de cable, acceso al puerto USB |
| Cable USB | Permite alimentar y conectar el dispositivo con el programa de registro | Comunicación serial a 9600 baudios |

Nuestro diseño se alimenta desde USB cuando utilizamos el registro de datos. No incorporamos una batería al montaje descrito.

## Conexiones

| Elemento | Pin |
|---|---|
| Señal del sensor | A0 |
| Alimentación del sensor | VCC compatible con el módulo |
| Tierra del sensor | GND |
| Canal rojo del LED | D9 |
| Canal verde del LED | D10 |
| Canal azul del LED | D11 |
| Común del LED | Conexión según tipo de módulo RGB |
| Registro de datos | USB |

Nuestro código utiliza salidas PWM activas en alto. Para reproducir el montaje necesitamos revisar el orden de terminales del LED, su tipo de común y las resistencias limitadoras que corresponden al módulo instalado.

[Esquema y conexiones](esquemas/README.md) · [Lista de materiales](bom/README.md) · [Fotografías](fotos/README.md)

## Reparación

Para acceder a los componentes, primero desconectamos la alimentación USB. Luego retiramos los tornillos de la tapa y revisamos el cableado, la placa y el módulo LED. El diseño evita tener que romper la carcasa para reemplazar los componentes. El sistema está pensado para utilizarse en interiores y mantener la electrónica alejada del agua.
