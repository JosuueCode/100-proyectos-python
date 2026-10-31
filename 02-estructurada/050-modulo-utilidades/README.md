# 050 Módulo de utilidades

Un programa para dividir la cuenta de una comida entre varias personas, con
propina opcional. Lo interesante está en cómo se arma: las funciones para
pedir datos y mostrar dinero viven en un archivo aparte, `utilidades.py`, y
`main.py` las importa para usarlas.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

También puedes ejecutar el módulo solo, con `python utilidades.py`, para ver
qué pasa cuando no lo importas.

## Qué vas a practicar

En este proyecto vas a crear tu propio módulo. Las funciones que escribiste en
proyectos anteriores, como `pedir_entero()` del 047, ahora están en un solo
lugar y cualquier programa de la carpeta puede usarlas con
`import utilidades`, igual que usabas `random`.

También vas a conocer `__name__`, una variable que Python crea en cada
archivo. Vale `"__main__"` cuando ejecutas el archivo directamente y vale el
nombre del módulo cuando otro archivo lo importa. Por eso el bloque
`if __name__ == "__main__":` solo se ejecuta en el primer caso: así un módulo
puede tener su propia prueba sin que esta se ejecute en cada import.

Con este proyecto cierras la etapa 02-estructurada. Ya sabes organizar un
programa en funciones, guardar datos en listas y diccionarios, manejar
errores, trabajar con archivos y repartir tu código en módulos. En la
siguiente etapa, 03-poo, vas a aprender a agrupar datos y funciones en clases.

Símbolos y sintaxis nuevos: importar un módulo propio, como
`import utilidades`, la variable especial `__name__` y el bloque
`if __name__ == "__main__":` como punto de entrada del programa.
