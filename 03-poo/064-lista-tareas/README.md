# 064 Lista de tareas

Un programa que administra una lista de tareas. Cada tarea tiene un título,
una prioridad (1 alta, 2 media, 3 baja) y una casilla que se marca al
completarla. El programa agrega tareas, rechaza las que no son válidas,
completa y elimina por número, muestra las pendientes y ordena la lista de la
más urgente a la menos urgente.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a ordenar objetos. En el proyecto 042 usaste `sorted()`
con números y textos, que Python ya sabe comparar. Con objetos `Tarea` no
sabe qué comparar, así que le dices cómo con el parámetro `key`: una función
que recibe cada tarea y devuelve su prioridad.

Esa función la vas a escribir con `lambda`, una función anónima: no tiene
nombre, cabe en una línea y devuelve el resultado de su expresión sin
escribir `return`. `lambda tarea: tarea.prioridad` hace lo mismo que un `def`
de dos líneas. Conviene usarla para funciones muy cortas que solo se usan en
un lugar, como el `key` de `sorted()`. Si la función hace más de una cosa,
es mejor escribirla con `def` y darle un nombre.

Símbolos y sintaxis nuevos: `lambda` para crear funciones anónimas y el
parámetro `key` de `sorted()`.
