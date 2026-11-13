# 082 Pelota que rebota

Seis pelotas de colores y tamaños al azar rebotan contra los bordes de la
ventana, cada una con su propia velocidad y dirección. Cada vez que haces
clic aparece una pelota nueva donde está el mouse.

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
| Agregar una pelota | Clic izquierdo |
| Salir | Cerrar la ventana |

## Qué vas a practicar

En este proyecto cada pelota es un objeto de la clase `Pelota`, con su
propia posición, velocidad, radio y color. La posición y la velocidad son
`pygame.Vector2`, un tipo que guarda `x` y `y` juntos: con una sola
operación, `posicion + velocidad * dt`, se mueven las dos coordenadas.

En el proyecto 081 la nube avanzaba 2 píxeles por cuadro, así que iba más
lenta si el juego corría a menos FPS. Aquí la velocidad está en píxeles por
segundo y se multiplica por el delta time (`dt`), el tiempo que pasó desde
el cuadro anterior. Si un cuadro tarda más, `dt` es mayor y la pelota da un
paso más largo, así que recorre la misma distancia por segundo en cualquier
computadora.

Símbolos y sintaxis nuevos: `pygame.Vector2`, el delta time con el valor
que devuelve `tick()`, la función `abs()` y el evento
`pygame.MOUSEBUTTONDOWN` con `evento.pos`.
