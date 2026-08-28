/*
  RP3-P06 - Lado ESP32: emisor UART hacia la Raspberry Pi
  Placa: ESP32 DevKit V1 de 30 pines (Unidad 2)
  Monitor serie (USB, hacia el computador): 115200 bit/s
  UART2 (hacia la Raspberry Pi): 9600 bit/s

  Objetivo: adquirir una lectura simple (ADC1) y enviarla periodicamente por
  UART2 a la Raspberry Pi, usando el mismo protocolo de linea con suma de
  verificacion definido en la Unidad 2 (ejercicio U2-E08).

  Conexiones (ver tabla completa en el manual, RP3-P06):
    GPIO16 (UART2 RX) <- GPIO14 / TXD de la Raspberry Pi (pin fisico 8)
    GPIO17 (UART2 TX) -> GPIO15 / RXD de la Raspberry Pi (pin fisico 10)
    GND               -- GND de la Raspberry Pi

  IMPORTANTE: ambas placas trabajan a 3,3 V logicos; a diferencia de la
  pareja ESP32/Arduino Uno R3 de la Unidad 2, esta conexion NO requiere
  divisor resistivo ni conversor de nivel logico.
*/
const uint8_t PIN_ADC = 34;               // ADC1_CH6, lectura simulada de sensor
const uint32_t VELOCIDAD_UART2 = 9600;    // debe coincidir con RP3-P06-receptor.py
const uint32_t INTERVALO_ENVIO_MS = 2000;

uint32_t ultimoEnvioMs = 0;
uint32_t contadorMensajes = 0;

uint8_t checksumSimple(const String& datos) {
  uint8_t suma = 0;
  for (size_t i = 0; i < datos.length(); i++) {
    suma ^= (uint8_t)datos[i];
  }
  return suma;
}

void enviarMensaje(const String& datos) {
  uint8_t chk = checksumSimple(datos);
  Serial2.print(datos);
  Serial2.print('*');
  Serial2.println(chk, HEX);
}

void setup() {
  Serial.begin(115200);                                // monitor serie por USB
  Serial2.begin(VELOCIDAD_UART2, SERIAL_8N1, 16, 17);   // RX=16, TX=17
  delay(300);
  Serial.println("RP3-P06 (emisor ESP32) iniciado: UART2 hacia Raspberry Pi");
}

void loop() {
  if (millis() - ultimoEnvioMs >= INTERVALO_ENVIO_MS) {
    ultimoEnvioMs = millis();
    contadorMensajes++;

    int lectura = analogRead(PIN_ADC);
    String mensaje = "ESP32:" + String(contadorMensajes) + ":ADC=" + String(lectura);

    enviarMensaje(mensaje);
    Serial.print("Enviado por UART2: ");
    Serial.println(mensaje);
  }
}
