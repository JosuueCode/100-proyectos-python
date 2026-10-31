# 044 Contador de palabras

Un programa que te pide un texto y te dice cuántas veces aparece cada palabra,
cuántas palabras tiene en total, cuántas son distintas y cuál es la más
frecuente. No distingue mayúsculas de minúsculas y quita los signos de
puntuación, así que "Hola," y "hola" cuentan como la misma palabra.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a juntar texto, listas y diccionarios. Primero conviertes
el texto en una lista de palabras con `split()`, y después usas un diccionario
donde cada palabra es una clave y su valor es cuántas veces aparece. Para
encontrar la más frecuente recorres el diccionario con `for` y te quedas con
la mejor que has visto, la misma idea que usaste para encontrar el mayor de
tres números.

Prueba con un párrafo de un libro o una canción para ver qué palabras se
repiten más.

Símbolos y sintaxis nuevos: el método `split()` para separar un texto en una
lista de palabras, `get()` con un valor por defecto para contar, como
`conteo.get(palabra, 0) + 1`, y devolver dos valores en un `return`, como
`return mas_frecuente, mayor_cantidad`.
