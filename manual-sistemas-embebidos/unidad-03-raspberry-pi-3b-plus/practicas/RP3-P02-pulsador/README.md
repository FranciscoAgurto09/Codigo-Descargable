# RP3-P02 — Pulsador con LED de respuesta

**Plataforma:** Raspberry Pi 3 Model B+ (Raspberry Pi OS)
**Nivel:** Básico
**Biblioteca:** gpiozero

## Objetivo
Leer una entrada digital con antirrebote y pull-up (sin dejar el pin
flotante) y encender un LED mientras el pulsador está presionado.

## Materiales
- Raspberry Pi 3 Model B+
- Protoboard, pulsador, LED, resistencia 220–330 Ω, cables

## Conexiones
| Origen | Destino | Función |
|---|---|---|
| GPIO27 (pin físico 13) | Una pata del pulsador | Entrada digital |
| Otra pata del pulsador | GND | Cierra el circuito al presionar |
| GPIO17 (pin físico 11) | Resistencia + LED (igual que RP3-P01) | Salida de respuesta |

## Instalación
```bash
pip install gpiozero --break-system-packages
```

## Ejecución
```bash
python3 RP3-P02-pulsador.py
```

## Resultado esperado
El LED enciende mientras se mantiene presionado el pulsador y se apaga al
soltarlo. La terminal cuenta las pulsaciones válidas (sin contar rebotes).

## Advertencias
- No conectar el pulsador directamente entre 3.3V y GND sin una entrada de
  control intermedia (cortocircuito franco al presionar).
- `Button` de gpiozero ya configura pull-up y antirrebote: no dejar la
  entrada sin resistencia de referencia si se implementa manualmente.

## Errores frecuentes
- Lecturas erráticas → entrada flotante, usar siempre `Button`.
- Cuenta varias pulsaciones por una → ajustar `bounce_time`.
- No responde → verificar continuidad del pulsador.
