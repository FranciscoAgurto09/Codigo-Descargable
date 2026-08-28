# RP3-P06 — Raspberry Pi + ESP32 por UART

**Plataformas:** Raspberry Pi 3 Model B+ (Raspberry Pi OS) + ESP32 DevKit V1 (Unidad 2)
**Nivel:** Avanzado

## Objetivo
Demostrar una arquitectura embebida distribuida: la ESP32 adquiere una
lectura y controla tiempos con precisión de firmware; la Raspberry Pi
recibe esos datos por UART, los valida y los registra en un archivo CSV.

## Por qué UART (y no Wi-Fi)
Continúa directamente el ejercicio U2-E08 de la Unidad 2, no requiere
configurar red ni protocolo de aplicación adicional, y — a diferencia de la
pareja ESP32/Arduino Uno R3 de la Unidad 2 — **ambas placas usan lógica de
3,3 V**, por lo que **no se necesita** divisor resistivo ni conversor de
nivel lógico entre ellas.

## Conexiones
| Raspberry Pi | ESP32 DevKit V1 | Función |
|---|---|---|
| GPIO14 / TXD (pin físico 8) | GPIO16 / UART2 RX | Raspberry Pi envía, ESP32 recibe |
| GPIO15 / RXD (pin físico 10) | GPIO17 / UART2 TX | ESP32 envía, Raspberry Pi recibe |
| GND (pin físico 6) | GND | Referencia común obligatoria |

## Advertencia específica de la Raspberry Pi 3 B+
En los modelos con Bluetooth integrado (incluida la 3 B+), el UART de
hardware completo (PL011, `/dev/ttyAMA0`) está por defecto asignado al
Bluetooth; los pines físicos 8/10 quedan conectados al mini-UART
(`/dev/ttyS0`). Antes de ejecutar:

```bash
sudo raspi-config
# Interface Options -> Serial Port
#   "login shell over serial?"      -> No
#   "serial port hardware enabled?" -> Yes
# reiniciar
```

## Instalación
Raspberry Pi:
```bash
pip install pyserial --break-system-packages
```
ESP32: mismo núcleo Arduino-ESP32 usado en la Unidad 2 (Arduino IDE).

## Ejecución
1. Habilitar la UART de hardware en `raspi-config` y reiniciar.
2. Cargar `esp32/RP3-P06-emisor.ino` en la ESP32 desde Arduino IDE.
3. Conectar TX/RX/GND cruzados según la tabla, con ambas placas apagadas.
4. En la Raspberry Pi: `python3 raspberry/RP3-P06-receptor.py`
5. Alimentar la ESP32 y observar los mensajes llegando.

## Resultado esperado
La terminal de la Raspberry Pi muestra los mensajes recibidos y crece el
archivo `registro_rp3_p06.csv`.

## Errores frecuentes
- No llega nada → UART de hardware no habilitada, o TX/RX no cruzados correctamente.
- Mensajes corruptos → velocidades distintas entre placas, o mini-UART inestable.
- Conflicto con consola serie → la consola de login por serie sigue habilitada.
