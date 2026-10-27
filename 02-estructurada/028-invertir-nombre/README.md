# 028 Invertir nombre

Un programa que te pide tu nombre y lo recorta de varias formas: te muestra la
primera letra, la última, las primeras tres, el nombre desde la segunda letra,
una letra sí y otra no, y al final tu nombre al revés.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a ver que cada letra de un texto tiene una posición, y
que puedes tomar una sola letra o un pedazo completo usando esas posiciones.
Fíjate en que los índices empiezan en 0 y en que el fin de un slicing no se
incluye, porque son los dos detalles que más confunden al principio.

Prueba con tu nombre completo o con un nombre de dos letras para ver qué pasa
cuando el pedazo pedido es más largo que el texto.

Símbolos y sintaxis nuevos: los corchetes `[]` para tomar un carácter por su
índice, como `nombre[0]`, los índices negativos, como `nombre[-1]`, y el
slicing `[inicio:fin:paso]`, como `nombre[0:3]`, `nombre[1:]`, `nombre[::2]`
y `nombre[::-1]` para invertir un texto.
