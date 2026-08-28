#!/usr/bin/env python3
"""
RP3-E09 - Raspberry Pi + ESP32: dos sensores, un solo enlace UART
Placa: Raspberry Pi 3 Model B+ (lado receptor)
Biblioteca: pyserial

Objetivo: ampliar RP3-P06 para distinguir el origen de cada lectura cuando
la ESP32 envia datos de MAS DE UN sensor por el mismo UART. Se asume que el
lado ESP32 fue modificado (ver comentario mas abajo) para anteponer un
identificador de sensor a cada mensaje, por ejemplo:
    ESP32:S1:123*A4
    ESP32:S2:087*3F

Requiere el mismo cableado y la misma habilitacion de UART de RP3-P06.

Cambio necesario en el lado ESP32 (RP3-P06-emisor.ino), a modo de referencia:
    String mensaje = "ESP32:S1:" + String(lecturaSensor1);
    ...
    String mensaje = "ESP32:S2:" + String(lecturaSensor2);
  (usando el mismo enviarMensaje() y checksumSimple() ya definidos alli)
"""
import csv
import time
from datetime import datetime

import serial

PUERTO = "/dev/serial0"
VELOCIDAD = 9600
ARCHIVO_CSV = "registro_rp3_e09.csv"


def checksum_simple(datos: str) -> int:
    suma = 0
    for caracter in datos:
        suma ^= ord(caracter)
    return suma & 0xFF


def procesar_linea(linea: str):
    """Devuelve (origen, valor) o (None, None) si el mensaje es invalido."""
    linea = linea.strip()
    if "*" not in linea:
        return None, None
    mensaje, _, chk_txt = linea.rpartition("*")
    try:
        chk_recibido = int(chk_txt, 16)
    except ValueError:
        return None, None
    if checksum_simple(mensaje) != chk_recibido:
        return None, None

    # Formato esperado: ESP32:<origen>:<valor>
    partes = mensaje.split(":")
    if len(partes) != 3:
        return None, None
    _, origen, valor = partes
    return origen, valor


def main():
    print(f"RP3-E09 iniciado: {PUERTO} a {VELOCIDAD} baudios, distinguiendo por origen")

    with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as csv_file:
        escritor = csv.writer(csv_file)
        if csv_file.tell() == 0:
            escritor.writerow(["marca_tiempo", "origen", "valor"])

        try:
            with serial.Serial(PUERTO, VELOCIDAD, timeout=2) as puerto_serie:
                while True:
                    linea_cruda = puerto_serie.readline().decode("utf-8", errors="ignore")
                    if not linea_cruda:
                        continue

                    origen, valor = procesar_linea(linea_cruda)
                    if origen is None:
                        print(f"Mensaje descartado: {linea_cruda!r}")
                        continue

                    marca = datetime.now().isoformat(timespec="seconds")
                    print(f"[{marca}] Origen={origen}  Valor={valor}")
                    escritor.writerow([marca, origen, valor])
                    csv_file.flush()
        except KeyboardInterrupt:
            print("\nDetenido por el usuario.")
        except serial.SerialException as error:
            print(f"Error al abrir el puerto serie: {error}")


if __name__ == "__main__":
    main()
