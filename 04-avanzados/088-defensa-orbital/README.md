# 088 Defensa orbital

Una torreta en órbita protege su planeta de oleadas de drones. Los drones
llegan en formación, se mueven de un lado a otro y bajan un escalón cada vez
que tocan un borde. De vez en cuando alguno dispara hacia ti. Tienes tres
vidas, y después de cada golpe parpadeas un momento sin recibir daño. Cada
oleada llega con otra figura (bloque, V o rombo) y es más rápida que la
anterior. Si un dron alcanza el planeta, pierdes.

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
| Mover la torreta | Flechas izquierda y derecha, o A y D |
| Disparar (se puede mantener) | Espacio |
| Jugar otra vez | Espacio |
| Salir | Esc o cerrar la ventana |

## Qué vas a practicar

En este proyecto vas a manejar muchos objetos a la vez con grupos de
sprites: drones, disparos tuyos y disparos enemigos. `groupcollide()`
compara dos grupos completos y devuelve un diccionario con lo que chocó, y
con sus dos últimos valores decides si se borra lo de cada grupo. Así, con
una sola línea, cada disparo que toca un dron desaparece junto con él.

Puedes mantener Espacio para disparar, pero un tiempo de espera (cooldown)
decide cada cuánto sale un disparo: sin él saldrían 60 por segundo. Los
drones disparan al azar con una probabilidad por segundo que se multiplica
por el delta time. Las figuras de cada oleada están escritas como listas de
textos, donde una `X` marca la posición de cada dron.

Símbolos y sintaxis nuevos: `pygame.sprite.groupcollide()`,
`pygame.sprite.GroupSingle`, el método `sprites()` de los grupos,
`draw.ellipse()`, `random.random()` y el tiempo de espera entre disparos.
