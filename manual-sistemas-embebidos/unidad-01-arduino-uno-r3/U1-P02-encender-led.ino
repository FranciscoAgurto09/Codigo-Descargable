/* ============================================================
   MANUAL EDUCATIVO DE SISTEMAS EMBEBIDOS
   Unidad 1 - Arduino Uno R3
   PRACTICA U1-P02 - Encender un LED
   ------------------------------------------------------------
   Objetivo:  controlar una salida digital y comprender el uso
              de la resistencia limitadora.
   Materiales: placa, protoboard, LED de 5 mm, resistencia de
              220 ohm y dos cables.
   Montaje:   anodo (terminal largo) -> resistencia -> pin 9
              catodo (terminal corto) -> GND
   ------------------------------------------------------------
   Autor: Francisco J. Agurto
   ============================================================ */

// ---- Constantes de configuracion ---------------------------
const byte          PIN_LED      = 9;     // usar LED_BUILTIN para probar sin cablear
const unsigned long T_ENCENDIDO  = 500;   // milisegundos en nivel alto
const unsigned long T_APAGADO    = 500;   // milisegundos en nivel bajo

// ============================================================
//  CONFIGURACION
// ============================================================
void setup() {
  // Sin esta declaracion el pin no se comporta como salida.
  pinMode(PIN_LED, OUTPUT);
}

// ============================================================
//  CICLO PRINCIPAL
// ============================================================
void loop() {
  digitalWrite(PIN_LED, HIGH);   // pin a 5 V  -> LED encendido
  delay(T_ENCENDIDO);            // el programa queda DETENIDO aqui

  digitalWrite(PIN_LED, LOW);    // pin a 0 V  -> LED apagado
  delay(T_APAGADO);
}

/* ------------------------------------------------------------
   VARIACIONES SUGERIDAS

   A) Parpadeo imperceptible: bajar los tiempos a 10 ms y luego
      a 2 ms. A partir de cierta frecuencia el ojo integra los
      pulsos y solo se percibe un LED mas tenue.

   B) Dos LED alternados: agregar un segundo LED en el pin 10
      y encender uno mientras el otro se apaga.

   C) Variar el brillo con PWM (el pin 9 lo admite):

        for (int v = 0; v <= 255; v++) { analogWrite(PIN_LED, v); delay(8); }
        for (int v = 255; v >= 0; v--) { analogWrite(PIN_LED, v); delay(8); }

   PARA PENSAR
   Con R = 220 ohm y un LED rojo de 2 V de caida alimentado
   desde un pin de 5 V:  I = (5 - 2) / 220 = 13,6 mA aprox.
   Que porcentaje representa del maximo recomendado de 20 mA?
   ------------------------------------------------------------ */
