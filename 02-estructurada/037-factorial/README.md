# 037 Factorial

Un programa que te pide un número del 0 al 100 y calcula su factorial, que es
la multiplicación de todos los enteros desde 1 hasta ese número. Por ejemplo,
el factorial de 5, que se escribe 5!, es 1 * 2 * 3 * 4 * 5 = 120. Lo calcula
de dos formas distintas y te muestra que dan el mismo resultado.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a resolver el mismo problema con dos estrategias. La
versión iterativa usa un `for` y un acumulador, como ya sabes hacer. La
versión recursiva es una función que se llama a sí misma con un número más
pequeño, hasta llegar al caso base, que es donde se detiene.

El caso base es la parte más importante de una función recursiva: sin él, la
función nunca dejaría de llamarse. Por eso el programa limita el número a 100,
porque Python solo permite cierta cantidad de llamadas pendientes a la vez.

Símbolos y sintaxis nuevos: la recursión, como
`return numero * factorial_recursivo(numero - 1)`, donde una función se llama
a sí misma.
