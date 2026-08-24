/*
  U2-E05 - Escaner de direcciones I2C
  Placa: ESP32 DevKit V1 de 30 pines
  Monitor serie: 115200 bit/s

  Objetivo: recorrer el bus I2C y reportar que direcciones responden,
  para identificar sensores o modulos conectados sin conocer de antemano
  su direccion exacta.

  Asignacion convencional en esta placa: SDA = GPIO21, SCL = GPIO22
  (ver manual, seccion 2.4). El bus requiere resistencias de pull-up
  hacia 3,3 V; muchos modulos ya las traen integradas.
*/
#include <Wire.h>

void setup() {
  Serial.begin(115200);
  delay(300);
  Wire.begin(21, 22); // SDA, SCL
  Serial.println("U2-E05 iniciado: escaner I2C (SDA=21, SCL=22)");
}

void loop() {
  Serial.println("Escaneando bus I2C...");
  uint8_t dispositivosEncontrados = 0;

  for (uint8_t direccion = 1; direccion < 127; direccion++) {
    Wire.beginTransmission(direccion);
    uint8_t error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("Dispositivo encontrado en 0x");
      if (direccion < 16) Serial.print("0");
      Serial.println(direccion, HEX);
      dispositivosEncontrados++;
    }
  }

  if (dispositivosEncontrados == 0) {
    Serial.println("Ningun dispositivo respondio. Revisar cableado y pull-up.");
  } else {
    Serial.print("Total de dispositivos: ");
    Serial.println(dispositivosEncontrados);
  }

  delay(5000);
}
