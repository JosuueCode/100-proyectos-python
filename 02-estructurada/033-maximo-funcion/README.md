# 033 Máximo con función

Un programa que te pide tres números y te dice cuál es el mayor de los dos
primeros y cuál es el mayor de los tres. Para lograrlo usa una función propia
que compara dos números, y la reutiliza para comparar tres.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a escribir tus primeras funciones. Vas a ver la
diferencia entre definir una función, que solo le dice a Python qué hacer, y
llamarla, que es cuando de verdad se ejecuta. También vas a notar que `return`
entrega un valor para seguir usándolo, mientras que `print()` solo lo muestra
en pantalla.

Fíjate en que `mayor_de_tres` no repite la comparación: llama dos veces a
`mayor_de_dos`. Esa es la gran ventaja de las funciones, escribir una idea una
sola vez y usarla donde la necesites.

Símbolos y sintaxis nuevos: `def` para definir una función, los parámetros
entre paréntesis, como `def mayor_de_dos(primero, segundo):`, `return` para
devolver un valor y el docstring de una función, como
`"""Devuelve el mayor de dos números."""`.
