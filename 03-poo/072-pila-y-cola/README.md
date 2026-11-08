# 072 Pila y cola

Un programa con dos estructuras de datos clásicas y un uso para cada una. La
pila revisa si los paréntesis, corchetes y llaves de un texto están bien
cerrados. La cola simula la fila de un banco: los clientes se forman y
pasan en el mismo orden en que llegaron. Si intentas sacar algo de una pila
o una cola vacía, se lanza `EstructuraVaciaError`.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a ver dos formas de ordenar la salida de los datos. En
la pila, el último que entra es el primero que sale, como una pila de
platos. Por eso sirve para los paréntesis: cada cierre debe corresponder a
la última apertura que sigue pendiente.

En la cola, el primero que entra es el primero que sale. Podrías hacerla con
una lista y `pop(0)`, pero quitar el primer elemento obliga a Python a mover
todos los demás un lugar, y con muchos elementos eso es lento. `deque`, del
módulo `collections`, está hecha para agregar y quitar por los dos extremos
sin mover nada, así que `popleft()` siempre es rápido.

Símbolos y sintaxis nuevos: el módulo `collections` con `deque` y sus
métodos `append()` y `popleft()`, el método `pop()` de las listas y
`__len__` para que `len()` funcione con tus objetos.
