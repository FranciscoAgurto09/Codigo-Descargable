/*
  U2-P02 - Servomotor SG90 en GPIO18
  Placa: ESP32 DevKit V1 de 30 pines
  Biblioteca: ESP32Servo
  Alimentacion del servo: fuente externa de 5 V con GND comun
  Monitor serie: 115200 bit/s
*/
#include <ESP32Servo.h>
Servo servo;
const uint8_t PIN_SERVO = 18;
const int ANGULO_MINIMO = 10;
const int ANGULO_MAXIMO = 170;
const int PASO = 2;
const uint16_t PAUSA_MS = 20;
void setup() {
  Serial.begin(115200);
  delay(300);
  // Reserva un temporizador PWM para la biblioteca.
  ESP32PWM::allocateTimer(0);
  // Los servos convencionales reciben una orden de 50 Hz.
  servo.setPeriodHertz(50);
  // 500 y 2400 us son valores iniciales de trabajo.
  // Deben ajustarse si el servo zumba o alcanza un tope mecanico.
  servo.attach(PIN_SERVO, 500, 2400);
  servo.write(90);
  Serial.println("U2-P02 iniciada: servo centrado en 90 grados");
  delay(1000);
}
void loop() {
  Serial.println("Barrido ascendente");
  for (int angulo = ANGULO_MINIMO;
       angulo <= ANGULO_MAXIMO;
       angulo += PASO) {
    servo.write(angulo);
    delay(PAUSA_MS);
  }
  delay(400);
  Serial.println("Barrido descendente");
  for (int angulo = ANGULO_MAXIMO;
       angulo >= ANGULO_MINIMO;
       angulo -= PASO) {
    servo.write(angulo);
    delay(PAUSA_MS);
  }
  delay(400);
}
