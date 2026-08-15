/* ============================================================
   Unidad 1 - Arduino Uno R3
   EJERCICIO U1-E08 - Alarma de proximidad con zumbador
                                                   Nivel: avanzado
   ------------------------------------------------------------
   Se practica: sensor de distancia, medicion de tiempo y logica
                de umbral.
   Materiales:  sensor HC-SR04, zumbador pasivo, LED.
   Montaje:     VCC -> 5V   GND -> GND
                TRIG -> pin 9    ECHO -> pin 10
                zumbador -> pin 8    LED -> pin 13 (integrado)
   ------------------------------------------------------------
   Principio: TRIG emite un pulso de 10 microsegundos; el sensor
   lanza un tren de ultrasonido y ECHO permanece en alto el
   tiempo que tarda el eco en volver. El sonido viaja a unos
   343 m/s = 0,0343 cm por microsegundo, y el recorrido es de
   ida y vuelta, de ahi la division por 2.
   ------------------------------------------------------------
   Autor: Francisco J. Agurto
   ============================================================ */

const byte PIN_TRIG     = 9;
const byte PIN_ECHO     = 10;
const byte PIN_ZUMBADOR = 8;
const byte PIN_LED      = LED_BUILTIN;

const float DISTANCIA_ALARMA = 20.0;    // centimetros
const unsigned long TIEMPO_LIMITE = 30000UL;  // microsegundos (unos 5 m)

void setup() {
  pinMode(PIN_TRIG,     OUTPUT);
  pinMode(PIN_ECHO,     INPUT);
  pinMode(PIN_ZUMBADOR, OUTPUT);
  pinMode(PIN_LED,      OUTPUT);
  Serial.begin(9600);
  Serial.println(F("U1-E08 - Alarma de proximidad"));
}

void loop() {
  float distancia = medirDistancia();

  if (distancia > 0 && distancia < DISTANCIA_ALARMA) {
    tone(PIN_ZUMBADOR, 1500);           // zumbador pasivo: se le indica la nota
    digitalWrite(PIN_LED, HIGH);
  } else {
    noTone(PIN_ZUMBADOR);
    digitalWrite(PIN_LED, LOW);
  }

  Serial.print(F("Distancia: "));
  if (distancia > 0) {
    Serial.print(distancia, 1);
    Serial.println(F(" cm"));
  } else {
    Serial.println(F("fuera de rango"));
  }

  delay(120);   // el sensor necesita una pausa entre mediciones
}

// ---- Funcion propia ----------------------------------------
// Devuelve la distancia en centimetros, o -1 si no hubo eco.
float medirDistancia() {
  digitalWrite(PIN_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG, LOW);

  unsigned long duracion = pulseIn(PIN_ECHO, HIGH, TIEMPO_LIMITE);
  if (duracion == 0) return -1.0;       // no volvio el eco

  return (duracion * 0.0343) / 2.0;
}

/* ADVERTENCIA
   tone() utiliza el temporizador 2, por lo que mientras suena
   el zumbador los pines 3 y 11 no pueden entregar PWM.

   EXTENSIONES
   - Que la frecuencia del pitido suba al acercarse el objeto.
   - Promediar tres mediciones y descartar las lecturas anomalas.
   - Agregar un LED verde y uno rojo como semaforo de distancia. */
