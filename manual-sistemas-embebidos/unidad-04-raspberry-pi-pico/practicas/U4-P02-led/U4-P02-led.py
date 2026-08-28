"""
U4-P02 - Encender un LED externo en GP15
Placa: Raspberry Pi Pico (RP2040)
Firmware: MicroPython

Objetivo: controlar una salida digital, comprender el uso de la resistencia
limitadora y comprobar la diferencia entre trabajar a 3,3 V y a 5 V.

Montaje:
    GP15 (posicion fisica 20) -> resistencia de 220 ohm -> anodo del LED
    catodo del LED            -> GND (posicion fisica 18)

OJO: el numero que se escribe aqui es el nombre logico GP15, no la
posicion fisica 15 (que corresponde a GP11).

Ejecucion: abrir en Thonny y pulsar Run. Detener con Ctrl+C.
"""
from machine import Pin
import time

PIN_LED = 15
INTERVALO_S = 0.5

led = Pin(PIN_LED, Pin.OUT)


def main():
    print("U4-P02 iniciada: LED externo en GP{}".format(PIN_LED))
    try:
        while True:
            led.value(1)
            print("LED ENCENDIDO")
            time.sleep(INTERVALO_S)
            led.value(0)
            print("LED APAGADO")
            time.sleep(INTERVALO_S)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        led.value(0)


main()
