/* ============================================================
   Unidad 1 - Arduino Uno R3
   EJERCICIO U1-E04 - Luz automatica con fotorresistencia
                                                  Nivel: intermedio
   ------------------------------------------------------------
   Se practica: divisor de tension y decision por umbral.
   Materiales:  LDR, resistencia de 10 k, LED, resistencia 220 ohm.
   Montaje (divisor de tension):
                5V ---- LDR ----+---- 10k ---- GND
                                |
                                A0
                Con mas luz la LDR baja su resistencia y la
                lectura en A0 SUBE.
   ------------------------------------------------------------
   Autor: Francisco J. Agurto
   ============================================================ */

const byte PIN_LDR = A0;
const byte PIN_LED = 9;

// Dos umbrales en lugar de uno: esto se llama HISTERESIS y evita
// que el LED parpadee sin control cuando la luz queda justo en
// el limite. Ajustelos observando el monitor serie.
const int UMBRAL_ENCENDER = 350;   // por debajo de esto: esta oscuro
const int UMBRAL_APAGAR   = 450;   // por encima de esto: hay luz

bool luzEncendida = false;

void setup() {
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(9600);
  Serial.println(F("U1-E04 - Tape y destape la LDR para calibrar"));
}

void loop() {
  int lectura = analogRead(PIN_LDR);

  if (!luzEncendida && lectura < UMBRAL_ENCENDER) {
    luzEncendida = true;
  } else if (luzEncendida && lectura > UMBRAL_APAGAR) {
    luzEncendida = false;
  }

  digitalWrite(PIN_LED, luzEncendida ? HIGH : LOW);

  Serial.print(F("Luz: "));
  Serial.print(lectura);
  Serial.print(F("   LED: "));
  Serial.println(luzEncendida ? F("ENCENDIDO") : F("apagado"));

  delay(200);
}
