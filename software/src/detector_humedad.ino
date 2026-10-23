// Demostración Arduino UNO + sensor capacitivo A0 + LED digital D8.
// PRECAUCIÓN: Verificar cableado, tensión y resistencia limitadora del LED.
// Calibrar lectura seca / húmeda antes de usar los umbrales.
const int PIN_SENSOR=A0;
const int PIN_LED=8;
const int UMBRAL_SECO=650;  // EJEMPLO: medir experimentalmente
bool secoCuandoMayor=true; // invertir si calibración lo determina
void setup(){pinMode(PIN_LED,OUTPUT);Serial.begin(9600);}
void loop(){
  int lectura=analogRead(PIN_SENSOR);
  bool sueloSeco=secoCuandoMayor ? lectura>=UMBRAL_SECO : lectura<=UMBRAL_SECO;
  digitalWrite(PIN_LED,sueloSeco?HIGH:LOW);
  Serial.print("ADC suelo: ");Serial.print(lectura);
  Serial.println(sueloSeco?" | Revisar riego":" | Humedad suficiente");
  delay(1000);
}
