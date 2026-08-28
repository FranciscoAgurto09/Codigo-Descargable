#!/usr/bin/env python3
"""
RP3-E10 - Mini sistema IoT (sensor + registro + servidor web)
Placa: Raspberry Pi 3 Model B+, bus I2C1 habilitado
Bibliotecas: Flask, smbus2

Objetivo: integrar en un solo programa lo aprendido en la unidad: lectura
periodica de un sensor I2C (BH1750) en un hilo de fondo, registro en CSV, y
una pagina web que muestra la ultima lectura y un historial simple. Es una
version reducida del proyecto integrador de la Unidad 3.

ADVERTENCIA: sin autenticacion; solo para red de laboratorio confiable.
"""
import csv
import threading
import time
from collections import deque
from datetime import datetime

from flask import Flask
from smbus2 import SMBus

BUS_I2C = 1
DIRECCION_BH1750 = 0x23
CMD_POWER_ON = 0x01
CMD_MODO_ALTA_RESOLUCION_CONTINUA = 0x10
ARCHIVO_CSV = "registro_iot.csv"
INTERVALO_LECTURA_S = 10
HISTORIAL_MAXIMO = 20

app = Flask(__name__)
historial = deque(maxlen=HISTORIAL_MAXIMO)
bloqueo_historial = threading.Lock()


def leer_lux(bus: SMBus) -> float:
    datos = bus.read_i2c_block_data(DIRECCION_BH1750, CMD_MODO_ALTA_RESOLUCION_CONTINUA, 2)
    valor_crudo = (datos[0] << 8) | datos[1]
    return valor_crudo / 1.2


def hilo_sensor():
    """Corre en segundo plano: lee el sensor y registra, sin bloquear el servidor web."""
    with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as csv_file:
        escritor = csv.writer(csv_file)
        if csv_file.tell() == 0:
            escritor.writerow(["marca_tiempo", "lux"])

        with SMBus(BUS_I2C) as bus:
            try:
                bus.write_byte(DIRECCION_BH1750, CMD_POWER_ON)
            except OSError as error:
                print(f"No se pudo inicializar el sensor: {error}")
                return

            while True:
                try:
                    lux = leer_lux(bus)
                    marca = datetime.now().isoformat(timespec="seconds")
                    with bloqueo_historial:
                        historial.append((marca, lux))
                    escritor.writerow([marca, f"{lux:.1f}"])
                    csv_file.flush()
                except OSError as error:
                    print(f"Lectura fallida, se omite este ciclo: {error}")
                time.sleep(INTERVALO_LECTURA_S)


@app.route("/")
def raiz():
    with bloqueo_historial:
        datos = list(historial)

    if datos:
        ultima_marca, ultimo_lux = datos[-1]
        estado_actual = f"{ultimo_lux:.1f} lx (a las {ultima_marca})"
    else:
        estado_actual = "sin lecturas todavia"

    filas_html = "".join(
        f"<tr><td>{marca}</td><td>{lux:.1f} lx</td></tr>" for marca, lux in reversed(datos)
    )

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="UTF-8"><title>RP3-E10</title></head>
    <body style="font-family: sans-serif; text-align:center; margin-top:30px;">
      <h2>Mini sistema IoT - Raspberry Pi 3 Model B+</h2>
      <p>Ultima lectura: <b>{estado_actual}</b></p>
      <table style="margin:auto; border-collapse:collapse;" border="1" cellpadding="6">
        <tr><th>Marca de tiempo</th><th>Iluminancia</th></tr>
        {filas_html}
      </table>
    </body>
    </html>
    """


if __name__ == "__main__":
    print("RP3-E10 iniciado: sensor en segundo plano + servidor web en :5000")
    hilo = threading.Thread(target=hilo_sensor, daemon=True)
    hilo.start()
    app.run(host="0.0.0.0", port=5000)
