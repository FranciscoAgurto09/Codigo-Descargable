/* ============================================================
   Unidad 1 - Arduino Uno R3
   EJERCICIO U1-E01 - Semaforo de tres LED          Nivel: basico
   ------------------------------------------------------------
   Se practica: secuencias temporizadas y orden de ejecucion.
   Materiales:  3 LED (rojo, amarillo, verde), 3 resistencias de
                220 ohm, protoboard y cables.
   Montaje:     rojo -> pin 4, amarillo -> pin 3, verde -> pin 2
                (cada anodo con su resistencia; catodos a GND)
   ------------------------------------------------------------
   Autor: Francisco J. Agurto
   ============================================================ */

const byte PIN_ROJO     = 4;
const byte PIN_AMARILLO = 3;
const byte PIN_VERDE    = 2;

const unsigned long T_ROJO     = 5000;
const unsigned long T_VERDE    = 4000;
const unsigned long T_AMARILLO = 1500;

void setup() {
  pinMode(PIN_ROJO,     OUTPUT);
  pinMode(PIN_AMARILLO, OUTPUT);
  pinMode(PIN_VERDE,    OUTPUT);
  apagarTodos();
}

void loop() {
  encenderSolo(PIN_ROJO);       delay(T_ROJO);
  encenderSolo(PIN_VERDE);      delay(T_VERDE);
  encenderSolo(PIN_AMARILLO);   delay(T_AMARILLO);
}

// ---- Funciones propias -------------------------------------
void apagarTodos() {
  digitalWrite(PIN_ROJO,     LOW);
  digitalWrite(PIN_AMARILLO, LOW);
  digitalWrite(PIN_VERDE,    LOW);
}

void encenderSolo(byte pin) {
  apagarTodos();
  digitalWrite(pin, HIGH);
}

/* EXTENSIONES
   - Modo intermitente nocturno: solo el amarillo parpadeando.
   - Reescribir la secuencia con millis() en lugar de delay(),
     de modo que el programa pueda atender un pulsador. */
