# 083 Nave con teclado

Una nave triangular sobre un fondo de estrellas que puedes mover en ocho
direcciones con las flechas o con WASD. La nave nunca sale de la ventana y
en diagonal va a la misma velocidad que en línea recta. Con la tecla C
cambias su color.

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
| Mover | Flechas o W, A, S, D |
| Cambiar color | C |
| Salir | Esc o cerrar la ventana |

## Qué vas a practicar

En este proyecto la nave hereda de `pygame.sprite.Sprite`, la clase base de
pygame para los objetos del juego. Un sprite tiene una `image`, la
superficie con su dibujo, y un `rect`, un `pygame.Rect` que dice dónde está
y cuánto mide.

Vas a leer el teclado de dos formas. `key.get_pressed()` te dice qué teclas
están presionadas en este momento; como se revisa en cada cuadro, sirve
para el movimiento continuo mientras mantienes la flecha. El evento
`KEYDOWN` ocurre una sola vez cuando pulsas una tecla, así que sirve para
acciones puntuales como cambiar de color. Si usaras `get_pressed()` para el
color, cambiaría en cada cuadro mientras la tecla siga abajo.

En diagonal, la dirección `(1, 1)` mide 1.41 en lugar de 1, y la nave iría
más rápido. `normalize()` la ajusta para que mida 1 sin cambiar hacia dónde
apunta.

Símbolos y sintaxis nuevos: `pygame.sprite.Sprite`, `pygame.Surface` con
`SRCALPHA`, `pygame.Rect` y `get_rect()`, `blit()`, `key.get_pressed()` con
las constantes `K_LEFT`, `K_a` y demás, el evento `KEYDOWN` y los métodos
`length()` y `normalize()` de `Vector2`.
