# 016 Año bisiesto

Un programa que te pide un año y te dice si es bisiesto. Usa la regla completa
del calendario: un año es bisiesto si es divisible entre 4, pero no entre 100,
salvo que también sea divisible entre 400. Por eso 2024 y 2000 son bisiestos,
pero 1900 no.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a usar el operador módulo `%` para revisar si un número es
divisible entre otro, y a combinar varias condiciones con `and` y `or` en una
sola regla.

Símbolos y sintaxis nuevos: los paréntesis para agrupar condiciones lógicas.
Ya los usaste para agrupar operaciones aritméticas; aquí sirven para decidir
qué parte de la regla se evalúa junta.
