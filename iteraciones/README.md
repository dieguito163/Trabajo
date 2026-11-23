# Evolución del detector

Durante el desarrollo fuimos ajustando el circuito, el código y la carcasa para conseguir un montaje más compacto y fácil de utilizar.

1. **Primer montaje:** trabajamos con Arduino UNO, una sonda capacitiva y un indicador RGB. Esta versión nos permitió definir el funcionamiento inicial.
2. **Diseño de carcasa:** modelamos una base y una tapa en 3D, con salida para el cable del sensor y acceso al indicador.
3. **Montaje Leonardo:** cambiamos la placa por un Arduino Leonardo y eliminamos la protoboard. También revisamos los pines del LED y los puntos de calibración.
4. **Código de tres colores:** establecimos las indicaciones rojo, verde y azul según tres intervalos.
5. **Registro de datos:** incorporamos un programa de captura por USB y un dashboard local para analizar la evolución de las lecturas.

En general el prototipo responde como esperamos en las pruebas iniciales. Seguimos trabajando en la calibración para relacionar mejor la lectura con el estado real de la tierra.
