# 031 Adivina el número

Un juego en el que la computadora elige un número secreto del 1 al 100 y tú
tratas de adivinarlo. Después de cada intento te da una pista: si el número
secreto es mayor o menor. Al final te dice cuántos intentos necesitaste.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a usar tu primer módulo. Los módulos de la biblioteca
estándar vienen con Python y te dan herramientas listas para usar; aquí
`random` te da un número al azar diferente en cada partida.

Intenta ganar en 7 intentos o menos: si cada vez eliges el número de en medio
del rango que queda, siempre lo logras. Si escribes algo que no es un número
entero, el programa se detiene con un error; en el proyecto 047 vas a ver
cómo evitarlo.

Símbolos y sintaxis nuevos: `import` para cargar un módulo, como
`import random`, y el punto para usar una función del módulo, como
`random.randint(1, 100)`.
