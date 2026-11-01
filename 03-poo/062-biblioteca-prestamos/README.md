# 062 Biblioteca con préstamos

Un programa que lleva los préstamos de una biblioteca. Se agregan libros al
catálogo, dos usuarios piden y devuelven libros, y la biblioteca revisa cada
préstamo: que el libro exista, que esté disponible y que el usuario no tenga
ya dos libros. Al final ves qué tiene cada usuario y el estado del catálogo.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a ver dos formas de relacionar objetos. La biblioteca
crea sus libros con `agregar_libro()` y los guarda: los libros son parte de
ella, y eso es composición, como los renglones del carrito del proyecto 061.
Los usuarios, en cambio, se crean por separado y solo se relacionan con la
biblioteca cuando piden un libro: eso es una asociación. En una asociación
cada objeto vive por su cuenta.

Fíjate también en que el libro que tiene un usuario es el mismo objeto que
está en el catálogo. Por eso, al prestarlo, el cambio de `disponible` se ve
en los dos lugares.

Símbolos y sintaxis nuevos: la asociación entre objetos, frente a la
composición, y las validaciones encadenadas que devuelven `False` en cuanto
algo no se cumple.
