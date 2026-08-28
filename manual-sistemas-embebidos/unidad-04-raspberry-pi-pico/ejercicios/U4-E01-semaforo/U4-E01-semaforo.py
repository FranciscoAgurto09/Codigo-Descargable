"""
U4-E01 - Semaforo de tres LED
Placa: Raspberry Pi Pico (RP2040) - MicroPython
Nivel: basico

Objetivo: practicar secuencias temporizadas y el orden de ejecucion.

Montaje: tres LED con resistencia de 220 ohm cada uno.
    GP13 -> LED rojo        GP14 -> LED amarillo      GP15 -> LED verde
    Los tres catodos van a GND.
"""
from machine import Pin
import time

rojo = Pin(13, Pin.OUT)
amarillo = Pin(14, Pin.OUT)
verde = Pin(15, Pin.OUT)

FASES = (
    # (rojo, amarillo, verde, duracion en segundos, nombre)
    (1, 0, 0, 4.0, "ROJO: detencion"),
    (1, 1, 0, 1.0, "ROJO+AMARILLO: prepararse"),
    (0, 0, 1, 4.0, "VERDE: paso permitido"),
    (0, 1, 0, 1.5, "AMARILLO: precaucion"),
)


def apagar_todo():
    rojo.value(0)
    amarillo.value(0)
    verde.value(0)


def main():
    print("U4-E01 iniciada: semaforo de tres LED")
    try:
        while True:
            for r, a, v, duracion, nombre in FASES:
                rojo.value(r)
                amarillo.value(a)
                verde.value(v)
                print(nombre)
                time.sleep(duracion)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        apagar_todo()


main()
