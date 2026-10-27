# 030 Contador de vocales

Un programa que te pide un texto y cuenta cuántas veces aparece cada vocal, sin
importar si está en mayúscula o en minúscula, ni si lleva acento. Al final te
dice cuántas vocales tiene tu texto en total.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a recorrer un texto letra por letra con `for`, igual que
antes recorrías los números de un `range()`. También vas a usar `in` como
operador para saber si una letra está dentro de otro texto, y un contador por
cada vocal.

Prueba con una frase como "Murciélago ágil en el pingüino" para ver que las
vocales con acento o con diéresis también se cuentan.

Símbolos y sintaxis nuevos: `for` sobre un str, como `for letra in texto:`, y
el operador de pertenencia `in`, como `letra in "aá"`, que da `True` o
`False`.
