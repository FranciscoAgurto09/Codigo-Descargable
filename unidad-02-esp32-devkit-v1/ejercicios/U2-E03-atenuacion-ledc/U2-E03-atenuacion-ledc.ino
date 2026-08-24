/*
  U2-E03 - Atenuacion con LEDC (efecto "respiracion")
  Placa: ESP32 DevKit V1 de 30 pines
  Monitor serie: 115200 bit/s

  Objetivo: generar PWM con el periferico LEDC y variar el ciclo de
  trabajo para producir un brillo creciente y decreciente en un LED.

  IMPORTANTE - version del nucleo Arduino-ESP32:
  Este sketch usa la API LEDC simplificada de la serie 3.x:
      ledcAttach(pin, frecuencia, resolucion_bits);
      ledcWrite(pin, valor_de_ciclo);
  Si el IDE tiene instalado un nucleo 2.x, esa API no existe y debe
  reemplazarse por la version anterior:
      ledcSetup(canal, frecuencia, resolucion_bits);
      ledcAttachPin(pin, canal);
      ledcWrite(canal, valor_de_ciclo);
  Registrar siempre la version del paquete "esp32" instalada en el
  informe de laboratorio (ver manual, seccion 2.6, nota sobre
  reproducibilidad).
*/
const uint8_t PIN_LED = 33;          // GPIO33, con capacidad PWM por LEDC
const uint32_t FRECUENCIA_HZ = 5000; // frecuencia del PWM
const uint8_t RESOLUCION_BITS = 8;   // ciclo de trabajo de 0 a 255
const uint8_t PASO = 5;
const uint16_t PAUSA_MS = 15;

void setup() {
  Serial.begin(115200);
  delay(300);
  ledcAttach(PIN_LED, FRECUENCIA_HZ, RESOLUCION_BITS);
  Serial.println("U2-E03 iniciado: atenuacion LEDC en GPIO33");
}

void loop() {
  for (int ciclo = 0; ciclo <= 255; ciclo += PASO) {
    ledcWrite(PIN_LED, ciclo);
    delay(PAUSA_MS);
  }
  for (int ciclo = 255; ciclo >= 0; ciclo -= PASO) {
    ledcWrite(PIN_LED, ciclo);
    delay(PAUSA_MS);
  }
}
