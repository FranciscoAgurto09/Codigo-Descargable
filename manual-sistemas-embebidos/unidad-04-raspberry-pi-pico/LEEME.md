# Unidad 4 — Raspberry Pi Pico — Códigos descargables

Esta carpeta contiene el código fuente completo de las prácticas y ejercicios
de la Unidad 4 del manual, para no tener que transcribirlo desde el libro.

```
unidad-04-raspberry-pi-pico/
  practicas/
    U4-P01-hola-mundo/
      U4-P01-hola-mundo.py
      README.md
    U4-P02-led/
      U4-P02-led.py
      README.md
    U4-P03-servo/
      U4-P03-servo.py
      README.md
  ejercicios/
    U4-E01-semaforo/
    U4-E02-pulsador-led/
    U4-E03-atenuador-potenciometro/
    U4-E04-luz-automatica/
    U4-E05-termometro-interno/
    U4-E06-barra-nivel/
    U4-E07-servo-potenciometro/
    U4-E08-registro-flash/
  imagenes/
  LEEME.md
```

## Plataforma

Todo el código está escrito en **MicroPython** para la **Raspberry Pi Pico
original (RP2040)**. No usa bibliotecas externas: solo los módulos `machine` y
`time`, incluidos en el propio firmware. Cada `.py` fue verificado con
`python3 -m py_compile` (sin errores de sintaxis).

> **Atención:** los programas que usan el LED integrado (`GP25`) **no funcionan
> sin modificación en una Pico W**, donde ese LED está conectado al chip
> inalámbrico y no a un GPIO.

## Antes de empezar: instalar el firmware (una sola vez)

1. Descargar el archivo `.uf2` de MicroPython para Raspberry Pi Pico desde la
   documentación oficial: <https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html>
2. Con la placa desconectada, mantener pulsado **BOOTSEL** y, sin soltarlo,
   conectar el cable micro-USB.
3. La Pico aparece como una unidad llamada `RPI-RP2`. Arrastrar el `.uf2`
   sobre ella; la placa se reinicia sola y la unidad desaparece.

## Cómo ejecutar un programa

1. Abrir el archivo `.py` en **Thonny**.
2. Seleccionar el intérprete *MicroPython (Raspberry Pi Pico)* en el extremo
   inferior derecho.
3. Pulsar **Run**. Detener con el botón de parada o con `Ctrl+C` en la consola.

Para que un programa arranque solo al energizar la placa, hay que guardarlo
**dentro de la Pico** con el nombre `main.py`
(*Archivo → Guardar como… → Raspberry Pi Pico*).

## Pines utilizados

| Recurso | Pin lógico | Posición física | Usado en |
|---|---|---|---|
| LED integrado | `GP25` | interno | P01, E08 |
| LED externo | `GP15` | 20 | P02, E02, E03, E04 |
| Servomotor (señal) | `GP16` | 21 | P03, E07 |
| Pulsador (`PULL_UP`) | `GP14` | 19 | E02 |
| Semáforo | `GP13`, `GP14`, `GP15` | 17, 19, 20 | E01 |
| Barra de nivel | `GP10` a `GP14` | 14, 15, 16, 17 y 19 (la 18 es `GND`) | E06 |
| Potenciómetro (ADC0) | `GP26` | 31 | E03, E06, E07 |
| Fotorresistencia (ADC1) | `GP27` | 32 | E04, E08 |
| Sensor de temperatura | canal interno 4 | — | E05, E08 |

## Recordatorios eléctricos

- La lógica de la Pico es de **3,3 V y no tolera 5 V**. Los potenciómetros y
  divisores de estos ejercicios se alimentan desde `3V3`, nunca desde `VBUS`.
- La **suma** de la corriente de todos los pines está limitada a unos 50 mA.
- El servomotor se alimenta siempre desde una **fuente externa de 5 V**, con su
  tierra unida a la de la Pico. Nunca desde el pin `3V3`.

## Pendiente

Subir esta carpeta al repositorio `FranciscoAgurto09/Codigo-Descargable`,
dentro de `manual-sistemas-embebidos/unidad-04-raspberry-pi-pico/` (mismo
patrón que las Unidades 1, 2 y 3), y luego reemplazar `PENDIENTE` por esa URL
en `\UrlCodigos` dentro de `unidad4_pico.tex`, para que el código QR de la
portada y el de la sección de prácticas apunten aquí automáticamente.
