/* ============================================================
   Unidad 1 - Arduino Uno R3
   EJERCICIO U1-E06 - Barra de nivel con cinco LED
                                                  Nivel: intermedio
   ------------------------------------------------------------
   Se practica: ciclos, arreglos y conversion de rangos.
   Materiales:  5 LED, 5 resistencias de 220 ohm, potenciometro.
   Montaje:     LED en los pines 2, 3, 4, 5 y 6.
                Cursor del potenciometro a A0.
   ------------------------------------------------------------
   Autor: Francisco J. Agurto
   ============================================================ */

const byte PIN_LEDS[] = {2, 3, 4, 5, 6};
const byte N_LEDS     = sizeof(PIN_LEDS) / sizeof(PIN_LEDS[0]);
const byte PIN_POTE   = A0;

void setup() {
  for (byte i = 0; i < N_LEDS; i++) {
    pinMode(PIN_LEDS[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  int lectura = analogRead(PIN_POTE);              // 0 .. 1023
  int nivel   = map(lectura, 0, 1023, 0, N_LEDS);  // 0 .. 5 LED encendidos
  nivel       = constrain(nivel, 0, N_LEDS);

  for (byte i = 0; i < N_LEDS; i++) {
    digitalWrite(PIN_LEDS[i], (i < nivel) ? HIGH : LOW);
  }

  Serial.print(F("Lectura: "));
  Serial.print(lectura);
  Serial.print(F("   LED encendidos: "));
  Serial.println(nivel);

  delay(80);
}

/* EXTENSIONES
   - Reemplazar el potenciometro por la LDR del ejercicio E04 y
     obtener un luxometro de barra.
   - Hacer que el ultimo LED de la barra parpadee al llegar al
     maximo, como aviso de nivel critico. */
