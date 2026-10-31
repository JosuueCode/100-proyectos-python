# 049 Registro de gastos en CSV

Un programa para llevar el registro de tus gastos. Cada gasto guarda la fecha,
la categoría y el monto en un archivo `gastos.csv`. Cuando quieras, te muestra
todos tus gastos, cuánto llevas gastado en cada categoría y el total general.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

El archivo `gastos.csv` se crea en la carpeta desde donde ejecutas el
programa. Puedes abrirlo con Excel o con cualquier hoja de cálculo. Está en el
`.gitignore` de este proyecto para que tus gastos no se suban al repositorio.

## Qué vas a practicar

En este proyecto vas a guardar datos con estructura. En el proyecto 048 cada
línea del archivo era una nota suelta; aquí cada línea es un registro con tres
columnas, y el módulo `csv` se encarga de separarlas por ti. Al escribir le
das un diccionario, y al leer te devuelve un diccionario por cada línea.

Para el total por categoría usas otro diccionario, igual que en el contador
de palabras del proyecto 044: la categoría es la clave y el total es el valor.

Símbolos y sintaxis nuevos: el módulo `csv` con `DictWriter`, `writeheader()`
y `writerow()` para escribir, `DictReader` para leer, el argumento
`fieldnames` para indicar las columnas y `newline=""` al abrir un archivo CSV.
