# 077 Calculadora con interfaz

Una calculadora en ventana con botones para los dígitos, el punto decimal,
las cuatro operaciones, `=` y `C` para borrar. Puedes encadenar operaciones,
como `2 + 3 * 4 =`, que se resuelven en el orden en que las escribes, igual
que en una calculadora de bolsillo. Si divides entre cero, la pantalla
muestra `Error` y puedes seguir con un número nuevo.

## Cómo ejecutarlo

tkinter ya viene con Python, así que no necesitas instalar nada. En algunas
distribuciones de Linux viene aparte; si al ejecutar ves un error que menciona
`tkinter`, instálalo con `sudo apt install python3-tk` o el comando de tu
distribución.

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a acomodar los widgets con `grid()`, que los coloca en
una cuadrícula de filas y columnas, en lugar de uno debajo de otro como
`pack()`. Los 16 botones no se escriben uno por uno: se crean con dos ciclos
`for` que recorren una lista de filas. Cada botón usa una `lambda` en su
`command` para avisar qué tecla se pulsó.

Las operaciones se resuelven con una función propia. Existe `eval()`, que
ejecuta un texto como si fuera código, pero es inseguro: si ese texto viene
del usuario, podría ejecutar cualquier instrucción. Resolverlo tú mismo es
más seguro y te deja controlar errores como la división entre cero.

Símbolos y sintaxis nuevos: `grid()` con `row`, `column`, `columnspan` y
`sticky`, los valores por defecto en parámetros, como `texto=texto` dentro
de una `lambda`, el método `cget()` para leer una opción de un widget y
`is_integer()` de los números decimales.
