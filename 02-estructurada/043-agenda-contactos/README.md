# 043 Agenda de contactos

Una agenda con menú para guardar los teléfonos de tus contactos. Puedes
agregar un contacto, buscarlo por nombre, cambiar su teléfono, eliminarlo y
ver todos en orden alfabético. No importa si escribes el nombre con
mayúsculas o minúsculas: "ana" y "ANA" son el mismo contacto.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a usar tu primer diccionario. A diferencia de una lista,
donde buscas un elemento por su posición, en un diccionario lo buscas por su
clave: escribes el nombre y obtienes el teléfono directo, sin recorrer nada.

Fíjate en las dos formas de leer un valor: `agenda[nombre]` marca un error si
el nombre no existe, mientras que `agenda.get(nombre, "")` te devuelve un
valor por defecto. Los contactos se pierden al cerrar el programa; en el
proyecto 048 vas a ver cómo guardar datos en un archivo.

Símbolos y sintaxis nuevos: los diccionarios con llaves, como `{}` o
`{"Ana": "555-1234"}`, el acceso por clave `agenda[nombre]`, el método
`get()`, `del` para borrar una clave, `in` para revisar si una clave existe y
`items()` para recorrer los pares clave y valor.
