/* ============================================================
   MANUAL EDUCATIVO DE SISTEMAS EMBEBIDOS
   Unidad 1 - Arduino Uno R3
   PRACTICA U1-P01 - Hola mundo por monitor serie
   ------------------------------------------------------------
   Objetivo:  comprobar que la placa, el cable y el entorno
              funcionan, y aprender a leer los mensajes que
              envia el microcontrolador.
   Materiales: solo la placa y su cable USB. No se conecta
              ningun componente.
   Monitor serie: 9600 baudios.
   ------------------------------------------------------------
   Autor: ______________________   Fecha: ____________
   ============================================================ */

// ---- Constantes de configuracion ---------------------------
const unsigned long VELOCIDAD_SERIE = 9600;   // debe coincidir con el monitor
const unsigned long INTERVALO_MS    = 1000;   // un mensaje por segundo

// ---- Variables globales ------------------------------------
// Viven en la SRAM: su valor se pierde al cortar la energia
// o al presionar el boton de RESET.
unsigned long contador       = 0;
unsigned long tiempoAnterior = 0;

// ============================================================
//  CONFIGURACION - se ejecuta una sola vez
// ============================================================
void setup() {
  Serial.begin(VELOCIDAD_SERIE);

  // El macro F() guarda el texto en la memoria Flash en lugar
  // de la SRAM. Con solo 2 kB de SRAM, es una buena costumbre.
  Serial.println(F("=========================================="));
  Serial.println(F(" Arduino Uno R3 - U1-P01 Hola mundo"));
  Serial.println(F(" La placa, el cable y el IDE funcionan."));
  Serial.println(F("=========================================="));
}

// ============================================================
//  CICLO PRINCIPAL - se repite indefinidamente
// ============================================================
void loop() {
  unsigned long ahora = millis();   // milisegundos desde el encendido

  // Se compara el tiempo en lugar de usar delay(): asi el
  // programa nunca queda bloqueado y podria atender otras
  // tareas dentro del mismo loop().
  if (ahora - tiempoAnterior >= INTERVALO_MS) {
    tiempoAnterior = ahora;
    contador++;

    Serial.print(F("Segundos desde el encendido: "));
    Serial.println(contador);
  }
}

/* ------------------------------------------------------------
   PARA PENSAR
   1. Que ocurre con el contador al presionar RESET? Por que?
   2. En que memoria vive la variable "contador"?
   3. Que pasaria si el monitor se abre a 115200 baudios?
   ------------------------------------------------------------ */
