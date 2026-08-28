# Unidad 3 — Raspberry Pi 3 Model B+ — Códigos descargables

Esta carpeta contiene el código fuente completo de las prácticas y
ejercicios de la Unidad 3 del manual, para no tener que transcribirlo desde
el libro.

```
unidad-03-raspberry-pi-3b-plus/
  practicas/
    RP3-P01-led/
      RP3-P01-led.py
      README.md
    RP3-P02-pulsador/
      RP3-P02-pulsador.py
      README.md
    RP3-P03-servo/
      RP3-P03-servo.py
      README.md
    RP3-P04-i2c/
      RP3-P04-i2c.py
      README.md
    RP3-P05-servidor-web/
      app.py
      README.md
    RP3-P06-raspberry-esp32/
      raspberry/RP3-P06-receptor.py
      esp32/RP3-P06-emisor.ino
      README.md
  ejercicios/
    RP3-E01-led-por-tiempo/
    RP3-E02-pulsador-contador/
    RP3-E03-control-pwm/
    RP3-E04-servo-por-entrada/
    RP3-E05-lectura-i2c/
    RP3-E06-registro-datos/
    RP3-E07-servidor-web/
    RP3-E08-ssh-control-remoto/
    RP3-E09-raspberry-esp32/
    RP3-E10-mini-sistema-iot/
  imagenes/
  LEEME.md
```

Todo el código de las prácticas y ejercicios usa Python 3 con `gpiozero`
como biblioteca principal de GPIO (justificación en la sección 3.6 del
manual), `smbus2` para el sensor I²C, `Flask` para las prácticas de
servidor web, y `pyserial` para la comunicación UART con la ESP32. Cada
`.py` fue verificado con `python3 -m py_compile` (sin errores de sintaxis).

**Pendiente:** subir esta carpeta al repositorio
`FranciscoAgurto09/Codigo-Descargable`, dentro de
`manual-sistemas-embebidos/unidad-03-raspberry-pi-3b-plus/` (mismo patrón
que las Unidades 1 y 2), y luego reemplazar `PENDIENTE` por esa URL en
`\UrlCodigos` dentro de `unidad3_raspberrypi.tex`, para que el código QR de
la portada y de cada práctica apunte aquí automáticamente.
