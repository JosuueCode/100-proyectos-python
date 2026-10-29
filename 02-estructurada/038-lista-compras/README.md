# 038 Lista de compras

Un programa con menú para armar tu lista de compras. Puedes agregar productos,
quitarlos, ver la lista numerada y vaciarla cuando termines. No deja agregar
productos vacíos ni repetidos, aunque los escribas con mayúsculas distintas.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a usar tu primera lista, una variable que guarda varios
valores en orden. Vas a ver que una lista sí se puede modificar, así que las
funciones pueden agregarle o quitarle elementos directamente. También vas a
mostrarla numerada sin llevar un contador a mano.

Fíjate en que antes de quitar un producto el programa revisa que esté en la
lista: si intentas quitar algo que no está, Python marca un error.

Símbolos y sintaxis nuevos: las listas con corchetes, como `[]` o
`["leche", "pan"]`, los métodos `append()`, `remove()` y `clear()`, `len()`
y el operador `in` con listas, y `enumerate()` para recorrer una lista con su
posición, como `for numero, producto in enumerate(lista, 1):`.
