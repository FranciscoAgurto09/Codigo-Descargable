"""
U4-E06 - Barra de nivel con cinco LED
Placa: Raspberry Pi Pico (RP2040) - MicroPython
Nivel: intermedio

Objetivo: practicar listas, ciclos y conversion de rangos: la posicion del
potenciometro decide cuantos LED quedan encendidos.

Montaje:
    Cinco LED, cada uno con su resistencia de 220 ohm, en GP10 a GP14.
    Potenciometro de 10 kohm entre 3V3 y GND, cursor -> GP26 (ADC0).
"""
from machine import Pin, ADC
import time

PINES = (10, 11, 12, 13, 14)
leds = [Pin(numero, Pin.OUT) for numero in PINES]
potenciometro = ADC(26)


def mostrar_nivel(cantidad):
    for indice, led in enumerate(leds):
        led.value(1 if indice < cantidad else 0)


def main():
    print("U4-E06 iniciada: barra de nivel de cinco LED")
    nivel_anterior = -1
    try:
        while True:
            lectura = potenciometro.read_u16()
            # Convierte 0..65535 en 0..5 LED encendidos.
            nivel = lectura * len(leds) // 65536
            if nivel != nivel_anterior:
                mostrar_nivel(nivel)
                print("Lectura:", lectura, "| LED encendidos:", nivel)
                nivel_anterior = nivel
            time.sleep_ms(100)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        mostrar_nivel(0)


main()
