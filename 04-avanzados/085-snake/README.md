# 085 Snake

El juego de la serpiente. Guías a la serpiente por el tablero para que coma
las manzanas: cada una suma un punto, la hace crecer un cuadro y la acelera
un poco. Pierdes si chocas con una pared o con tu propio cuerpo. Tu mejor
puntaje se guarda como récord y sigue ahí la próxima vez que juegues.

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

El récord se guarda en `record.txt`, en la carpeta desde donde ejecutas el
juego.

## Controles

| Acción | Control |
|---|---|
| Cambiar de dirección | Flechas o W, A, S, D |
| Jugar otra vez | Espacio |
| Salir | Esc o cerrar la ventana |

## Qué vas a practicar

En este proyecto el movimiento es en cuadrícula: la serpiente es una lista
de celdas `(columna, fila)`, donde la primera es la cabeza. En cada paso se
agrega una cabeza nueva al inicio con `insert(0, ...)` y se quita la cola
con `pop()`; si come, la cola se queda y la serpiente crece. Los pasos no
ocurren en cada cuadro sino cada cierto intervalo, que se acorta al comer.

Hay tres reglas con su truco. No puedes girar en sentido contrario, porque
la cabeza chocaría con el cuello, y se compara con la dirección del último
paso para que dos teclas rápidas tampoco lo permitan. La comida se elige de
una lista de celdas libres, así nunca aparece sobre la serpiente. Y la
cabeza sí puede entrar donde está la cola, porque la cola se mueve en ese
mismo paso.

Símbolos y sintaxis nuevos: los métodos de lista `insert()` y `pop()`,
`Rect.inflate()`, la opción `border_radius` de `draw.rect()` y una capa
semitransparente con un color de cuatro valores, como `(0, 0, 0, 170)`.
