/* ============================================================
   Unidad 1 - Arduino Uno R3
   EJERCICIO U1-E02 - LED comandado por pulsador    Nivel: basico
   ------------------------------------------------------------
   Se practica: entradas digitales y resistencia de polarizacion
                interna (INPUT_PULLUP).
   Materiales:  1 pulsador, 1 LED, 1 resistencia de 220 ohm.
   Montaje:     pulsador entre el pin 2 y GND (sin resistencia
                externa: se usa la interna de la placa).
                LED -> resistencia -> pin 9;  catodo a GND.
   ------------------------------------------------------------
   IMPORTANTE: con INPUT_PULLUP la logica se invierte.
   Pulsador SUELTO   -> el pin lee HIGH  (5 V por la interna)
   Pulsador PRESIONADO -> el pin lee LOW (queda unido a GND)
   ------------------------------------------------------------
   Autor: Francisco J. Agurto
   ============================================================ */

const byte PIN_BOTON = 2;
const byte PIN_LED   = 9;

void setup() {
  pinMode(PIN_BOTON, INPUT_PULLUP);   // sin esto la entrada queda "flotante"
  pinMode(PIN_LED,   OUTPUT);
}

void loop() {
  bool presionado = (digitalRead(PIN_BOTON) == LOW);
  digitalWrite(PIN_LED, presionado ? HIGH : LOW);
}

/* ------------------------------------------------------------
   VARIACION: encendido conmutado con antirrebote
   El LED cambia de estado en cada pulsacion y se mantiene.
   Reemplace loop() por el siguiente codigo:

   bool estadoLed = false;
   bool anterior  = HIGH;
   unsigned long ultimoCambio = 0;
   const unsigned long REBOTE = 40;   // milisegundos

   void loop() {
     bool lectura = digitalRead(PIN_BOTON);
     if (lectura != anterior && millis() - ultimoCambio > REBOTE) {
       ultimoCambio = millis();
       if (lectura == LOW) {                 // flanco de bajada
         estadoLed = !estadoLed;
         digitalWrite(PIN_LED, estadoLed);
       }
       anterior = lectura;
     }
   }
   ------------------------------------------------------------ */
