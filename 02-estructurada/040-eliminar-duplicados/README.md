# 040 Eliminar duplicados

Un programa que te pide palabras, algunas repetidas, hasta que dejas el texto
vacío. Después te muestra la lista sin repetidos de dos formas distintas y te
dice cuántas palabras se quitaron.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a conocer el set, una colección que no admite repetidos,
y a compararlo con una solución hecha a mano.

La primera forma convierte la lista en un set y luego de vuelta en lista. Es
la más corta, pero pierde el orden: un set no guarda posiciones, así que las
palabras salen en cualquier orden, y ese orden puede cambiar cada vez que
ejecutas el programa. Pruébalo dos veces con las mismas palabras.

La segunda forma recorre la lista con `for` y agrega cada palabra a una lista
nueva solo si todavía no está. Es un poco más larga, pero conserva el orden en
que escribiste las palabras. Usa el set cuando el orden no importe y el `for`
cuando sí.

Símbolos y sintaxis nuevos: `set()` para crear un set a partir de una lista,
`list()` para convertirlo de nuevo en lista, el operador lógico `not` y su uso
con `in`, como `elemento not in sin_repetir`.
