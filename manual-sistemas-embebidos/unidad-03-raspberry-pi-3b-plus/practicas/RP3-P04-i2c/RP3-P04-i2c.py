#!/usr/bin/env python3
"""
RP3-P04 - Sensor I2C de luz ambiental BH1750
Placa: Raspberry Pi 3 Model B+ (Raspberry Pi OS), bus I2C1 habilitado
Biblioteca: smbus2 (acceso directo a registros, sin capa de abstraccion)

Objetivo: activar el bus I2C, leer el sensor BH1750 directamente por sus
registros y convertir el resultado a lux.

Antes de ejecutar:
    1. Habilitar I2C: sudo raspi-config -> Interface Options -> I2C -> Enable
    2. Reiniciar si se pide.
    3. Verificar deteccion: sudo i2cdetect -y 1
       (debe aparecer 0x23 o 0x5C segun el pin ADDR del modulo)

Instalacion:
    sudo apt install -y i2c-tools
    pip install smbus2 --break-system-packages

Ejecucion:
    python3 RP3-P04-i2c.py
"""
import time
from smbus2 import SMBus

BUS_I2C = 1              # bus de usuario del header de 40 pines
DIRECCION_BH1750 = 0x23  # 0x23 con ADDR a GND/flotante; 0x5C con ADDR a VCC

# Comandos del BH1750 (documentados por el fabricante del sensor)
CMD_POWER_ON = 0x01
CMD_RESET = 0x07
CMD_MODO_ALTA_RESOLUCION_CONTINUA = 0x10  # 1 lx de resolucion, ~120 ms


def leer_lux(bus: SMBus) -> float:
    datos = bus.read_i2c_block_data(DIRECCION_BH1750, CMD_MODO_ALTA_RESOLUCION_CONTINUA, 2)
    valor_crudo = (datos[0] << 8) | datos[1]
    # Constante de conversion documentada por el fabricante del BH1750.
    lux = valor_crudo / 1.2
    return lux


def main():
    print(f"RP3-P04 iniciada: sensor BH1750 en direccion 0x{DIRECCION_BH1750:02X}, bus I2C{BUS_I2C}")
    with SMBus(BUS_I2C) as bus:
        bus.write_byte(DIRECCION_BH1750, CMD_POWER_ON)
        time.sleep(0.01)
        bus.write_byte(DIRECCION_BH1750, CMD_RESET)
        time.sleep(0.01)

        try:
            while True:
                lux = leer_lux(bus)
                print(f"Iluminancia: {lux:.1f} lx")
                time.sleep(1.0)
        except KeyboardInterrupt:
            print("\nDetenido por el usuario.")


if __name__ == "__main__":
    main()
