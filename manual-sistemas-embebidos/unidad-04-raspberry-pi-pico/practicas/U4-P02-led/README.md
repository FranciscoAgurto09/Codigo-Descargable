# U4-P02 — Encender un LED externo

**Plataforma:** Raspberry Pi Pico (RP2040)
**Firmware:** MicroPython
**Nivel:** Básico

## Objetivo
Controlar una salida digital y comprender el uso de la resistencia limitadora
trabajando a 3,3 V.

## Materiales
- Raspberry Pi Pico
- Protoboard
- 1 LED de 5 mm
- 1 resistencia de 220 Ω
- 2 cables de conexión

## Conexiones
| Origen | Destino | Función |
|---|---|---|
| `GP15` (posición física 20) | Resistencia de 220 Ω | Limita la corriente de salida |
| Resistencia | Ánodo del LED (terminal largo) | Alimenta el LED |
| Cátodo del LED (terminal corto) | `GND` (posición física 18) | Cierra el circuito |

## Cálculo de la resistencia
Con un LED rojo de 2 V de caída alimentado desde 3,3 V y buscando unos 8 mA:

```
R = (3,3 - 2) / 0,008 ≈ 163 Ω  →  valor comercial: 220 Ω  (≈ 6 mA reales)
```

## Ejecución
Abrir en Thonny, pulsar **Run**, detener con `Ctrl+C`.

## Resultado esperado
El LED alterna encendido y apagado cada medio segundo; la consola imprime un
mensaje por cada cambio de estado.

## Variaciones sugeridas
- Reducir el intervalo hasta que el parpadeo se vuelva imperceptible.
- Agregar un segundo LED en otro pin y hacerlos alternar.
- Reemplazar la salida digital por `machine.PWM` y variar el brillo.

## Errores frecuentes
- LED invertido o sin resistencia.
- Confundir `GP15` con la posición física 15 (que es `GP11`).
- Cable conectado a un pin distinto del declarado en el programa.
