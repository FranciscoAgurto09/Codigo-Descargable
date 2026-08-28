# RP3-P04 — Sensor I²C de luz ambiental BH1750

**Plataforma:** Raspberry Pi 3 Model B+ (Raspberry Pi OS), bus I²C1 habilitado
**Nivel:** Intermedio
**Biblioteca:** smbus2

## Objetivo
Activar el bus I²C, identificar el sensor conectado y leer su medición de
iluminancia directamente desde sus registros (sin biblioteca de alto nivel).

## Materiales
- Raspberry Pi 3 Model B+
- Módulo sensor de luz ambiental BH1750 (GY-30)
- Cables de conexión

## Conexiones
| Origen | Destino | Función |
|---|---|---|
| 3.3V (pin físico 1) | VCC del BH1750 | Alimentación |
| GND (pin físico 6) | GND del BH1750 | Referencia común |
| GPIO2 / SDA (pin físico 3) | SDA del BH1750 | Datos I²C |
| GPIO3 / SCL (pin físico 5) | SCL del BH1750 | Reloj I²C |

## Activación de I²C y escaneo
```bash
sudo raspi-config          # Interface Options -> I2C -> Enable, luego reiniciar
sudo apt install -y i2c-tools
sudo i2cdetect -y 1        # debe mostrar 0x23 (o 0x5C)
```

## Instalación
```bash
pip install smbus2 --break-system-packages
```

## Ejecución
```bash
python3 RP3-P04-i2c.py
```

## Resultado esperado
La terminal imprime periódicamente la iluminancia en lux, cambiando al
cubrir o iluminar el sensor.

## Advertencias
- Alimentar el BH1750 a 3.3V (no 5V) salvo que el módulo tenga regulador propio verificado.
- El bus I²C1 de la Raspberry Pi ya trae pull-ups fijas; no agregar externas.

## Errores frecuentes
- `i2cdetect` no muestra nada → I²C no habilitado, o SDA/SCL invertidos.
- `OSError: [Errno 121] Remote I/O error` → dirección incorrecta o sensor sin alimentación.
- Lectura en cero/saturada → sensor tapado, no necesariamente un error de código.
