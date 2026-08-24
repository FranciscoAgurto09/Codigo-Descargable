/*
  U2-E06 - Escaner de redes Wi-Fi
  Placa: ESP32 DevKit V1 de 30 pines
  Monitor serie: 115200 bit/s

  Objetivo: usar el modo estacion para buscar redes Wi-Fi cercanas y
  registrar SSID, intensidad de senal (RSSI) y tipo de seguridad.
  No requiere conectarse a ninguna red.

  Nota: el ESP32 solo ve redes de 2,4 GHz (802.11 b/g/n). Una red de
  5 GHz simplemente no aparecera en el listado.
*/
#include <WiFi.h>

void setup() {
  Serial.begin(115200);
  delay(300);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect(); // asegura que no intente conectarse a nada
  delay(100);
  Serial.println("U2-E06 iniciado: escaner de redes Wi-Fi (2,4 GHz)");
}

void loop() {
  Serial.println("Buscando redes...");
  int redesEncontradas = WiFi.scanNetworks();

  if (redesEncontradas == 0) {
    Serial.println("No se encontraron redes.");
  } else {
    Serial.print(redesEncontradas);
    Serial.println(" redes encontradas:");
    Serial.println("Num | RSSI (dBm) | Seguridad       | SSID");

    for (int i = 0; i < redesEncontradas; i++) {
      Serial.printf("%3d | %10d | ", i + 1, WiFi.RSSI(i));

      switch (WiFi.encryptionType(i)) {
        case WIFI_AUTH_OPEN:            Serial.print("ABIERTA         "); break;
        case WIFI_AUTH_WEP:             Serial.print("WEP             "); break;
        case WIFI_AUTH_WPA_PSK:         Serial.print("WPA-PSK         "); break;
        case WIFI_AUTH_WPA2_PSK:        Serial.print("WPA2-PSK        "); break;
        case WIFI_AUTH_WPA_WPA2_PSK:    Serial.print("WPA/WPA2-PSK    "); break;
        case WIFI_AUTH_WPA2_ENTERPRISE: Serial.print("WPA2-ENTERPRISE "); break;
        case WIFI_AUTH_WPA3_PSK:        Serial.print("WPA3-PSK        "); break;
        default:                        Serial.print("DESCONOCIDA     "); break;
      }

      Serial.println(WiFi.SSID(i));
    }
  }

  WiFi.scanDelete(); // libera la memoria del resultado anterior
  Serial.println();
  delay(6000);
}
