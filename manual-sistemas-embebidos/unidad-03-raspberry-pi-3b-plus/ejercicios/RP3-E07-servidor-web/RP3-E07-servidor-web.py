#!/usr/bin/env python3
"""
RP3-E07 - Servidor web ampliado (formulario de intervalo de parpadeo)
Placa: Raspberry Pi 3 Model B+
Bibliotecas: Flask, gpiozero

Objetivo: ampliar RP3-P05 con una tercera ruta que recibe, desde un
formulario HTML, un intervalo de parpadeo y lo aplica al LED durante un
numero limitado de ciclos, sin bloquear el servidor web (se ejecuta en un
hilo aparte).

ADVERTENCIA: sin autenticacion; solo para red de laboratorio confiable.
"""
import threading
import time

from flask import Flask, redirect, request, url_for
from gpiozero import LED

PIN_LED = 17
CICLOS_PARPADEO = 6

app = Flask(__name__)
led = LED(PIN_LED)
parpadeando = False

PAGINA_HTML = """
<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><title>RP3-E07</title></head>
<body style="font-family: sans-serif; text-align:center; margin-top:40px;">
  <h2>Control ampliado de LED - Raspberry Pi 3 Model B+</h2>
  <p>Estado actual: <b>{estado}</b></p>
  <p>
    <a href="/encender"><button style="font-size:18px;padding:8px;">Encender</button></a>
    <a href="/apagar"><button style="font-size:18px;padding:8px;">Apagar</button></a>
  </p>
  <form action="/parpadear" method="post">
    <label>Intervalo de parpadeo (segundos): </label>
    <input type="number" step="0.1" min="0.1" name="intervalo" value="0.5">
    <button type="submit" style="font-size:16px;padding:6px;">Parpadear</button>
  </form>
</body>
</html>
"""


def parpadear_en_hilo(intervalo: float):
    global parpadeando
    parpadeando = True
    for _ in range(CICLOS_PARPADEO):
        led.toggle()
        time.sleep(intervalo)
    led.off()
    parpadeando = False


@app.route("/")
def raiz():
    estado = "PARPADEANDO" if parpadeando else ("ENCENDIDO" if led.is_lit else "APAGADO")
    return PAGINA_HTML.format(estado=estado)


@app.route("/encender")
def encender():
    led.on()
    return redirect(url_for("raiz"))


@app.route("/apagar")
def apagar():
    led.off()
    return redirect(url_for("raiz"))


@app.route("/parpadear", methods=["POST"])
def parpadear():
    if not parpadeando:
        try:
            intervalo = float(request.form.get("intervalo", "0.5"))
            intervalo = max(0.1, min(intervalo, 5.0))  # limite razonable
        except ValueError:
            intervalo = 0.5
        hilo = threading.Thread(target=parpadear_en_hilo, args=(intervalo,), daemon=True)
        hilo.start()
    return redirect(url_for("raiz"))


if __name__ == "__main__":
    print(f"RP3-E07 iniciado: control web ampliado de GPIO{PIN_LED}")
    app.run(host="0.0.0.0", port=5000)
