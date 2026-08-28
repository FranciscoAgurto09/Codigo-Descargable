# U4-P01 — Hola mundo por consola

**Plataforma:** Raspberry Pi Pico (RP2040)
**Firmware:** MicroPython
**Nivel:** Básico

## Objetivo
Comprobar que la placa, el cable, el firmware y el entorno funcionan, y
aprender a leer mensajes enviados desde el microcontrolador.

## Materiales
- Raspberry Pi Pico con MicroPython instalado
- Cable micro-USB **de datos** (los de solo carga no sirven)

## Conexiones
Ninguna. La práctica usa el LED integrado, conectado internamente a `GP25`.

## Instalación del firmware (una sola vez)
1. Descargar el `.uf2` de MicroPython para Raspberry Pi Pico desde la
   documentación oficial de Raspberry Pi.
2. Con la placa desconectada, mantener pulsado **BOOTSEL** y conectar el USB.
3. Arrastrar el `.uf2` sobre la unidad `RPI-RP2`. La placa se reinicia sola.

## Ejecución
1. Abrir el archivo en Thonny.
2. Seleccionar el intérprete *MicroPython (Raspberry Pi Pico)*.
3. Pulsar **Run**. Detener con el botón de parada o con `Ctrl+C`.

Para que arranque solo al energizar la placa, guardar el archivo **en la
Pico** con el nombre `main.py`.

## Resultado esperado
La consola imprime un contador que crece cada segundo y el LED verde de la
placa parpadea al mismo ritmo.

## Errores frecuentes
- Thonny no encuentra la placa → cable de solo carga, o firmware nunca instalado.
- La unidad `RPI-RP2` no aparece → BOOTSEL no estaba pulsado **antes** de conectar.
- Consola bloqueada → pulsar el botón de parada de Thonny.

## Atención
Este programa usa el LED de `GP25`, que **no existe en la Pico W**: en esa
placa el LED está conectado al chip inalámbrico.
