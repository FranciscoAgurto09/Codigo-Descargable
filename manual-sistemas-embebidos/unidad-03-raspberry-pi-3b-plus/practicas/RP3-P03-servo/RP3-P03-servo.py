#!/usr/bin/env python3
"""
RP3-P03 - Servomotor SG90 en GPIO18
Placa: Raspberry Pi 3 Model B+ (Raspberry Pi OS)
Biblioteca: gpiozero

Objetivo: controlar la posicion de un servomotor SG90 mediante PWM generado
desde GPIO18 (pin fisico 12), alimentandolo desde una fuente externa de 5V
con tierra comun (NUNCA desde el pin de 3.3V ni desde un GPIO).

Ejecucion:
    python3 RP3-P03-servo.py
"""
from gpiozero import AngularServo
from time import sleep

PIN_SERVO = 18       # GPIO18 = pin fisico 12
ANGULO_MINIMO = -80  # gpiozero AngularServo usa un rango simetrico
ANGULO_MAXIMO = 80
PASO = 4
PAUSA_S = 0.03


def main():
    # min_pulse_width y max_pulse_width son valores tipicos de partida para
    # un SG90; deben ajustarse si el servo zumba o alcanza un tope mecanico.
    servo = AngularServo(
        PIN_SERVO,
        min_angle=ANGULO_MINIMO,
        max_angle=ANGULO_MAXIMO,
        min_pulse_width=0.0005,
        max_pulse_width=0.0024,
    )

    print(f"RP3-P03 iniciada: servo en GPIO{PIN_SERVO}")
    servo.angle = 0
    sleep(1)

    try:
        while True:
            print("Barrido ascendente")
            for angulo in range(ANGULO_MINIMO, ANGULO_MAXIMO + 1, PASO):
                servo.angle = angulo
                sleep(PAUSA_S)
            sleep(0.4)

            print("Barrido descendente")
            for angulo in range(ANGULO_MAXIMO, ANGULO_MINIMO - 1, -PASO):
                servo.angle = angulo
                sleep(PAUSA_S)
            sleep(0.4)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        servo.detach()  # deja de enviar pulsos; el servo queda libre
        servo.close()


if __name__ == "__main__":
    main()
