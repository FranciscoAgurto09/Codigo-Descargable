#!/usr/bin/env python3
"""
RP3-E01 - LED controlado por tiempo
Placa: Raspberry Pi 3 Model B+
Biblioteca: gpiozero

Objetivo: comparar dos formas de temporizar un LED en Python:
  1) un bucle bloqueante con time.sleep()
  2) un temporizador no bloqueante con threading.Timer

Requiere el montaje de RP3-P01 (LED en GPIO17).
"""
import threading
import time

from gpiozero import LED

PIN_LED = 17
led = LED(PIN_LED)


def version_bloqueante(segundos_total=6, intervalo=1.0):
    print("Version bloqueante (time.sleep):")
    fin = time.time() + segundos_total
    while time.time() < fin:
        led.toggle()
        print(f"  LED -> {'ON' if led.is_lit else 'OFF'}")
        time.sleep(intervalo)
    led.off()


def version_no_bloqueante(segundos_total=6, intervalo=1.0):
    print("Version no bloqueante (threading.Timer):")
    fin = time.time() + segundos_total

    def parpadear():
        if time.time() >= fin:
            led.off()
            return
        led.toggle()
        print(f"  LED -> {'ON' if led.is_lit else 'OFF'}  (el programa principal sigue libre)")
        threading.Timer(intervalo, parpadear).start()

    parpadear()
    # Mientras el temporizador corre en segundo plano, el hilo principal
    # puede seguir haciendo otras cosas; aqui solo esperamos para demostrarlo.
    time.sleep(segundos_total + 0.5)


if __name__ == "__main__":
    try:
        version_bloqueante()
        time.sleep(1)
        version_no_bloqueante()
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    finally:
        led.off()
        led.close()
