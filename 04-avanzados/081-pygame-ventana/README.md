# 081 Ventana y dibujo con pygame

Tu primer programa con pygame. Se abre una ventana con un paisaje dibujado
solo con figuras: una casa, un árbol, el sol con sus rayos y una nube que
cruza el cielo de un lado a otro. No hay imágenes: todo son rectángulos,
círculos, líneas y un triángulo.

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
| Salir | Cerrar la ventana |

## Qué vas a practicar

En este proyecto vas a conocer el ciclo de juego, la base de cualquier
videojuego. Es un `while` que se repite muchas veces por segundo y en cada
vuelta hace tres cosas, siempre en el mismo orden: lee los eventos (como
cerrar la ventana), actualiza lo que se mueve y dibuja un cuadro nuevo.
Cada vuelta es un cuadro de la animación, y la nube parece moverse porque
en cada cuadro se dibuja un poco más a la derecha.

`Clock.tick(60)` limita el ciclo a 60 cuadros por segundo (FPS). Sin ese
límite, el ciclo correría tan rápido como pueda tu computadora: usaría todo
el procesador y la nube iría más rápido en un equipo potente que en uno
lento.

Para dibujar, cada cuadro empieza borrando todo con `fill()`, dibuja las
figuras en memoria y las muestra de una vez con `display.flip()`. Las
coordenadas empiezan en la esquina superior izquierda, y la `y` crece hacia
abajo.

Símbolos y sintaxis nuevos: el módulo `pygame` con `pygame.init()`,
`display.set_mode()`, `display.set_caption()`, `event.get()`, el evento
`pygame.QUIT`, `draw.rect()`, `draw.circle()`, `draw.line()`,
`draw.polygon()`, `fill()`, `display.flip()`, `time.Clock()` con `tick()` y
`pygame.quit()`, y los colores como tuplas `(rojo, verde, azul)`.
