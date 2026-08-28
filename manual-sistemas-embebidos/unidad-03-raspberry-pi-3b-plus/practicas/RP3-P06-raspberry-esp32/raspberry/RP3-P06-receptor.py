#!/usr/bin/env python3
"""
RP3-P06 - Lado Raspberry Pi: receptor UART desde la ESP32
Placa: Raspberry Pi 3 Model B+ (Raspberry Pi OS)
Biblioteca: pyserial

Objetivo: recibir por UART los mensajes que envia la ESP32 (ver
esp32/RP3-P06-emisor.ino), validar la suma de verificacion, e ir
registrando cada mensaje valido en un archivo CSV con marca de tiempo.

IMPORTANTE (especifico de la Raspberry Pi 3 B+): en los modelos con
Bluetooth integrado, el UART de hardware completo (PL011) esta asignado por
defecto al Bluetooth, y los pines fisicos 8/10 (GPIO14/15) quedan conectados
al mini-UART. Antes de ejecutar este script:
    sudo raspi-config -> Interface Options -> Serial Port
        "Would you like a login shell over serial?"  -> No
        "Would you like the serial port hardware enabled?" -> Yes
    Reiniciar.

Conexiones (ver tabla completa en el manual, RP3-P06):
    GPIO14 (TXD, pin fisico 8)  -> RX de la ESP32 (GPIO16 / UART2 RX)
    GPIO15 (RXD, pin fisico 10) -> TX de la ESP32 (GPIO17 / UART2 TX)
    GND (pin fisico 6)          -> GND de la ESP32

Instalacion:
    pip install pyserial --break-system-packages

Ejecucion:
    python3 RP3-P06-receptor.py
"""
import csv
import time
from datetime import datetime

import serial

PUERTO = "/dev/serial0"   # apunta al UART de hardware habilitado
VELOCIDAD = 9600          # debe coincidir con la ESP32 (ver RP3-P06-emisor.ino)
ARCHIVO_CSV = "registro_rp3_p06.csv"


def checksum_simple(datos: str) -> int:
    """Debe coincidir exactamente con checksumSimple() del lado ESP32."""
    suma = 0
    for caracter in datos:
        suma ^= ord(caracter)
    return suma & 0xFF


def procesar_linea(linea: str) -> str | None:
    """
    Formato esperado (definido en la Unidad 2, ejercicio U2-E08):
        <mensaje>*<checksum_en_hex>
    Devuelve el mensaje si el checksum es valido, o None si es corrupto.
    """
    linea = linea.strip()
    if "*" not in linea:
        return None
    mensaje, _, chk_txt = linea.rpartition("*")
    try:
        chk_recibido = int(chk_txt, 16)
    except ValueError:
        return None
    if checksum_simple(mensaje) != chk_recibido:
        return None
    return mensaje


def main():
    print(f"RP3-P06 (receptor) iniciado: {PUERTO} a {VELOCIDAD} baudios")

    with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as csv_file:
        escritor = csv.writer(csv_file)
        if csv_file.tell() == 0:
            escritor.writerow(["marca_tiempo", "mensaje"])

        try:
            with serial.Serial(PUERTO, VELOCIDAD, timeout=2) as puerto_serie:
                while True:
                    linea_cruda = puerto_serie.readline().decode("utf-8", errors="ignore")
                    if not linea_cruda:
                        continue  # timeout sin datos; seguir esperando

                    mensaje = procesar_linea(linea_cruda)
                    if mensaje is None:
                        print(f"Mensaje descartado (checksum invalido): {linea_cruda!r}")
                        continue

                    marca = datetime.now().isoformat(timespec="seconds")
                    print(f"[{marca}] Recibido: {mensaje}")
                    escritor.writerow([marca, mensaje])
                    csv_file.flush()
        except KeyboardInterrupt:
            print("\nDetenido por el usuario.")
        except serial.SerialException as error:
            print(f"Error al abrir el puerto serie: {error}")
            print("Verificar que la UART de hardware este habilitada (raspi-config).")


if __name__ == "__main__":
    main()
