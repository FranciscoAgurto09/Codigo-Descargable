/*
  U2-E04 - Lectura ADC1 con promediado simple
  Placa: ESP32 DevKit V1 de 30 pines
  Monitor serie: 115200 bit/s

  Objetivo: leer un sensor analogico (por ejemplo un potenciometro) por
  un canal ADC1 y comparar la lectura cruda contra un promedio filtrado.

  GPIO34 es ADC1_CH6: solo entrada, sin pull-up/pull-down interno. Se usa
  un canal ADC1 (no ADC2) porque ADC2 comparte recursos con Wi-Fi y puede
  dejar de estar disponible si la radio esta activa (ver manual,
  seccion 2.4).
*/
const uint8_t PIN_ADC = 34;          // GPIO34, ADC1_CH6
const uint8_t NUM_MUESTRAS = 16;

void setup() {
  Serial.begin(115200);
  delay(300);
  analogReadResolution(12);          // 0 a 4095
  Serial.println("U2-E04 iniciado: lectura ADC1 en GPIO34");
}

void loop() {
  int crudo = analogRead(PIN_ADC);

  uint32_t suma = 0;
  for (uint8_t i = 0; i < NUM_MUESTRAS; i++) {
    suma += analogRead(PIN_ADC);
    delay(2);
  }
  int promedio = suma / NUM_MUESTRAS;

  float voltajeAprox = (promedio / 4095.0f) * 3.3f;

  Serial.print("Crudo: ");
  Serial.print(crudo);
  Serial.print("  Promedio(");
  Serial.print(NUM_MUESTRAS);
  Serial.print("): ");
  Serial.print(promedio);
  Serial.print("  Voltaje aprox.: ");
  Serial.print(voltajeAprox, 2);
  Serial.println(" V");

  delay(300);
}
