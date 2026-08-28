#!/usr/bin/env python3
"""
RP3-P02 - Pulsador con LED de respuesta
Placa: Raspberry Pi 3 Model B+ (Raspberry Pi OS)
Biblioteca: gpiozero

Objetivo: leer una entrada digital con antirrebote (debounce) y pull-up
integrado, encendiendo un LED mientras el pulsador esta presionado.

GPIO27 (pin fisico 13) se configura como entrada con pull-up interno
mediante gpiozero.Button: nunca queda flotante.
GPIO17 (pin fisico 11) se reutiliza como salida para el LED de respuesta.

Ejecucion:
    python3 RP3-P02-pulsador.py
"""
from gpiozero import Button, LED
from signal import pause

PIN_BOTON = 27   # GPIO27 = pin fisico 13
PIN_LED = 17     # GPIO17 = pin fisico 11

contador_pulsaciones = 0


def al_presionar():
    global contador_pulsaciones
    contador_pulsaciones += 1
    led.on()
    print(f"Pulsacion valida numero {contador_pulsaciones}")


def al_soltar():
    led.off()


def main():
    global led
    boton = Button(PIN_BOTON, pull_up=True, bounce_time=0.05)
    led = LED(PIN_LED)

    boton.when_pressed = al_presionar
    boton.when_released = al_soltar

    print(f"RP3-P02 iniciada: pulsador en GPIO{PIN_BOTON}, LED en GPIO{PIN_LED}")
    print("Presiona el pulsador. Ctrl+C para salir.")
    try:
        pause()  # espera eventos indefinidamente, sin consumir CPU en un bucle activo
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        led.off()
        led.close()
        boton.close()


if __name__ == "__main__":
    main()
