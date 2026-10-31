# 048 Bloc de notas

Un bloc de notas en la terminal. Escribes notas, las ves numeradas y puedes
borrarlas todas cuando quieras. Las notas se guardan en un archivo
`notas.txt`, así que siguen ahí aunque cierres el programa y lo vuelvas a
abrir.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

El archivo `notas.txt` se crea en la carpeta desde donde ejecutas el programa.
Está en el `.gitignore` de este proyecto para que tus notas no se suban al
repositorio.

## Qué vas a practicar

Hasta ahora todo lo que guardabas se perdía al cerrar el programa. En este
proyecto vas a leer y escribir un archivo de texto, así que los datos
sobreviven entre una ejecución y otra.

Vas a usar tres modos de apertura: `"a"` para agregar al final, `"r"` para
leer y `"w"` para escribir desde cero, que borra lo anterior. También vas a
manejar el caso en que el archivo todavía no existe con `FileNotFoundError`,
usando lo que viste en el proyecto 047.

Símbolos y sintaxis nuevos: `open()` con sus modos `"r"`, `"w"` y `"a"` y el
argumento `encoding="utf-8"`, `with ... as` para abrir y cerrar el archivo,
los métodos `write()` y `readlines()`, la secuencia de escape `\n` para el
salto de línea, el error `FileNotFoundError` y `return` sin valor.
