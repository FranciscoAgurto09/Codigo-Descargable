"""
U4-E03 - Atenuador de LED con potenciometro
Placa: Raspberry Pi Pico (RP2040) - MicroPython
Nivel: intermedio

Objetivo: leer una entrada analogica, convertir el rango de valores y
gobernar con el una salida PWM.

Montaje:
    Potenciometro de 10 kohm: extremo 1 -> 3V3, extremo 2 -> GND,
    cursor (terminal central) -> GP26 (ADC0)
    LED con resistencia de 220 ohm -> GP15, catodo a GND

OJO: el potenciometro se alimenta desde 3V3, NUNCA desde 5 V: la Pico no
tolera 5 V en sus entradas.
"""
from machine import Pin, PWM, ADC
import time

potenciometro = ADC(26)
led = PWM(Pin(15))
led.freq(1000)          # 1 kHz: muy por encima de lo que percibe el ojo


def main():
    print("U4-E03 iniciada: girar el potenciometro para variar el brillo")
    try:
        while True:
            # read_u16() entrega 0..65535, escalado desde una medicion
            # real de 12 bits (0..4095).
            lectura = potenciometro.read_u16()
            led.duty_u16(lectura)
            porcentaje = lectura * 100 // 65535
            print("Lectura:", lectura, "| Brillo:", porcentaje, "%")
            time.sleep_ms(200)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        led.duty_u16(0)
        led.deinit()


main()
