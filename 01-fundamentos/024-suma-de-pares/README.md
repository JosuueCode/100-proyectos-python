# 024 Suma de números pares

Un programa que te pide un límite y suma todos los números pares desde 2 hasta
ese límite. También te dice cuántos números pares sumó.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a usar el patrón de acumulador: una variable que empieza
en 0 y va sumando valores en cada vuelta del ciclo. Vas a compararlo con un
contador, que solo suma 1 por vuelta. También vas a recorrer solo los números
pares sin revisarlos uno por uno, haciendo que `range()` avance de dos en dos.

Símbolos y sintaxis nuevos: `range()` con un tercer valor, el paso, como
`range(2, limite + 1, 2)`.
