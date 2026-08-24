/*
  U2-E07 - LED controlado desde una pagina web
  Placa: ESP32 DevKit V1 de 30 pines
  Monitor serie: 115200 bit/s

  Objetivo: levantar un punto de acceso Wi-Fi propio (modo AP) y un
  servidor web simple con dos botones HTML para encender y apagar un
  LED, sin depender de una red externa.

  IMPORTANTE: reemplazar CLAVE_AP por una contrasena propia de al menos
  8 caracteres antes de usar este ejercicio fuera del laboratorio; una
  red abierta o con clave por defecto expone el control del LED a
  cualquiera que este dentro del alcance de la senal.

  Requiere el nucleo Arduino-ESP32 (incluye WiFi.h y WebServer.h).
*/
#include <WiFi.h>
#include <WebServer.h>

const char* NOMBRE_AP = "ESP32-U2E07";
const char* CLAVE_AP  = "cambia-esta-clave"; // minimo 8 caracteres

const uint8_t PIN_LED = 32; // GPIO32, salida digital segura

WebServer servidor(80);
bool estadoLed = false;

const char PAGINA_HTML[] PROGMEM = R"rawliteral(
<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><title>U2-E07</title></head>
<body style="font-family: sans-serif; text-align:center; margin-top:40px;">
  <h2>Control de LED - ESP32 DevKit V1</h2>
  <p>Estado actual: <b>%ESTADO%</b></p>
  <p>
    <a href="/encender"><button style="font-size:20px;padding:10px;">Encender</button></a>
    <a href="/apagar"><button style="font-size:20px;padding:10px;">Apagar</button></a>
  </p>
</body>
</html>
)rawliteral";

String construirPagina() {
  String html = PAGINA_HTML;
  html.replace("%ESTADO%", estadoLed ? "ENCENDIDO" : "APAGADO");
  return html;
}

void manejarRaiz() {
  servidor.send(200, "text/html", construirPagina());
}

void manejarEncender() {
  estadoLed = true;
  digitalWrite(PIN_LED, HIGH);
  Serial.println("LED encendido desde la pagina web");
  servidor.sendHeader("Location", "/");
  servidor.send(303);
}

void manejarApagar() {
  estadoLed = false;
  digitalWrite(PIN_LED, LOW);
  Serial.println("LED apagado desde la pagina web");
  servidor.sendHeader("Location", "/");
  servidor.send(303);
}

void setup() {
  Serial.begin(115200);
  pinMode(PIN_LED, OUTPUT);
  digitalWrite(PIN_LED, LOW);
  delay(300);

  WiFi.mode(WIFI_AP);
  WiFi.softAP(NOMBRE_AP, CLAVE_AP);

  Serial.println("U2-E07 iniciado: LED desde pagina web");
  Serial.print("Conectate a la red: ");
  Serial.println(NOMBRE_AP);
  Serial.print("Luego abre en el navegador: http://");
  Serial.println(WiFi.softAPIP());

  servidor.on("/", manejarRaiz);
  servidor.on("/encender", manejarEncender);
  servidor.on("/apagar", manejarApagar);
  servidor.begin();
}

void loop() {
  servidor.handleClient();
}
