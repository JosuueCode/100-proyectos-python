# 067 Clase Matriz

Un programa con una clase `Matriz` que puedes sumar, restar, multiplicar y
comparar con los mismos operadores que usas con los números: `a + b`,
`a - b`, `a * b` y `a == b`. También lees sus números con corchetes, como
`a[1][0]`. Si dos matrices no tienen las dimensiones correctas para una
operación, la clase lanza un `ValueError` que explica por qué.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a sobrecargar operadores: decirle a Python qué hace
cada operador con objetos de tu clase. Cuando escribes `a + b`, Python llama
en realidad a `a.__add__(b)`, y lo mismo pasa con `__sub__` para `-`,
`__mul__` para `*` y `__eq__` para `==`. Los corchetes también son un método:
`a[1]` llama a `a.__getitem__(1)`.

La multiplicación es el producto de matrices, no número por número. Cada
valor del resultado sale de recorrer una fila de la primera matriz y una
columna de la segunda, multiplicando y sumando. Por eso solo se puede
multiplicar si la primera tiene tantas columnas como filas tiene la segunda,
y el resultado tiene las filas de la primera y las columnas de la segunda.

Símbolos y sintaxis nuevos: la sobrecarga de operadores con `__add__`,
`__sub__`, `__mul__` y `__eq__`, `__getitem__` para usar corchetes con un
objeto y las listas de listas, como `[[1, 2], [3, 4]]`.
