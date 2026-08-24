# U2-P01 — LED externo en GPIO23

**Plataforma:** ESP32 DevKit V1 de 30 pines (módulo ESP32-WROOM-32)
**Nivel:** Básico
**Monitor serie:** 115200 bit/s

## Objetivo
Configurar GPIO23 como salida, encender y apagar un LED externo, y comprobar
el estado mediante el monitor serie. No se usa el LED integrado de la placa
porque su existencia y GPIO varían entre fabricantes.

## Materiales
- Placa ESP32 DevKit V1
- Cable Micro-USB de datos
- Protoboard
- 1 LED
- 1 resistencia de 220 a 330 Ω
- 2 cables de conexión

## Conexiones
| Origen | Destino | Función |
|---|---|---|
| GPIO23 | Resistencia de 220–330 Ω | Limita la corriente de la salida |
| Resistencia | Ánodo del LED (terminal largo) | Alimenta el LED con corriente limitada |
| Cátodo del LED (terminal corto) | GND | Cierra el circuito hacia la referencia |

## Procedimiento
1. Montar el circuito con la placa desconectada.
2. Conectar el USB, seleccionar la placa y el puerto en Arduino IDE.
3. Cargar `U2-P01-led-externo.ino`.
4. Abrir el monitor serie a 115200 bit/s.

## Resultado esperado
El LED permanece un segundo encendido y un segundo apagado. El monitor
alterna `LED ENCENDIDO` / `LED APAGADO` en sincronía.

## Advertencias
- Desconectar el USB mientras se arma el circuito.
- No omitir la resistencia.
- No conectar el LED entre 5 V y GPIO23: el GPIO no es tolerante a 5 V.

## Errores frecuentes
- **No enciende:** LED invertido, mala continuidad, o cable en el GPIO equivocado.
- **Siempre encendido:** puente directo a 3V3 o 5V.
- **Mensajes ilegibles:** el monitor no está a 115200 bit/s.
- **Carga fallida:** cerrar otras ventanas serie, confirmar puerto, probar otro cable de datos.

Código fuente completo: `U2-P01-led-externo.ino` en esta misma carpeta.
