# 027 Transformador de texto

Un programa que te pide un texto y te muestra un menú para transformarlo:
pasarlo a mayúsculas o minúsculas, ponerlo en tipo título, quitarle los
espacios de los extremos, reemplazar una letra o palabra, o contar cuántas
veces aparece algo. El menú se repite hasta que eliges salir.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a usar tus primeros métodos de texto. Vas a ver que un
método no cambia el texto original, sino que devuelve uno nuevo que tienes que
guardar en otra variable. Por eso, al salir, el programa te muestra tu texto
tal como lo escribiste.

Prueba a escribir un texto con espacios al inicio y al final para ver qué hace
la opción 4, y a contar una letra en mayúscula y en minúscula para notar que
`count()` las distingue.

Símbolos y sintaxis nuevos: el punto para llamar a un método, como
`texto.upper()`, y los métodos `upper()`, `lower()`, `title()`, `strip()`,
`replace()` y `count()`.
