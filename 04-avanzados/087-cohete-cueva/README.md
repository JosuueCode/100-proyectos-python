# 087 Cohete en la cueva

Un juego de un solo botón. Pilotas un pequeño cohete que avanza por una
cueva: la gravedad lo jala hacia abajo y cada vez que pulsas Espacio el
motor da un impulso hacia arriba. Tienes que cruzar los huecos entre las
rocas del techo y del piso sin tocar nada. Cada roca que dejas atrás suma
un punto, y el hueco se va cerrando conforme avanzas. Si chocas, pulsas
Espacio y vuelves a intentarlo.

## Cómo instalarlo

Este proyecto usa pygame-ce, la edición comunitaria de pygame. Se importa
igual, con `import pygame`. Desde esta carpeta:

```bash
pip install -r requirements.txt
```

Si ya tenías instalado el paquete `pygame` original, desinstálalo antes con
`pip uninstall pygame`, porque los dos usan el mismo nombre al importarse.

## Cómo ejecutarlo

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Controles

| Acción | Control |
|---|---|
| Impulso del motor | Espacio, flecha arriba o clic |
| Volver a intentar | Espacio, flecha arriba o clic |
| Salir | Esc o cerrar la ventana |

## Qué vas a practicar

En este proyecto vas a simular gravedad e impulso. La gravedad es una
aceleración: no mueve el cohete directamente, sino que en cada cuadro le
suma velocidad hacia abajo. Por eso la caída empieza lenta y se vuelve cada
vez más rápida. El impulso hace lo contrario de golpe: cambia la velocidad a
un valor fijo hacia arriba, así cada pulsación da el mismo salto aunque el
cohete viniera cayendo.

Las rocas se generan mientras juegas: cuando la última avanzó lo suficiente,
se crea otra a la derecha con el hueco a una altura al azar, y las que salen
por la izquierda se quitan de la lista. El cohete se dibuja girando sus
puntos con `Vector2.rotate()`, para que mire hacia arriba al subir y hacia
abajo al caer.

Símbolos y sintaxis nuevos: la gravedad como aceleración, el impulso como
cambio directo de velocidad y el método `rotate()` de `Vector2`.
