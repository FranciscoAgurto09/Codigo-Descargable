# Unidad 1 — Arduino Uno R3

Códigos de referencia del **Manual educativo de sistemas embebidos y
plataformas de desarrollo**. Cada archivo corresponde al código que aparece en
el encabezado de la práctica o del ejercicio dentro del manual impreso.

---

## Estructura

```
unidad-01-arduino-uno-r3/
    practicas/
        U1-P01-hola-mundo/U1-P01-hola-mundo.ino
        U1-P02-encender-led/U1-P02-encender-led.ino
        U1-P03-mover-servo/U1-P03-mover-servo.ino
    ejercicios/
        U1-E01-semaforo/U1-E01-semaforo.ino
        ...
    LEEME.md
```

Cada sketch vive en una carpeta con su mismo nombre: es un requisito del
Arduino IDE. Si se cambia el nombre del archivo, debe cambiarse también el de
la carpeta.

---

## Prácticas guiadas (sección 1.7)

| Código | Práctica | Pines usados | Biblioteca |
|---|---|---|---|
| `U1-P01` | Hola mundo por monitor serie | ninguno | — |
| `U1-P02` | Encender un LED | 9 | — |
| `U1-P03` | Mover un servomotor | 9 | `Servo` |

## Ejercicios propuestos (sección 1.8)

| Código | Ejercicio | Pines usados | Nivel |
|---|---|---|---|
| `U1-E01` | Semáforo de tres LED | 2, 3, 4 | Básico |
| `U1-E02` | LED comandado por pulsador | 2, 9 | Básico |
| `U1-E03` | Atenuador con potenciómetro | A0, 9 | Intermedio |
| `U1-E04` | Luz automática con fotorresistencia | A0, 9 | Intermedio |
| `U1-E05` | Termómetro por monitor serie | A0 | Intermedio |
| `U1-E06` | Barra de nivel con cinco LED | A0, 2–6 | Intermedio |
| `U1-E07` | Servo comandado por potenciómetro | A0, 9 | Intermedio |
| `U1-E08` | Alarma de proximidad con zumbador | 8, 9, 10, 13 | Avanzado |

---

## Cómo usar estos archivos

1. Descargar el repositorio (botón **Code → Download ZIP**) o clonarlo.
2. Abrir el archivo `.ino` con el Arduino IDE.
3. Seleccionar **Herramientas → Placa → Arduino Uno**.
4. Seleccionar **Herramientas → Puerto** (`COM3` en Windows, `/dev/ttyACM0` en
   Linux, `/dev/cu.usbmodem…` en macOS).
5. Presionar **Verificar** y luego **Subir**.
6. Para las prácticas que envían datos, abrir el **Monitor serie** a
   **9600 baudios**.

> Los ejercicios están pensados para intentarse antes de mirar el código. Se
> recomienda usar estos archivos como referencia de contraste, no como punto de
> partida.

---

## Bibliotecas necesarias

| Biblioteca | Se usa en | Instalación |
|---|---|---|
| `Servo` | `U1-P03`, `U1-E07` | Ya viene incluida en el IDE |

El resto de los sketches solo usa funciones del núcleo de Arduino.

---

## Recordatorios eléctricos

- Máximo **20 mA** por pin (40 mA es el límite absoluto, con riesgo de daño).
- Máximo **50 mA** en el pin de 3,3 V.
- Un LED **siempre** con resistencia en serie (220 Ω para 5 V).
- Servos, motores y relés **nunca** se alimentan desde el pin de 5 V:
  requieren fuente propia con **tierra común**.
- Se conecta primero y se energiza después.

---

*Ingeniería Civil Electrónica · 2026*
