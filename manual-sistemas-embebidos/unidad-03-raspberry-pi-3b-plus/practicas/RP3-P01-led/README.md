# RP3-P01 — LED externo en GPIO17

**Plataforma:** Raspberry Pi 3 Model B+ (Raspberry Pi OS)
**Nivel:** Básico
**Biblioteca:** gpiozero

## Objetivo
Configurar GPIO17 (pin físico 11) como salida, encender y apagar un LED
externo y comprobar el estado por terminal.

## Materiales
- Raspberry Pi 3 Model B+ configurada (SSH o monitor/teclado)
- Protoboard
- 1 LED
- 1 resistencia de 220–330 Ω
- 2 cables de conexión

## Conexiones
| Origen | Destino | Función |
|---|---|---|
| GPIO17 (pin físico 11) | Resistencia 220–330 Ω | Limita la corriente |
| Resistencia | Ánodo del LED (terminal largo) | Alimenta el LED |
| Cátodo del LED (terminal corto) | GND (pin físico 9, por ejemplo) | Cierra el circuito |

## Instalación
```bash
pip install gpiozero --break-system-packages
```
(gpiozero normalmente ya viene preinstalado en Raspberry Pi OS)

## Ejecución
```bash
python3 RP3-P01-led.py
```
Detener con `Ctrl+C`.

## Resultado esperado
El LED alterna encendido/apagado cada segundo; la terminal imprime un
mensaje por cada cambio de estado.

## Advertencias
- No omitir la resistencia.
- No conectar el LED entre 5V y GPIO17: el GPIO no tolera 5V.
- Usar el número **GPIO/BCM (17)**, no el número de pin físico (11), en el código.

## Errores frecuentes
- `ModuleNotFoundError: gpiozero` → instalar el paquete.
- No enciende → LED invertido, mala continuidad, o GPIO confundido con pin físico.
- Error de permisos → confirmar que el usuario pertenece al grupo `gpio`.
