# 090 Juego de memoria

Dieciséis cartas boca abajo esconden ocho parejas de figuras de colores.
Haz clic en dos cartas para voltearlas: si son iguales se quedan
descubiertas, y si no, las verás un momento antes de que se vuelvan a
tapar. El juego cuenta tus movimientos y el tiempo, y al encontrar todas
las parejas te muestra la pantalla de victoria con tu resultado.

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
| Voltear una carta | Clic izquierdo |
| Jugar otra vez | Espacio |
| Salir | Esc o cerrar la ventana |

## Qué vas a practicar

En este proyecto vas a barajar con `random.shuffle()`, que revuelve una
lista en su lugar: no crea otra, cambia el orden de la misma. La lista tiene
cada carta dos veces, y después de revolverla, la posición de cada carta en
la cuadrícula sale de su índice con `//` para la fila y `%` para la columna.

Cuando volteas dos cartas distintas, el programa no puede detenerse con
`sleep()` para que las veas, porque la ventana se congelaría, como viste en
el proyecto 080. En su lugar anota el momento en que hay que taparlas, con
`pygame.time.get_ticks()` más 800 milisegundos, y pasa al estado
`ESPERANDO`. El ciclo de juego sigue dibujando, y cuando llega ese momento,
`actualizar()` las tapa. Mientras tanto, los clics se ignoran.

Símbolos y sintaxis nuevos: `random.shuffle()`, `pygame.time.get_ticks()`,
`Rect.collidepoint()`, `evento.button` y el formato `:02d` para escribir un
número con dos dígitos.
