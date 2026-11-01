# 055 Clase Libro

Un programa con una lista de libros que muestra cada uno de dos formas: como
una frase fácil de leer, "Pedro Páramo, de Juan Rulfo (1955)", y como el
código que crea el libro, `Libro('Pedro Páramo', 'Juan Rulfo', 1955)`.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a decidir cómo se ve tu objeto cuando lo conviertes en
texto. Sin estos métodos, `print(libro)` mostraría algo como
`<__main__.Libro object at 0x...>`, que no dice nada útil.

`__str__` es para las personas que usan el programa: lo ves con `print()` y
en los f-strings. `__repr__` es para ti como programador: lo ves con `repr()`
y cuando imprimes una lista de objetos, y te ayuda a saber exactamente qué
hay dentro de cada uno al revisar tu código.

Símbolos y sintaxis nuevos: los métodos especiales `__str__` y `__repr__`, y
la función `repr()`.
