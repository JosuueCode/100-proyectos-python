# 042 Ordenar números

Un programa que genera una lista de ocho números al azar y la ordena de tres
formas: con `sorted()`, con un ordenamiento burbuja que te muestra cada vuelta
y con `sort()`. Cada vez que lo ejecutas, los números cambian.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a ver la diferencia entre obtener una lista nueva y
modificar la original. `sorted()` te devuelve una lista ordenada y deja la
original intacta; `sort()` ordena la misma lista y ya no puedes recuperar el
orden que tenía.

El ordenamiento burbuja te deja ver qué pasa por dentro: en cada vuelta el
número más grande que falta llega al final. Fíjate en que a veces la lista ya
está ordenada antes de la última vuelta; con `break` podrías detener el ciclo
en ese momento, como en el proyecto 035.

Símbolos y sintaxis nuevos: `sorted()`, el método `sort()`, el argumento con
nombre `reverse=True`, asignar un valor a una posición de una lista, como
`copia[posicion] = valor`, `list()` para copiar una lista, `==` para comparar
listas y `_` como nombre de una variable que no se usa.
