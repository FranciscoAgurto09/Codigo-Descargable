"""
U4-E02 - LED comandado por pulsador
Placa: Raspberry Pi Pico (RP2040) - MicroPython
Nivel: basico

Objetivo: usar una entrada digital con la resistencia interna de
polarizacion y eliminar el rebote mecanico del pulsador.

Montaje:
    Un terminal del pulsador -> GP14      El otro terminal -> GND
    LED con resistencia de 220 ohm -> GP15, catodo a GND

Con PULL_UP la entrada vale 1 en reposo y 0 mientras el pulsador esta
presionado: no hace falta ninguna resistencia externa.
"""
from machine import Pin
import time

pulsador = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

REBOTE_MS = 50
estado_led = 0
ultimo_cambio = time.ticks_ms()
estado_anterior = pulsador.value()


def main():
    global estado_led, ultimo_cambio, estado_anterior
    print("U4-E02 iniciada: cada pulsacion invierte el estado del LED")
    try:
        while True:
            lectura = pulsador.value()
            ahora = time.ticks_ms()
            # Solo se acepta un cambio si paso el tiempo de antirrebote.
            if lectura != estado_anterior and \
                    time.ticks_diff(ahora, ultimo_cambio) > REBOTE_MS:
                ultimo_cambio = ahora
                estado_anterior = lectura
                if lectura == 0:            # flanco de bajada = pulsado
                    estado_led = 1 - estado_led
                    led.value(estado_led)
                    print("LED:", "ON" if estado_led else "OFF")
            time.sleep_ms(5)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        led.value(0)


main()
