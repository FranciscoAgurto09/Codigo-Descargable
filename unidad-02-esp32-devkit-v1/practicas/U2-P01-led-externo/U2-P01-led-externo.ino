/*
  U2-P01 - LED externo en GPIO23
  Placa: ESP32 DevKit V1 de 30 pines
  Monitor serie: 115200 bit/s
*/
const uint8_t PIN_LED = 23;
const uint32_t INTERVALO_MS = 1000;
void setup() {
  // Abre el monitor serie para observar evidencia del programa.
  Serial.begin(115200);
  // GPIO23 se utilizara como salida digital.
  pinMode(PIN_LED, OUTPUT);
  // Se parte con el LED apagado para tener un estado conocido.
  digitalWrite(PIN_LED, LOW);
  delay(300);
  Serial.println("U2-P01 iniciada: LED externo en GPIO23");
}
void loop() {
  digitalWrite(PIN_LED, HIGH);
  Serial.println("LED ENCENDIDO");
  delay(INTERVALO_MS);
  digitalWrite(PIN_LED, LOW);
  Serial.println("LED APAGADO");
  delay(INTERVALO_MS);
}
