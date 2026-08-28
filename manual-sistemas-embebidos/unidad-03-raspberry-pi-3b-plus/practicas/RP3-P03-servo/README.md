# RP3-P03 — Servomotor SG90 en GPIO18

**Plataforma:** Raspberry Pi 3 Model B+ (Raspberry Pi OS)
**Nivel:** Intermedio
**Biblioteca:** gpiozero

## Objetivo
Controlar la posición de un servomotor SG90 mediante PWM desde GPIO18
(pin físico 12), alimentado desde una fuente externa de 5V con tierra común.

## Materiales
- Raspberry Pi 3 Model B+
- Servomotor SG90
- Fuente externa regulada de 5V apropiada para el servo
- Protoboard/distribución de alimentación, cables

## Conexiones
| Origen | Destino | Función |
|---|---|---|
| GPIO18 (pin físico 12) | Señal del SG90 | Pulsos de control PWM |
| Positivo fuente externa 5V | Positivo del SG90 | Energía del actuador |
| GND de fuente externa | GND del SG90 | Retorno de potencia |
| GND de fuente externa | GND de la Raspberry Pi | Referencia común |

## Instalación
```bash
pip install gpiozero --break-system-packages
```

## Ejecución
```bash
python3 RP3-P03-servo.py
```

## Resultado esperado
El servo se centra y realiza un barrido suave entre los límites definidos.

## Advertencias
- **Nunca** alimentar el servo desde 3.3V ni desde un GPIO.
- No usar el pin de 5V del header sin conocer su capacidad de corriente real.
- Verificar el pinout real del servo (los colores de cable no son una norma).

## Errores frecuentes
- No se mueve → revisar GND común, señal y alimentación del servo.
- Vibra/errático → jitter del PWM por software; reducir carga de CPU.
- La Raspberry Pi se reinicia → fuente del servo insuficiente o mal compartida.
