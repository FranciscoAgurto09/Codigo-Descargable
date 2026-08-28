#!/usr/bin/env python3
"""
RP3-P05 - Servidor web para controlar GPIO17
Placa: Raspberry Pi 3 Model B+ (Raspberry Pi OS)
Bibliotecas: Flask + gpiozero

Objetivo: publicar una interfaz web simple (encender/apagar) para el LED
de la practica RP3-P01, mostrando el estado actual.

ADVERTENCIA: este servidor no tiene autenticacion. Usar solo en una red de
laboratorio confiable, nunca expuesto directamente a internet.

Instalacion:
    pip install flask gpiozero --break-system-packages

Ejecucion:
    python3 app.py
    Luego, desde otro dispositivo en la MISMA red:
        http://<ip_de_la_raspberry>:5000
    (la IP se obtiene en la Raspberry Pi con:  hostname -I)
"""
from flask import Flask, redirect, url_for
from gpiozero import LED

PIN_LED = 17  # GPIO17 = pin fisico 11

app = Flask(__name__)
led = LED(PIN_LED)

PAGINA_HTML = """
<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><title>RP3-P05</title></head>
<body style="font-family: sans-serif; text-align:center; margin-top:40px;">
  <h2>Control de LED - Raspberry Pi 3 Model B+</h2>
  <p>Estado actual: <b>{estado}</b></p>
  <p>
    <a href="/encender"><button style="font-size:20px;padding:10px;">Encender</button></a>
    <a href="/apagar"><button style="font-size:20px;padding:10px;">Apagar</button></a>
  </p>
</body>
</html>
"""


@app.route("/")
def raiz():
    estado = "ENCENDIDO" if led.is_lit else "APAGADO"
    return PAGINA_HTML.format(estado=estado)


@app.route("/encender")
def encender():
    led.on()
    print("LED encendido desde la pagina web")
    return redirect(url_for("raiz"))


@app.route("/apagar")
def apagar():
    led.off()
    print("LED apagado desde la pagina web")
    return redirect(url_for("raiz"))


if __name__ == "__main__":
    print(f"RP3-P05 iniciada: control web de GPIO{PIN_LED}")
    # host=0.0.0.0 permite conexiones desde otros dispositivos de la red,
    # no solo desde la propia Raspberry Pi.
    app.run(host="0.0.0.0", port=5000)
