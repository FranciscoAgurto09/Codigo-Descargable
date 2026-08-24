/*
  U2-E09 - Nodo de bajo consumo con deep-sleep
  Placa: ESP32 DevKit V1 de 30 pines
  Monitor serie: 115200 bit/s

  Objetivo: despertar periodicamente desde sueño profundo (deep-sleep),
  tomar una lectura, imprimirla y volver a dormir, simulando un nodo de
  sensado de bajo consumo.

  En deep-sleep se apagan los nucleos y la mayoria de los perifericos;
  solo permanece un subconjunto del dominio RTC. Por eso las variables
  normales se pierden entre ciclos: para conservar un dato (como el
  contador de ciclos) se declara en memoria RTC con RTC_DATA_ATTR.

  Para medir el ahorro real de energia se necesita un multimetro o un
  medidor de corriente en serie con la alimentacion; el consumo del
  chip en el datasheet no incluye el regulador ni el LED de la placa
  (ver manual, seccion 2.3).
*/
#include <esp_sleep.h>

const uint8_t  PIN_ADC = 34;              // ADC1_CH6, lectura simulada de sensor
const uint64_t TIEMPO_SUENO_US = 15ULL * 1000000ULL; // 15 segundos

RTC_DATA_ATTR uint32_t contadorCiclos = 0;

void setup() {
  Serial.begin(115200);
  delay(300);

  contadorCiclos++;

  Serial.println();
  Serial.println("U2-E09 - Nodo con deep-sleep");
  Serial.print("Ciclo numero: ");
  Serial.println(contadorCiclos);

  int lectura = analogRead(PIN_ADC);
  float voltajeAprox = (lectura / 4095.0f) * 3.3f;
  Serial.print("Lectura ADC1 (GPIO34): ");
  Serial.print(lectura);
  Serial.print("  ~");
  Serial.print(voltajeAprox, 2);
  Serial.println(" V");

  Serial.print("Entrando a deep-sleep por ");
  Serial.print(TIEMPO_SUENO_US / 1000000ULL);
  Serial.println(" segundos...");
  Serial.flush(); // asegura que el mensaje salga antes de dormir

  esp_sleep_enable_timer_wakeup(TIEMPO_SUENO_US);
  esp_deep_sleep_start();
  // El programa no continua desde aqui: al despertar, se reinicia
  // y setup() se ejecuta nuevamente desde el principio.
}

void loop() {
  // No se usa: cada ciclo comienza y termina dentro de setup().
}
