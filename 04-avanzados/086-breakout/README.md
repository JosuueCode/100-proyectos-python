# 086 Breakout

Un rompe ladrillos. Mueves una paleta en la parte de abajo para que la
pelota no se caiga, y cada ladrillo que toca desaparece y te da puntos: los
de arriba valen más. Tienes tres vidas. Al romper todos los ladrillos pasas
de nivel, con una fila más y la pelota más rápida, y si superas el nivel 3,
ganas.

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
| Mover la paleta | Flechas izquierda y derecha, o A y D |
| Lanzar la pelota o jugar otra vez | Espacio |
| Salir | Esc o cerrar la ventana |

## Qué vas a practicar

En este proyecto vas a usar grupos de sprites. Un `pygame.sprite.Group`
guarda varios sprites y trabaja con todos a la vez: `update()` actualiza a
cada uno, `draw()` los dibuja y `spritecollide()` te dice cuáles chocan con
otro sprite. Cuando la pelota rompe un ladrillo, `kill()` lo saca del grupo,
y cuando el grupo queda vacío, se acabó el nivel.

Para que el rebote se vea natural, el juego detecta por qué lado entró la
pelota al ladrillo. Mide cuánto se enciman en cada eje: si se enciman poco a
lo ancho, entró por un costado y rebota hacia el lado; si se enciman poco a
lo alto, entró por arriba o por abajo y rebota en vertical.

Símbolos y sintaxis nuevos: `pygame.sprite.Group` con `add()`, `empty()`,
`update()` y `draw()`, `pygame.sprite.spritecollide()`, el método `kill()`
de los sprites y el método `update()` que pygame llama en cada sprite.
