#!/usr/bin/env python3
"""
RP3-E03 - Control PWM con PWMLED (efecto de atenuacion)
Placa: Raspberry Pi 3 Model B+
Biblioteca: gpiozero

Objetivo: generar PWM con PWMLED y variar el ciclo de trabajo para producir
un efecto de brillo creciente/decreciente ("respiracion"), analogo al
ejercicio U2-E03 de la Unidad 2 (LEDC en el ESP32).

Requiere un LED con su resistencia en GPIO17 (igual montaje que RP3-P01).
"""
import time

from gpiozero import PWMLED

PIN_LED = 17
PASO = 0.02      # incremento del ciclo de trabajo (0.0 a 1.0)
PAUSA_S = 0.02


def main():
    led = PWMLED(PIN_LED)
    print(f"RP3-E03 iniciado: PWM en GPIO{PIN_LED}")

    try:
        while True:
            valor = 0.0
            while valor < 1.0:
                led.value = valor
                valor += PASO
                time.sleep(PAUSA_S)
            valor = 1.0
            while valor > 0.0:
                led.value = valor
                valor -= PASO
                time.sleep(PAUSA_S)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        led.off()
        led.close()


if __name__ == "__main__":
    main()
