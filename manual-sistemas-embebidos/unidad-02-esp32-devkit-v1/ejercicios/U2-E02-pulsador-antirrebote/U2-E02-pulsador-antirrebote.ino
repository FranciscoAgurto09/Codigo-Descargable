/*
  U2-E02 - Pulsador con antirrebote (debounce)
  Placa: ESP32 DevKit V1 de 30 pines
  Monitor serie: 115200 bit/s

  Objetivo: leer una entrada digital con antirrebote por software y
  contar pulsaciones reales, distinguiendolas de los rebotes mecanicos
  del boton.

  GPIO27 admite resistencia de pull-up interna (INPUT_PULLUP), por lo que
  el boton se conecta simplemente entre GPIO27 y GND, sin resistencia
  externa. GPIO32 se usa como salida para el LED indicador.
*/
const uint8_t PIN_BOTON = 27;
const uint8_t PIN_LED   = 32;
const uint32_t TIEMPO_ANTIRREBOTE_MS = 40;

bool estadoLed = false;
int  lecturaAnterior = HIGH;
int  estadoEstable    = HIGH;
uint32_t ultimoCambioMs = 0;
uint32_t contadorPulsaciones = 0;

void setup() {
  Serial.begin(115200);
  pinMode(PIN_BOTON, INPUT_PULLUP); // reposo en HIGH, presionado = LOW
  pinMode(PIN_LED, OUTPUT);
  digitalWrite(PIN_LED, LOW);
  delay(300);
  Serial.println("U2-E02 iniciado: pulsador con antirrebote en GPIO27");
}

void loop() {
  int lecturaActual = digitalRead(PIN_BOTON);

  if (lecturaActual != lecturaAnterior) {
    ultimoCambioMs = millis();
  }

  if ((millis() - ultimoCambioMs) > TIEMPO_ANTIRREBOTE_MS) {
    if (lecturaActual != estadoEstable) {
      estadoEstable = lecturaActual;
      if (estadoEstable == LOW) { // flanco de bajada = pulsacion valida
        contadorPulsaciones++;
        estadoLed = !estadoLed;
        digitalWrite(PIN_LED, estadoLed ? HIGH : LOW);
        Serial.print("Pulsacion valida numero ");
        Serial.println(contadorPulsaciones);
      }
    }
  }

  lecturaAnterior = lecturaActual;
}
