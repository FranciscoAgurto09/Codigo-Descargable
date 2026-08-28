#!/usr/bin/env python3
"""
RP3-E08 - SSH y control remoto de un LED
Placa: Raspberry Pi 3 Model B+
Biblioteca: gpiozero

Objetivo: ejecutar y detener, por SSH desde otro equipo, un script que
controla el GPIO. El "ejercicio" en si es el procedimiento de SSH; este
script es deliberadamente simple para que el foco este en el flujo remoto,
no en la logica de GPIO (ya cubierta en RP3-P01).

Procedimiento sugerido (ejecutar desde OTRO computador de la misma red):

    1. Averiguar la IP de la Raspberry Pi (en ella misma): hostname -I
    2. Conectarse por SSH:            ssh usuario@<ip_de_la_raspberry>
    3. Copiar este archivo (si aun no esta) con scp, o clonarlo desde el
       repositorio de codigos de la unidad.
    4. Ejecutarlo en segundo plano, para poder seguir usando la sesion SSH:
           python3 RP3-E08-led-remoto.py &
       o bien, para que siga corriendo tras cerrar la sesion SSH:
           nohup python3 RP3-E08-led-remoto.py &
    5. Verificar que el LED parpadea (mirando la placa fisicamente, o
       pidiendole a alguien presente que lo confirme).
    6. Detenerlo remotamente:
           - Si se ejecuto con "&": traerlo a primer plano con "fg" y
             presionar Ctrl+C, o matarlo con "kill <PID>" (el PID lo
             muestra el propio shell al lanzarlo con "&").
           - Si se ejecuto con "nohup ... &": usar "kill <PID>", buscando
             el PID con "ps aux | grep RP3-E08".
"""
import time

from gpiozero import LED

PIN_LED = 17
INTERVALO_S = 0.5


def main():
    led = LED(PIN_LED)
    print(f"RP3-E08 iniciado (PID visible con 'ps aux | grep RP3-E08'): GPIO{PIN_LED}")
    try:
        while True:
            led.toggle()
            time.sleep(INTERVALO_S)
    except KeyboardInterrupt:
        print("\nDetenido (Ctrl+C o señal recibida).")
    finally:
        led.off()
        led.close()


if __name__ == "__main__":
    main()
