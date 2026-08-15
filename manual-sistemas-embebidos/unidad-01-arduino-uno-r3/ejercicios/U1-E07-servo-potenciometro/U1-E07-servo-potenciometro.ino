/* ============================================================
   Unidad 1 - Arduino Uno R3
   EJERCICIO U1-E07 - Servo comandado por potenciometro
                                                  Nivel: intermedio
   ------------------------------------------------------------
   Se practica: control proporcional de un actuador.
   Materiales:  servo SG90, potenciometro de 10 k, fuente
                externa de 5 V para el servo.
   Montaje:     senal del servo -> pin 9
                alimentacion del servo -> FUENTE EXTERNA
                GND de la fuente UNIDO al GND de la placa
                cursor del potenciometro -> A0
   ------------------------------------------------------------
   Autor: Francisco J. Agurto
   ============================================================ */

#include <Servo.h>

Servo miServo;

const byte PIN_SERVO = 9;
const byte PIN_POTE  = A0;

// El conversor entrega pequenas variaciones aunque el
// potenciometro no se mueva. Solo se ordena un movimiento nuevo
// si el cambio supera este margen: evita el temblor del eje.
const byte MARGEN_GRADOS = 2;

int anguloActual = 90;

void setup() {
  miServo.attach(PIN_SERVO);
  miServo.write(anguloActual);
  Serial.begin(9600);
  delay(500);
}

void loop() {
  int lectura = analogRead(PIN_POTE);
  int angulo  = map(lectura, 0, 1023, 0, 180);
  angulo      = constrain(angulo, 0, 180);

  if (abs(angulo - anguloActual) >= MARGEN_GRADOS) {
    anguloActual = angulo;
    miServo.write(anguloActual);

    Serial.print(F("Lectura: "));
    Serial.print(lectura);
    Serial.print(F("   Angulo: "));
    Serial.println(anguloActual);
  }

  delay(20);   // tiempo minimo entre ordenes al servo
}

/* RECORDATORIO
   La biblioteca Servo toma el temporizador de los pines 9 y 10:
   mientras haya un servo conectado, esos dos pines no pueden
   entregar PWM con analogWrite(). */
