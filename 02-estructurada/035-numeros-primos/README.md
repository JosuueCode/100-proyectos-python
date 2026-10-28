# 035 Números primos

Un programa que te pide un límite y te muestra todos los números primos desde
el 2 hasta ese límite, y cuántos encontró. Un número primo es el que solo se
puede dividir exacto entre 1 y entre sí mismo, como 2, 3, 5 o 7.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a escribir una función que responde con `True` o `False`
y a usarla directo como condición de un `if`. También vas a cortar un ciclo
antes de tiempo con `break`: en cuanto el programa encuentra un divisor, ya
sabe que el número no es primo y deja de revisar los que faltan.

Prueba con un límite grande, como 5000, para ver que el programa sigue
respondiendo rápido gracias a `break`.

Símbolos y sintaxis nuevos: `break` para terminar un ciclo de inmediato.
