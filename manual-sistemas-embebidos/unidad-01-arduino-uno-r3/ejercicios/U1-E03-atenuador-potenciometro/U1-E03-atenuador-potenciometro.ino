/* ============================================================
   Unidad 1 - Arduino Uno R3
   EJERCICIO U1-E03 - Atenuador con potenciometro  Nivel: intermedio
   ------------------------------------------------------------
   Se practica: lectura analogica, conversion de rangos (map) y
                salida PWM.
   Materiales:  potenciometro de 10 k, 1 LED, resistencia 220 ohm.
   Montaje:     extremos del potenciometro a 5V y GND;
                cursor (pin central) a A0.
                LED -> resistencia -> pin 9 (pin con PWM).
   ------------------------------------------------------------
   Autor: Francisco J. Agurto
   ============================================================ */

const byte PIN_POTE = A0;
const byte PIN_LED  = 9;      // debe ser un pin marcado con ~

void setup() {
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int lectura = analogRead(PIN_POTE);          // 0 .. 1023 (conversor de 10 bits)
  int brillo  = map(lectura, 0, 1023, 0, 255); // 0 .. 255  (ciclo de trabajo PWM)
  brillo      = constrain(brillo, 0, 255);     // nunca fuera del rango seguro

  analogWrite(PIN_LED, brillo);

  Serial.print(F("Lectura: "));
  Serial.print(lectura);
  Serial.print(F("   Brillo PWM: "));
  Serial.println(brillo);

  delay(50);
}

/* PARA PENSAR
   analogWrite() NO entrega una tension intermedia: conmuta
   entre 0 y 5 V a unos 490 Hz. El LED parece atenuado porque
   responde al promedio, pero un osciloscopio veria pulsos. */
