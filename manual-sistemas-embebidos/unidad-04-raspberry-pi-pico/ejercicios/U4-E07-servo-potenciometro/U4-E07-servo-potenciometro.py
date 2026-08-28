"""
U4-E07 - Servo comandado por potenciometro
Placa: Raspberry Pi Pico (RP2040) - MicroPython
Nivel: intermedio

Objetivo: control proporcional de un actuador. La posicion del
potenciometro se traduce directamente en el angulo del servo.

Montaje:
    Potenciometro de 10 kohm entre 3V3 y GND, cursor -> GP26 (ADC0)
    Servo SG90: senal -> GP16, alimentacion 5 V desde FUENTE EXTERNA,
    y tierra de esa fuente unida a la tierra de la Pico.

Se reutiliza el calculo de ancho de pulso de la practica U4-P03.
"""
from machine import Pin, PWM, ADC
import time

potenciometro = ADC(26)
servo = PWM(Pin(16))
servo.freq(50)

PULSO_MIN_MS = 0.5
PULSO_MAX_MS = 2.5
PERIODO_MS = 20.0


def angulo_a_duty(angulo):
    ancho_ms = PULSO_MIN_MS + (PULSO_MAX_MS - PULSO_MIN_MS) * angulo / 180.0
    return int(ancho_ms / PERIODO_MS * 65535)


def main():
    print("U4-E07 iniciada: el potenciometro comanda el angulo del servo")
    angulo_anterior = -1
    try:
        while True:
            lectura = potenciometro.read_u16()
            angulo = lectura * 180 // 65535
            # Solo se mueve si el cambio es apreciable: evita el temblor
            # producido por el ruido de la medicion.
            if abs(angulo - angulo_anterior) >= 2:
                servo.duty_u16(angulo_a_duty(angulo))
                print("Angulo:", angulo, "grados")
                angulo_anterior = angulo
            time.sleep_ms(50)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        servo.deinit()


main()
