# 045 Ahorcado

El juego del ahorcado contra la computadora. Ella elige una palabra al azar y
tú tienes que adivinarla letra por letra. Cada letra que no está te quita una
vida; si completas la palabra antes de quedarte sin las seis vidas, ganas.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a juntar casi todo lo que llevas de la etapa: una lista
de palabras, `random` para elegir una, una lista para recordar las letras que
ya usaste y funciones pequeñas para mostrar la palabra, revisar si está
completa y validar cada letra.

Las palabras están escritas sin acentos para que no tengas que adivinar si la
"o" lleva tilde. Si quieres, agrega tus propias palabras a la lista
`PALABRAS`.

Símbolos y sintaxis nuevos: `random.choice()` para elegir un elemento al azar
de una lista, el método `join()` para unir una lista de textos, como
`" ".join(partes)`, y una lista escrita en varias líneas.
