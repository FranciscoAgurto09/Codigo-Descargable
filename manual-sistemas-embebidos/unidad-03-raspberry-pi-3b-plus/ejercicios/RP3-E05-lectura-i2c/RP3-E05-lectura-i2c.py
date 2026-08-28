#!/usr/bin/env python3
"""
RP3-E05 - Lectura I2C con manejo de errores
Placa: Raspberry Pi 3 Model B+, bus I2C1 habilitado
Biblioteca: smbus2

Objetivo: reutilizar el sensor BH1750 de RP3-P04, pero con manejo explicito
de errores de bus (sensor desconectado, direccion incorrecta), sin que el
programa se caiga por una lectura fallida aislada.
"""
import time

from smbus2 import SMBus

BUS_I2C = 1
DIRECCION_BH1750 = 0x23
CMD_POWER_ON = 0x01
CMD_MODO_ALTA_RESOLUCION_CONTINUA = 0x10


def leer_lux_seguro(bus: SMBus) -> float | None:
    try:
        datos = bus.read_i2c_block_data(DIRECCION_BH1750, CMD_MODO_ALTA_RESOLUCION_CONTINUA, 2)
        valor_crudo = (datos[0] << 8) | datos[1]
        return valor_crudo / 1.2
    except OSError as error:
        print(f"  Error de bus I2C (sensor desconectado o direccion incorrecta): {error}")
        return None


def main():
    print(f"RP3-E05 iniciado: lectura robusta del BH1750 en 0x{DIRECCION_BH1750:02X}")
    lecturas_fallidas_seguidas = 0

    with SMBus(BUS_I2C) as bus:
        try:
            bus.write_byte(DIRECCION_BH1750, CMD_POWER_ON)
        except OSError as error:
            print(f"No se pudo inicializar el sensor: {error}")
            return

        try:
            while True:
                lux = leer_lux_seguro(bus)
                if lux is None:
                    lecturas_fallidas_seguidas += 1
                    if lecturas_fallidas_seguidas >= 5:
                        print("  Demasiadas lecturas fallidas seguidas. Verificar cableado.")
                else:
                    lecturas_fallidas_seguidas = 0
                    print(f"Iluminancia: {lux:.1f} lx")
                time.sleep(1.0)
        except KeyboardInterrupt:
            print("\nDetenido por el usuario.")


if __name__ == "__main__":
    main()
