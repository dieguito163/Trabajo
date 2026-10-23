# Calibración y lectura de humedad

El código del equipo define `valorSeco=895` y `valorHumedo=767`. Estos valores deben comprobarse con la sonda real.

1. Cargar el sketch y observar `Lectura del sensor` en el Monitor Serie (9600 baudios).
2. Registrar varias lecturas en aire y luego en condiciones húmedas apropiadas para la sonda. Evitar sumergir su placa electrónica/conector si no está preparado para ello.
3. Ajustar `valorSeco` y `valorHumedo` a las lecturas registradas; comprobar que el resultado aumenta con la humedad.
4. Comprobar la correspondencia visual de los tres colores y evaluar si los umbrales 25 % y 45 % son apropiados para la planta/tierra concreta.

## Mapa RGB (programa actual)

- Verde: 45–100 %, RGB (0,255,0).
- Amarillo: 25–44 %, RGB (255,150,0).
- Rojo: 0–24 %, RGB (255,0,0).

**Nota:** `analogWrite` requiere un circuito LED con corriente limitada y compatible con PWM. Un LED RGB de ánodo común suele requerir invertir los tres niveles.
