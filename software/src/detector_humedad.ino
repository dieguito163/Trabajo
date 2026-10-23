// 1. Configuración de los pines que conectamos
const int pinSensor = A0;
const int pinRojo = 11;
const int pinVerde = 10;
const int pinAzul = 9;

// 2. VALORES DE CALIBRACIÓN (¡Debes ajustar estos dos números!)
// Los sensores capacitivos suelen dar un número ALTO en seco y un número BAJO en agua.
int valorSeco = 895;    // Reemplaza por la lectura que te dé al aire libre
int valorHumedo = 767;  // Reemplaza por la lectura que te dé en un vaso con agua

void setup() {
  // Iniciar la comunicación con el computador para ver los datos en pantalla
  Serial.begin(9600); 
  
  // Configurar los pines del LED como salidas de energía
  pinMode(pinRojo, OUTPUT);
  pinMode(pinVerde, OUTPUT);
  pinMode(pinAzul, OUTPUT);
}

void loop() {
  // --- PASO 1: LECTURA ---
  int lecturaCruda = analogRead(pinSensor);
  
  // --- PASO 2: CONVERSIÓN A PORCENTAJE ---
  // map() convierte el rango de lecturas al rango 0-100%
  int porcentaje = map(lecturaCruda, valorSeco, valorHumedo, 0, 100);
  
  // constrain() evita que el porcentaje baje de 0% o suba de 100% 
  // (por si el sensor lee un valor un poco más extremo que tu calibración)
  porcentaje = constrain(porcentaje, 0, 100);
  
  // Mostrar los datos en el Monitor Serie (Lupa arriba a la derecha en el programa Arduino)
  Serial.print("Lectura del sensor: ");
  Serial.print(lecturaCruda);
  Serial.print(" | Humedad: ");
  Serial.print(porcentaje);
  Serial.println("%");

  // --- PASO 3: LÓGICA DE COLORES ---
  if (porcentaje >= 45) {
    // Verde (Humedad Óptima)
    setColor(0, 255, 0); 
  } 
  else if (porcentaje >= 25 && porcentaje < 45) {
    // Amarillo (Advertencia)
    // Para el amarillo mezclamos Rojo al máximo (255) y Verde a la mitad (150)
    setColor(255, 150, 0); 
  } 
  else {
    // Rojo (Riego Urgente)
    setColor(255, 0, 0); 
  }
  
  // Esperar 1 segundo antes de volver a medir para no saturar la placa
  delay(1000); 
}

// --- FUNCIÓN AUXILIAR PARA LOS COLORES ---
// analogWrite() usa los puertos PWM (~9, ~10, ~11) para regular la intensidad de 0 a 255
void setColor(int intensidadRojo, int intensidadVerde, int intensidadAzul) {
  analogWrite(pinRojo, intensidadRojo);
  analogWrite(pinVerde, intensidadVerde);
  analogWrite(pinAzul, intensidadAzul);
}