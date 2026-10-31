# 041 Buscador en lista

Un programa que te muestra una lista de frutas con la posición de cada una y te
deja buscar las que quieras. Para cada búsqueda te dice en qué posición está la
fruta y cuántas veces aparece, primero con una búsqueda hecha a mano y después
con las herramientas que ya trae Python.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a escribir una búsqueda lineal: revisar la lista elemento
por elemento hasta encontrar el que buscas. Es lo que hacen por dentro `in` e
`index()`, así que al compararlas vas a ver que dan el mismo resultado.

Fíjate en las diferencias: tu función devuelve -1 cuando no encuentra nada,
`in` solo responde `True` o `False`, e `index()` marca un error si el elemento
no está. Por eso conviene revisar con `in` antes de usar `index()`.

Símbolos y sintaxis nuevos: los índices en listas, como `FRUTAS[posicion]`, y
los métodos de lista `index()` y `count()`.
