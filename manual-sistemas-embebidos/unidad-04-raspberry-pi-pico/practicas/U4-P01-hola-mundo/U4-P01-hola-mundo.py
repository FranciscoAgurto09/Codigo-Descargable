"""
U4-P01 - Hola mundo por consola
Placa: Raspberry Pi Pico (RP2040)
Firmware: MicroPython

Objetivo: comprobar que la placa, el cable, el firmware y el entorno
funcionan, y aprender a leer mensajes enviados desde el microcontrolador.
Es la practica que debe repetirse siempre que algo falle, para descartar
problemas de instalacion.

Materiales: solo la Pico y su cable micro-USB. No se conecta nada mas.

Ejecucion:
    Abrir el archivo en Thonny, seleccionar el interprete
    "MicroPython (Raspberry Pi Pico)" y pulsar Run.
    Detener con el boton de parada o con Ctrl+C en la consola.
"""
from machine import Pin
import time

PIN_LED = 25          # LED integrado de la Pico (NO existe en la Pico W)
INTERVALO_S = 1.0

led = Pin(PIN_LED, Pin.OUT)


def main():
    print("U4-P01 iniciada: hola mundo desde la Raspberry Pi Pico")
    print("Cada segundo se imprime un contador y parpadea el LED integrado.")
    contador = 0
    try:
        while True:
            contador += 1
            led.toggle()
            print("Contador:", contador, "| LED:", "ON" if led.value() else "OFF")
            time.sleep(INTERVALO_S)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        # Dejar la placa en un estado conocido.
        led.value(0)


main()
