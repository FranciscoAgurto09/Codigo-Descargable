"""
U4-E08 - Registro de mediciones en la memoria flash
Placa: Raspberry Pi Pico (RP2040) - MicroPython
Nivel: avanzado

Objetivo: aprovechar que parte de la flash de 2 MB esta formateada como
sistema de archivos para guardar datos que sobreviven al apagado. Es el
reemplazo natural de la EEPROM del Arduino Uno, que el RP2040 no tiene.

Montaje: ninguno obligatorio. Si se conecta la LDR del ejercicio U4-E04 en
GP27, se registra tambien la luz ambiental.

El archivo datos.csv queda dentro de la placa y puede abrirse despues desde
Thonny, en el panel de archivos de la Raspberry Pi Pico.
"""
from machine import ADC, Pin
import time

ARCHIVO = "datos.csv"
INTERVALO_S = 5
sensor_temp = ADC(4)
ldr = ADC(27)
led = Pin(25, Pin.OUT)
CONVERSION = 3.3 / 65535


def leer_temperatura():
    tension = sensor_temp.read_u16() * CONVERSION
    return 27 - (tension - 0.706) / 0.001721


def crear_encabezado():
    """Escribe el encabezado solo si el archivo aun no existe."""
    try:
        with open(ARCHIVO, "r"):
            return False
    except OSError:
        with open(ARCHIVO, "w") as f:
            f.write("segundos,temperatura_c,luz\n")
        return True


def main():
    nuevo = crear_encabezado()
    print("U4-E08 iniciada: registrando en", ARCHIVO,
          "(archivo nuevo)" if nuevo else "(se agregan datos al existente)")
    inicio = time.ticks_ms()
    try:
        while True:
            segundos = time.ticks_diff(time.ticks_ms(), inicio) // 1000
            temperatura = leer_temperatura()
            luz = ldr.read_u16()
            linea = "{},{:.2f},{}\n".format(segundos, temperatura, luz)
            # Se abre y se cierra en cada medicion: asi el dato queda
            # realmente escrito aunque se corte la energia despues.
            with open(ARCHIVO, "a") as f:
                f.write(linea)
            led.toggle()
            print(linea.strip())
            time.sleep(INTERVALO_S)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario. Datos guardados en", ARCHIVO)
    finally:
        led.value(0)


main()
