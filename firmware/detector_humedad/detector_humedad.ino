/*
  Detector de humedad del suelo - TEI201
  Placa: Arduino Leonardo
  Sensor: salida analogica A0
  LED RGB: rojo D9, verde D10, azul D11 (PWM)
  Calibracion del equipo: aire = 892, agua = 350
  Periodo nominal de muestreo: 1 segundo.

  IMPORTANTE: el porcentaje es un INDICE RELATIVO calculado entre dos
  referencias, NO un porcentaje de humedad volumetrica certificado.
  La salida PWM presupone LED de catodo comun (activo en alto) o modulo
  equivalente. Revisar las resistencias limitadoras y el pinout real.
*/

const int sensorPin = A0;
const int pinRojo = 9;
const int pinVerde = 10;
const int pinAzul = 11;

const int valorAire = 892;
const int valorAgua = 350;

void setup() {
  Serial.begin(9600);
  pinMode(pinRojo, OUTPUT);
  pinMode(pinVerde, OUTPUT);
  pinMode(pinAzul, OUTPUT);
}

void loop() {
  // 1. Leer la senal cruda del sensor capacitivo (ADC de 10 bits).
  int lecturaCruda = analogRead(sensorPin);

  // 2. Interpolar entre aire (0 %) y agua (100 %), limitar a 0-100.
  int porcentaje = map(lecturaCruda, valorAire, valorAgua, 0, 100);
  porcentaje = constrain(porcentaje, 0, 100);

  // 3. Formato estable para el monitor serial y el registrador CSV.
  Serial.print("Lectura cruda: ");
  Serial.print(lecturaCruda);
  Serial.print("  ->  Humedad: ");
  Serial.print(porcentaje);
  Serial.print("%  |  Estado: ");

  // 4. Tres estados de humedad y tres colores visibles.
  if (porcentaje < 20) {
    Serial.println("Seco");
    setColor(255, 0, 0);
  }
  else if (porcentaje < 40) {
    Serial.println("Humedo");
    setColor(0, 255, 0);
  }
  else {
    Serial.println("Muy humedo");
    setColor(0, 0, 255);
  }

  delay(1000);
}

void setColor(int rojo, int verde, int azul) {
  analogWrite(pinRojo, rojo);
  analogWrite(pinVerde, verde);
  analogWrite(pinAzul, azul);
}
