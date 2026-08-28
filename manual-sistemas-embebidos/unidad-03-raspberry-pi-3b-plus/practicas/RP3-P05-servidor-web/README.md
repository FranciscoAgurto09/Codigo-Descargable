# RP3-P05 — Servidor web para controlar GPIO17

**Plataforma:** Raspberry Pi 3 Model B+ (Raspberry Pi OS)
**Nivel:** Intermedio
**Bibliotecas:** Flask, gpiozero

## Objetivo
Publicar una interfaz web mínima que encienda/apague el LED de RP3-P01 y
muestre su estado actual, aprovechando que la Raspberry Pi ejecuta Linux.

## Materiales
- Montaje de RP3-P01 (LED en GPIO17)
- Raspberry Pi conectada a red Wi-Fi o Ethernet
- Teléfono o computador en la misma red

## Instalación
```bash
pip install flask gpiozero --break-system-packages
```

## Ejecución
```bash
hostname -I        # anota la IP de la Raspberry Pi
python3 app.py
```
Desde otro dispositivo en la misma red: `http://<ip>:5000`

## Resultado esperado
La página muestra el estado actual y los botones cambian el LED de
inmediato.

## Advertencias
- Sin autenticación: solo para red de laboratorio confiable.
- No exponer este servidor directamente a internet.

## Errores frecuentes
- No carga desde otro dispositivo → falta `host="0.0.0.0"` o cortafuegos bloqueando el puerto.
- `Address already in use` → otro proceso ya usa el puerto 5000.
