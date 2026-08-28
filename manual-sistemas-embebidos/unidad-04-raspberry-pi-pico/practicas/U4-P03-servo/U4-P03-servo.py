"""
U4-P03 - Mover un servomotor SG90 en GP16
Placa: Raspberry Pi Pico (RP2040)
Firmware: MicroPython

Objetivo: comandar un actuador con posicion controlada, generar una senal
PWM de frecuencia y ancho definidos, y reconocer la necesidad de
alimentacion independiente.

Montaje:
    Cable de senal (naranjo/amarillo) -> GP16 (posicion fisica 21)
    Cable rojo                        -> 5 V de una FUENTE EXTERNA
    Cable cafe/negro                  -> GND de la fuente externa
    GND de la fuente externa          -> GND de la Pico   <-- OBLIGATORIO

NUNCA alimentar el servo desde el pin 3V3 de la placa: en vacio consume
unos 150 mA y con carga supera con facilidad los 500 mA.

Como se calcula el ciclo de trabajo:
    A 50 Hz el periodo es de 20 ms. El servo interpreta el ancho del pulso,
    aproximadamente entre 0,5 ms (0 grados) y 2,5 ms (180 grados).
    duty_u16 = (ancho_ms / 20 ms) * 65535

Ejecucion: abrir en Thonny y pulsar Run. Detener con Ctrl+C.
"""
from machine import Pin, PWM
import time

PIN_SERVO = 16
FRECUENCIA_HZ = 50
PULSO_MIN_MS = 0.5        # aproximadamente 0 grados
PULSO_MAX_MS = 2.5        # aproximadamente 180 grados
PERIODO_MS = 1000.0 / FRECUENCIA_HZ    # 20 ms

servo = PWM(Pin(PIN_SERVO))
servo.freq(FRECUENCIA_HZ)


def angulo_a_duty(angulo):
    """Convierte un angulo de 0 a 180 grados en un valor de duty_u16."""
    if angulo < 0:
        angulo = 0
    elif angulo > 180:
        angulo = 180
    ancho_ms = PULSO_MIN_MS + (PULSO_MAX_MS - PULSO_MIN_MS) * angulo / 180.0
    return int(ancho_ms / PERIODO_MS * 65535)


def mover(angulo, espera_s=1.0):
    servo.duty_u16(angulo_a_duty(angulo))
    print("Posicion ordenada:", angulo, "grados")
    time.sleep(espera_s)


def main():
    print("U4-P03 iniciada: servo SG90 en GP{}".format(PIN_SERVO))
    print("Recuerde: alimentacion externa de 5 V y tierra comun con la Pico.")
    try:
        while True:
            mover(0)
            mover(90)
            mover(180)
            mover(90)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        # Liberar el pin: si se deja la senal activa el servo sigue
        # forzando contra su tope y zumba.
        servo.deinit()


main()
