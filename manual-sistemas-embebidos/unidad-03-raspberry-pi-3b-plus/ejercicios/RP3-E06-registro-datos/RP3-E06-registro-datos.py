#!/usr/bin/env python3
"""
RP3-E06 - Registro periodico de datos en CSV
Placa: Raspberry Pi 3 Model B+, bus I2C1 habilitado
Biblioteca: smbus2

Objetivo: leer el sensor BH1750 una vez por minuto y registrar cada lectura
en un archivo CSV con marca de tiempo, sentando la base de un sistema de
monitoreo (ver proyecto integrador de la Unidad 3).
"""
import csv
import time
from datetime import datetime

from smbus2 import SMBus

BUS_I2C = 1
DIRECCION_BH1750 = 0x23
CMD_POWER_ON = 0x01
CMD_MODO_ALTA_RESOLUCION_CONTINUA = 0x10
ARCHIVO_CSV = "registro_luz.csv"
INTERVALO_S = 60  # una lectura por minuto


def leer_lux(bus: SMBus) -> float:
    datos = bus.read_i2c_block_data(DIRECCION_BH1750, CMD_MODO_ALTA_RESOLUCION_CONTINUA, 2)
    valor_crudo = (datos[0] << 8) | datos[1]
    return valor_crudo / 1.2


def main():
    print(f"RP3-E06 iniciado: registrando en {ARCHIVO_CSV} cada {INTERVALO_S} s")

    with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as csv_file, \
         SMBus(BUS_I2C) as bus:

        escritor = csv.writer(csv_file)
        if csv_file.tell() == 0:
            escritor.writerow(["marca_tiempo", "lux"])

        bus.write_byte(DIRECCION_BH1750, CMD_POWER_ON)

        try:
            while True:
                try:
                    lux = leer_lux(bus)
                    marca = datetime.now().isoformat(timespec="seconds")
                    escritor.writerow([marca, f"{lux:.1f}"])
                    csv_file.flush()
                    print(f"[{marca}] {lux:.1f} lx registrados")
                except OSError as error:
                    print(f"  Lectura fallida, se omite este ciclo: {error}")

                time.sleep(INTERVALO_S)
        except KeyboardInterrupt:
            print("\nDetenido por el usuario.")


if __name__ == "__main__":
    main()
