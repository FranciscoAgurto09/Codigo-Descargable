# U2-P02 — Servomotor SG90 en GPIO18

**Plataforma:** ESP32 DevKit V1 de 30 pines (módulo ESP32-WROOM-32)
**Nivel:** Intermedio
**Biblioteca:** ESP32Servo (Kevin Harrington — github.com/madhephaestus/ESP32Servo)
**Monitor serie:** 115200 bit/s

## Objetivo
Controlar la posición de un servomotor SG90 mediante GPIO18, alimentándolo
desde una fuente externa de 5 V con tierra común (nunca desde 3V3 o un GPIO).

## Materiales
- Placa ESP32 DevKit V1
- Servomotor SG90
- Fuente externa regulada de 5 V apropiada para el servo
- Protoboard o distribución de alimentación
- Cables y Micro-USB

## Conexiones
| Origen | Destino | Función |
|---|---|---|
| GPIO18 de la ESP32 | Señal del SG90 (naranja/amarilla) | Pulsos de control |
| Positivo de fuente externa 5 V | Positivo del SG90 (rojo) | Energía del actuador |
| GND de fuente externa | GND del SG90 (café/negro) | Retorno de potencia |
| GND de fuente externa | GND de la ESP32 | Referencia común para la señal |

## Instalación de la biblioteca
Gestor de bibliotecas de Arduino IDE → buscar `ESP32Servo` → verificar autor
(Kevin Harrington) y compatibilidad con la versión instalada de Arduino-ESP32
→ instalar. Registrar las versiones usadas.

## Procedimiento
1. Probar la fuente externa sin el servo conectado.
2. Unir GND de la fuente y GND de la placa.
3. Conectar señal, positivo y retorno del servo con todo desenergizado.
4. Cargar `U2-P02-servomotor.ino`.
5. Conectar la fuente del servo, energizar y observar.
6. Abrir el monitor serie a 115200 bit/s.

## Resultado esperado
El servo se centra en 90°, recorre suavemente de 10° a 170° y vuelve. El
monitor indica el sentido de cada barrido.

## Advertencias
- No alimentar el servo desde 3V3 ni desde un GPIO: no son fuentes de potencia.
- No usar el pin VIN/5V de la placa para el servo salvo que se conozca el
  esquema exacto del fabricante.
- Verificar el pinout real del servo: los colores no son una norma universal.

## Errores frecuentes
- **No se mueve:** revisar GND común, señal y positivo.
- **Vibra:** mejorar fuente/conexiones, separar potencia de señal.
- **Zumba en un extremo:** reducir el ángulo máximo o ajustar los
  microsegundos de `attach()`.
- **La ESP32 se reinicia:** fuente o retorno compartido inadecuadamente.

Código fuente completo: `U2-P02-servomotor.ino` en esta misma carpeta.
