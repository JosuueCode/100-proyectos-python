# 029 Detector de palíndromos

Un programa que te dice si una palabra o frase es un palíndromo, es decir, si
se lee igual al derecho y al revés, como "Oso" o "Anita lava la tina". No toma
en cuenta las mayúsculas ni los espacios, y puedes probar todas las frases que
quieras hasta dejar el texto vacío.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a juntar lo que viste en los dos anteriores: primero
limpias el texto con métodos de str y después lo inviertes con slicing para
compararlo consigo mismo.

Ten en cuenta que los acentos pueden afectar la comparación. Para Python, "ó"
y "o" son caracteres distintos, así que "Amó la paloma" no sale como
palíndromo aunque al leerlo sí lo parezca. Lo mismo pasa con las comas y los
puntos, porque el programa solo quita los espacios.

Símbolos y sintaxis nuevos: encadenar métodos, como
`frase.lower().replace(" ", "")`, donde cada método trabaja sobre el
resultado del anterior.
