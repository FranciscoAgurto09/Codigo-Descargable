#!/usr/bin/env python3
"""
RP3-E04 - Servo controlado por entrada de teclado
Placa: Raspberry Pi 3 Model B+
Biblioteca: gpiozero

Objetivo: leer un angulo objetivo desde la entrada estandar (input()) y
mover el servo a ese angulo, validando que este dentro del rango permitido
antes de aplicarlo.

Requiere el montaje de RP3-P03 (servo en GPIO18, fuente externa de 5V,
GND comun).
"""
from gpiozero import AngularServo

PIN_SERVO = 18
ANGULO_MINIMO = -80
ANGULO_MAXIMO = 80


def main():
    servo = AngularServo(
        PIN_SERVO,
        min_angle=ANGULO_MINIMO,
        max_angle=ANGULO_MAXIMO,
        min_pulse_width=0.0005,
        max_pulse_width=0.0024,
    )
    servo.angle = 0
    print(f"RP3-E04 iniciado. Rango valido: [{ANGULO_MINIMO}, {ANGULO_MAXIMO}] grados.")
    print("Escribe un angulo y presiona Enter (o 'salir' para terminar).")

    try:
        while True:
            entrada = input("Angulo> ").strip()
            if entrada.lower() in ("salir", "exit", "q"):
                break
            try:
                angulo = float(entrada)
            except ValueError:
                print("  Entrada invalida: escribe un numero.")
                continue

            if not (ANGULO_MINIMO <= angulo <= ANGULO_MAXIMO):
                print(f"  Fuera de rango. Debe estar entre {ANGULO_MINIMO} y {ANGULO_MAXIMO}.")
                continue

            servo.angle = angulo
            print(f"  Servo movido a {angulo} grados.")
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        servo.detach()
        servo.close()


if __name__ == "__main__":
    main()
