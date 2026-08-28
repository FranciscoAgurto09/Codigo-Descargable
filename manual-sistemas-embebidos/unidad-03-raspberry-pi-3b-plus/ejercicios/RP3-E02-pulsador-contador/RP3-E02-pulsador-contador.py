#!/usr/bin/env python3
"""
RP3-E02 - Pulsador y contador con persistencia
Placa: Raspberry Pi 3 Model B+
Biblioteca: gpiozero

Objetivo: contar pulsaciones y guardar el conteo en un archivo, de modo que
sobreviva a un reinicio del script (aunque no a un reinicio de la placa sin
un mecanismo adicional).

Requiere el pulsador de RP3-P02 (GPIO27).
"""
import json
import os

from gpiozero import Button
from signal import pause

PIN_BOTON = 27
ARCHIVO_CONTADOR = "contador_rp3_e02.json"


def cargar_contador() -> int:
    if os.path.exists(ARCHIVO_CONTADOR):
        with open(ARCHIVO_CONTADOR, "r", encoding="utf-8") as f:
            return json.load(f).get("contador", 0)
    return 0


def guardar_contador(valor: int) -> None:
    with open(ARCHIVO_CONTADOR, "w", encoding="utf-8") as f:
        json.dump({"contador": valor}, f)


def main():
    contador = cargar_contador()
    print(f"RP3-E02 iniciado. Contador cargado: {contador}")

    boton = Button(PIN_BOTON, pull_up=True, bounce_time=0.05)

    def al_presionar():
        nonlocal contador
        contador += 1
        guardar_contador(contador)
        print(f"Pulsacion registrada. Total: {contador}")

    boton.when_pressed = al_presionar

    try:
        pause()
    except KeyboardInterrupt:
        print(f"\nDetenido por el usuario. Contador final: {contador}")
    finally:
        boton.close()


if __name__ == "__main__":
    main()
