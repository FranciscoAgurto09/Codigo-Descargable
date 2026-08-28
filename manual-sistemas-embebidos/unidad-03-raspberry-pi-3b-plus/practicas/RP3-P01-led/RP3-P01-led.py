#!/usr/bin/env python3
"""
RP3-P01 - LED externo en GPIO17
Placa: Raspberry Pi 3 Model B+ (Raspberry Pi OS)
Biblioteca: gpiozero

Objetivo: comprender GPIO + nivel logico + resistencia + LED + GND + Python,
encendiendo y apagando un LED externo conectado a GPIO17 (pin fisico 11).

Instalacion (normalmente ya viene preinstalado en Raspberry Pi OS):
    pip install gpiozero --break-system-packages

Ejecucion:
    python3 RP3-P01-led.py
    (Ctrl+C para detener)
"""
from gpiozero import LED
from time import sleep
from signal import pause

PIN_LED = 17          # GPIO17 = pin fisico 11. OJO: no es el numero de pin fisico.
INTERVALO_S = 1.0


def main():
    led = LED(PIN_LED)
    print(f"RP3-P01 iniciada: LED externo en GPIO{PIN_LED}")
    try:
        while True:
            led.on()
            print("LED ENCENDIDO")
            sleep(INTERVALO_S)
            led.off()
            print("LED APAGADO")
            sleep(INTERVALO_S)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        # gpiozero libera el GPIO automaticamente al salir del programa,
        # pero apagamos el LED explicitamente para dejar un estado conocido.
        led.off()
        led.close()


if __name__ == "__main__":
    main()
