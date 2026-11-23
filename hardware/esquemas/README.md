# Esquema y conexiones

Utilizamos un Arduino Leonardo, un sensor capacitivo y un LED RGB. Conectamos el sensor a A0 y los canales de color a D9 (rojo), D10 (verde) y D11 (azul). Eliminamos la protoboard para reducir el volumen del montaje.

![Esquema de conexiones](esquematico_detallado.svg)

Podemos consultar el [esquemático en PDF](esquematico_leonardo.pdf) para seguir cada conexión. Las resistencias en serie corresponden a un LED RGB sin limitadores integrados; si nuestro módulo ya los incorpora no duplicamos estas resistencias. El programa actual supone un indicador activo en alto, por lo que verificamos el tipo de LED y su pinout.

También conservamos el [diagrama general del sistema](esquema_leonardo.svg).
