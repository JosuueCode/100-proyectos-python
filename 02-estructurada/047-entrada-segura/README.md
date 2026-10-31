# 047 Entrada segura

Un programa que te pide tus puntos de la temporada y cuántos partidos jugaste,
y calcula tu promedio por partido. Puedes escribir letras, decimales o dejar
el texto vacío: en lugar de cerrarse con un error, el programa te avisa y te
vuelve a preguntar. Si jugaste cero partidos, también lo maneja sin fallar.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a manejar errores con `try` y `except`. Desde el proyecto
021 venías viendo la misma limitación: si escribías algo que no era un número,
`int()` o `float()` detenían el programa. En los proyectos 021 y 031 se te
avisó que aquí lo ibas a resolver, y la función `pedir_entero()` lo hace:
intenta convertir el texto y, si no puede, te pide el dato otra vez.

También vas a ver otra forma de cuidar la división entre cero. En el proyecto
004 revisabas el divisor antes de dividir; aquí intentas la división y
atrapas el `ZeroDivisionError` si ocurre. Las dos formas son válidas.

Símbolos y sintaxis nuevos: `try` y `except` para manejar errores, los tipos
de error `ValueError` y `ZeroDivisionError`, y `while True` para un ciclo que
solo termina con `return`.
