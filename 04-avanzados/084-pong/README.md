# 084 Pong

El clásico tenis de mesa para dos jugadores en la misma computadora. Cada
jugador mueve su paleta para devolver la pelota, y si se le escapa, el otro
gana un punto. La pelota acelera con cada golpe, y el ángulo con que sale
depende de dónde la golpeas: en el centro sale recta y en la orilla sale
inclinada. Gana quien llegue primero a cinco puntos.

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
| Mover jugador 1 | W y S |
| Mover jugador 2 | Flechas arriba y abajo |
| Empezar o volver al menú | Espacio |
| Salir | Esc o cerrar la ventana |

## Qué vas a practicar

En este proyecto vas a organizar el juego como una máquina de estados: el
juego siempre está en uno solo de tres estados, `MENU`, `JUGANDO` o `FIN`,
guardados en un `Enum`. Cada estado decide qué se dibuja y qué hace la tecla
Espacio, y el juego pasa de uno a otro cuando ocurre algo: empezar la
partida o llegar a cinco puntos. Así no mezclas en cada cuadro las reglas
del menú con las del partido.

Los choques se detectan con `colliderect()`, que dice si dos rectángulos se
enciman. Para el ángulo de rebote se mide qué tan lejos del centro de la
paleta pegó la pelota y se convierte en un ángulo, y con `math.cos()` y
`math.sin()` ese ángulo se vuelve la velocidad horizontal y vertical.

Símbolos y sintaxis nuevos: `colliderect()`, la máquina de estados con
`Enum`, `None`, `pygame.font.Font()` con `render()` para escribir texto, el
operador `//` de división entera, `math.radians()`, `math.cos()` y
`math.sin()`.
