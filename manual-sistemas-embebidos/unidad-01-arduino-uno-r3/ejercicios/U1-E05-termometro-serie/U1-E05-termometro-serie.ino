/* ============================================================
   Unidad 1 - Arduino Uno R3
   EJERCICIO U1-E05 - Termometro por monitor serie
                                                  Nivel: intermedio
   ------------------------------------------------------------
   Se practica: conversion de una lectura del conversor A/D a
                unidades fisicas.
   Materiales:  sensor LM35 (o TMP36).
   Montaje LM35 (mirando la cara plana, pines hacia abajo):
                izquierda -> 5V ; centro -> A0 ; derecha -> GND
   ------------------------------------------------------------
   Cada unidad del conversor equivale a 5 V / 1024 = 4,88 mV.
   El LM35 entrega 10 mV por grado Celsius, con 0 V a 0 C.
   ============================================================ */

const byte PIN_SENSOR   = A0;
const byte N_MUESTRAS   = 10;      // promedio para filtrar ruido
const unsigned long INTERVALO = 1000;

unsigned long tiempoAnterior = 0;

void setup() {
  Serial.begin(9600);
  Serial.println(F("U1-E05 - Termometro LM35"));
  Serial.println(F("Tiempo(s)\tLectura\tVolt(V)\tTemp(C)"));
}

void loop() {
  if (millis() - tiempoAnterior < INTERVALO) return;
  tiempoAnterior = millis();

  // ---- Promedio de varias lecturas -------------------------
  long suma = 0;
  for (byte i = 0; i < N_MUESTRAS; i++) {
    suma += analogRead(PIN_SENSOR);
    delay(5);
  }
  float lectura = (float)suma / N_MUESTRAS;

  // ---- Conversion a unidades fisicas -----------------------
  float tension     = lectura * (5.0 / 1023.0);   // volts
  float temperatura = tension * 100.0;            // LM35: 10 mV por grado
  // Para un TMP36 la formula seria: (tension - 0.5) * 100.0

  Serial.print(millis() / 1000);
  Serial.print(F("\t"));
  Serial.print(lectura, 1);
  Serial.print(F("\t"));
  Serial.print(tension, 3);
  Serial.print(F("\t"));
  Serial.println(temperatura, 1);
}

/* PARA PENSAR
   La resolucion del conversor es de 4,88 mV, es decir, unos
   0,5 C con el LM35. Que ganariamos usando analogReference()
   con una referencia interna de 1,1 V? */
