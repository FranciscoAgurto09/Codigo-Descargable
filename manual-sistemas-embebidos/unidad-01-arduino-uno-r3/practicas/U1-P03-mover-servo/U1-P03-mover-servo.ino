/* ============================================================
   MANUAL EDUCATIVO DE SISTEMAS EMBEBIDOS
   Unidad 1 - Arduino Uno R3
   PRACTICA U1-P03 - Mover un servomotor
   ------------------------------------------------------------
   Objetivo:  comandar un actuador con posicion controlada y
              reconocer la necesidad de alimentacion externa.
   Materiales: placa, servo SG90, fuente externa de 5 V o
              portapilas, protoboard y cables.
   Montaje:   senal (naranjo/amarillo) -> pin 9
              rojo   -> +5 V de la FUENTE EXTERNA
              cafe/negro -> GND de la fuente externa
   ------------------------------------------------------------
   ATENCION: la tierra de la fuente externa DEBE unirse al GND
   de la placa. Sin referencia comun el servo no recibe bien la
   senal. Alimentar el servo desde el pin 5V provoca reinicios.
   ------------------------------------------------------------
   Autor: ______________________   Fecha: ____________
   ============================================================ */

#include <Servo.h>     // biblioteca incluida por omision en el IDE

// ---- Objeto y constantes -----------------------------------
Servo miServo;

const byte          PIN_SERVO   = 9;     // la biblioteca Servo usa el
                                         // temporizador de los pines 9 y 10:
                                         // mientras se controla un servo,
                                         // esos pines pierden el PWM.
const unsigned long T_MOVIMIENTO = 800;  // pausa para dar tiempo al giro

// ============================================================
//  CONFIGURACION
// ============================================================
void setup() {
  miServo.attach(PIN_SERVO);
  miServo.write(90);          // posicion central de partida
  delay(T_MOVIMIENTO);
}

// ============================================================
//  CICLO PRINCIPAL
// ============================================================
void loop() {
  miServo.write(0);           // extremo inferior del recorrido
  delay(T_MOVIMIENTO);

  miServo.write(90);          // centro
  delay(T_MOVIMIENTO);

  miServo.write(180);         // extremo superior del recorrido
  delay(T_MOVIMIENTO);

  miServo.write(90);          // regreso al centro
  delay(T_MOVIMIENTO);
}

/* ------------------------------------------------------------
   QUE DEBE OCURRIR
   El eje gira hasta cada posicion y se mantiene alli,
   resistiendo pequenas fuerzas externas. Un zumbido permanente
   indica que el servo esta forzando contra un tope mecanico:
   se debe reducir el rango (por ejemplo, de 10 a 170 grados).

   PARA PENSAR
   Un servo estandar solo recorre unos 180 grados. Por que esa
   limitacion es una ventaja en un brazo mecanico y una
   desventaja en una rueda?
   ------------------------------------------------------------ */
