# U4-P03 — Mover un servomotor

**Plataforma:** Raspberry Pi Pico (RP2040)
**Firmware:** MicroPython
**Nivel:** Intermedio

## Objetivo
Comandar un actuador con posición controlada, generar una señal PWM de
frecuencia y ancho definidos, y reconocer la necesidad de alimentación
independiente.

## Materiales
- Raspberry Pi Pico
- 1 servomotor SG90
- Fuente externa de 5 V o portapilas
- Protoboard y cables

## Conexiones
| Origen | Destino | Función |
|---|---|---|
| Cable de señal (naranjo/amarillo) | `GP16` (posición física 21) | Señal PWM de 50 Hz |
| Cable rojo | +5 V de la **fuente externa** | Alimenta el servo |
| Cable café o negro | `GND` de la fuente externa | Retorno del servo |
| `GND` de la fuente externa | `GND` de la Pico | **Tierra común, obligatoria** |

## Cómo se calcula el ciclo de trabajo
A 50 Hz el período es de 20 ms. El servo interpreta el ancho del pulso, entre
unos 0,5 ms (0°) y 2,5 ms (180°):

```
duty_u16 = (ancho_ms / 20 ms) × 65535
0,5 ms → 1638      1,5 ms → 4915      2,5 ms → 8192
```

## Ejecución
Abrir en Thonny, pulsar **Run**, detener con `Ctrl+C`.

## Resultado esperado
El eje gira hasta 0°, 90° y 180°, y se mantiene en cada posición resistiendo
pequeñas fuerzas externas.

## Advertencias
- **Nunca** alimentar el servo desde el pin `3V3`: provoca reinicios y puede
  dañar la placa.
- Un zumbido permanente significa que el servo fuerza contra un tope mecánico:
  corregir el rango de movimiento.
- Si el movimiento resulta errático, intercalar un adaptador de nivel entre
  `GP16` y la entrada de señal del servo.
