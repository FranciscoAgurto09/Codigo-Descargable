/*
  U2-E01 - Semaforo de tres LED
  Placa: ESP32 DevKit V1 de 30 pines
  Monitor serie: 115200 bit/s

  Objetivo: practicar varias salidas digitales y una secuencia de tiempos.
  GPIO32, 33 y 27 no son pines de arranque (strapping) ni estan reservados
  para la flash, por lo que son una eleccion segura para LED de practica.

  Ampliacion sugerida (ver manual, seccion 2.8): reemplazar los delay()
  bloqueantes por una maquina de estados basada en millis(), de modo que
  el programa pueda seguir atendiendo otras tareas durante la secuencia.
*/
const uint8_t PIN_ROJO     = 32;
const uint8_t PIN_AMARILLO = 33;
const uint8_t PIN_VERDE    = 27;

void setup() {
  Serial.begin(115200);
  pinMode(PIN_ROJO, OUTPUT);
  pinMode(PIN_AMARILLO, OUTPUT);
  pinMode(PIN_VERDE, OUTPUT);
  digitalWrite(PIN_ROJO, LOW);
  digitalWrite(PIN_AMARILLO, LOW);
  digitalWrite(PIN_VERDE, LOW);
  delay(300);
  Serial.println("U2-E01 iniciado: semaforo de tres LED");
}

void loop() {
  // Rojo
  digitalWrite(PIN_ROJO, HIGH);
  Serial.println("ROJO");
  delay(3000);
  digitalWrite(PIN_ROJO, LOW);

  // Verde
  digitalWrite(PIN_VERDE, HIGH);
  Serial.println("VERDE");
  delay(3000);
  digitalWrite(PIN_VERDE, LOW);

  // Amarillo (aviso antes de volver a rojo)
  digitalWrite(PIN_AMARILLO, HIGH);
  Serial.println("AMARILLO");
  delay(1000);
  digitalWrite(PIN_AMARILLO, LOW);
}
