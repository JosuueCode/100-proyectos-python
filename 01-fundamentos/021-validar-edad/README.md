# 021 Validar edad

Un programa que te pide tu edad y te la vuelve a pedir mientras escribas un
número fuera del rango de 0 a 120. Cuando la edad es válida, la registra y te
dice si eres mayor o menor de edad.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a repetir una parte del programa con un ciclo hasta que se
cumpla una condición. Es la forma de no dejar avanzar al programa con un dato
incorrecto.

Símbolos y sintaxis nuevos: el ciclo `while`, que repite su bloque mientras la
condición sea `True`.

El programa da por hecho que escribes un número. Si escribes letras, termina
con un error. En el proyecto 047 vas a ver cómo manejar ese caso con
`try/except`.
