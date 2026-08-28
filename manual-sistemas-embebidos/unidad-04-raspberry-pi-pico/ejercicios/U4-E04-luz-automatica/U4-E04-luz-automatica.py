"""
U4-E04 - Luz automatica con fotorresistencia
Placa: Raspberry Pi Pico (RP2040) - MicroPython
Nivel: intermedio

Objetivo: armar un divisor de tension con una LDR y tomar una decision por
umbral, con histeresis para que la salida no oscile en el limite.

Montaje (divisor de tension):
    3V3 -> LDR -> nodo -> resistencia de 10 kohm -> GND
    nodo -> GP27 (ADC1)
    LED con resistencia de 220 ohm -> GP15, catodo a GND

Con este orden, mas luz sobre la LDR significa una lectura mas alta.
Los umbrales dependen de la LDR y de la iluminacion de la sala: conviene
imprimir las lecturas y ajustarlos antes de usarlos.
"""
from machine import Pin, ADC
import time

ldr = ADC(27)
led = Pin(15, Pin.OUT)

UMBRAL_ENCENDER = 18000     # por debajo de esto esta oscuro
UMBRAL_APAGAR = 26000       # por encima de esto esta claro
encendida = False


def main():
    global encendida
    print("U4-E04 iniciada: la luz se enciende sola al oscurecer")
    try:
        while True:
            lectura = ldr.read_u16()
            if not encendida and lectura < UMBRAL_ENCENDER:
                encendida = True
                led.value(1)
                print("Oscuro -> luz ENCENDIDA")
            elif encendida and lectura > UMBRAL_APAGAR:
                encendida = False
                led.value(0)
                print("Claro  -> luz APAGADA")
            print("Lectura:", lectura)
            time.sleep_ms(500)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        led.value(0)


main()
