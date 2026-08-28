"""
U4-E05 - Termometro con el sensor interno del RP2040
Placa: Raspberry Pi Pico (RP2040) - MicroPython
Nivel: intermedio

Objetivo: convertir una lectura del conversor analogico-digital en una
magnitud fisica, usando el sensor de temperatura que el RP2040 trae
incorporado. No requiere ningun componente externo.

El sensor esta conectado al canal 4 del conversor, que no sale al conector.
La formula proviene de la hoja de datos del RP2040:

    T = 27 - (V - 0,706) / 0,001721      con V en volt

Advertencia: el sensor mide la temperatura del propio chip, no la del aire.
Sirve para estudiar la conversion, no como instrumento de precision.
"""
from machine import ADC
import time

sensor = ADC(4)
CONVERSION = 3.3 / 65535


def leer_temperatura():
    tension = sensor.read_u16() * CONVERSION
    return 27 - (tension - 0.706) / 0.001721


def main():
    print("U4-E05 iniciada: temperatura interna del RP2040")
    try:
        while True:
            t = leer_temperatura()
            print("Temperatura del chip: {:.2f} grados C".format(t))
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")


main()
