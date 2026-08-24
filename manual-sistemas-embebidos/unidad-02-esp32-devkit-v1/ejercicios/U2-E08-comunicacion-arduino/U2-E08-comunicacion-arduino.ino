/*
  U2-E08 - Comunicacion UART2 entre ESP32 y Arduino Uno R3
  Placa: ESP32 DevKit V1 de 30 pines
  Monitor serie (USB, hacia el computador): 115200 bit/s
  UART2 (hacia el Arduino): 9600 bit/s

  Objetivo: enviar y recibir mensajes cortos entre la ESP32 y un Arduino
  Uno R3 por un UART dedicado (UART2), dejando UART0 libre para el
  monitor serie y la programacion por USB.

  Asignacion en esta placa: UART2 RX = GPIO16, UART2 TX = GPIO17
  (ver manual, seccion 2.4).

  ADVERTENCIA ELECTRICA (ver manual, seccion 2.5):
  El Arduino Uno R3 trabaja a 5 V y sus GPIO no son compatibles
  directamente con la logica de 3,3 V de la ESP32.
    - Arduino TX (5 V) -> ESP32 RX (GPIO16): OBLIGATORIO usar un
      divisor resistivo o un conversor de nivel logico antes de
      conectar esta linea. Nunca conectar el TX de 5 V directo a un
      GPIO de la ESP32.
    - ESP32 TX (GPIO17, 3,3 V) -> Arduino RX: el Arduino suele
      reconocer 3,3 V como nivel alto, por lo que esta direccion es
      generalmente segura, pero conviene revisarlo si se cambia de
      placa Arduino.
    - GND de ambas placas debe unirse siempre.

  Este sketch define un protocolo minimo: una linea de texto terminada
  en salto de linea, con un caracter de suma de verificacion simple al
  final, para detectar mensajes corruptos.
*/
const uint32_t VELOCIDAD_UART2 = 9600;
const uint32_t INTERVALO_ENVIO_MS = 2000;

uint32_t ultimoEnvioMs = 0;
uint32_t contadorMensajes = 0;

uint8_t checksumSimple(const String& datos) {
  uint8_t suma = 0;
  for (size_t i = 0; i < datos.length(); i++) {
    suma ^= (uint8_t)datos[i]; // XOR de todos los bytes
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
  Serial.begin(115200);               // monitor serie por USB
  Serial2.begin(VELOCIDAD_UART2, SERIAL_8N1, 16, 17); // RX=16, TX=17
  delay(300);
  Serial.println("U2-E08 iniciado: UART2 hacia Arduino (RX=16, TX=17)");
}

void loop() {
  // Envio periodico de un mensaje de prueba al Arduino
  if (millis() - ultimoEnvioMs >= INTERVALO_ENVIO_MS) {
    ultimoEnvioMs = millis();
    contadorMensajes++;
    String mensaje = "ESP32:" + String(contadorMensajes);
    enviarMensaje(mensaje);
    Serial.print("Enviado por UART2: ");
    Serial.println(mensaje);
  }

  // Lectura de lo que llegue desde el Arduino
  if (Serial2.available()) {
    String recibido = Serial2.readStringUntil('\n');
    recibido.trim();
    Serial.print("Recibido desde Arduino: ");
    Serial.println(recibido);
  }
}
