# 046 Inventario

Un programa para llevar el inventario de una papelería. Empieza con algunos
productos y te deja agregar productos nuevos, sumar unidades cuando llega
mercancía, registrar ventas y ver el inventario con el valor de cada producto
y el valor total.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a guardar varios datos por producto usando un
diccionario dentro de otro. El nombre del producto es la clave, y su valor es
un diccionario con el precio y la cantidad. Así cada producto lleva su
información junta y la encuentras con dos pares de corchetes, como
`inventario["lápiz"]["precio"]`.

Fíjate en que una venta no puede dejar existencias negativas: el programa
revisa antes si hay suficientes unidades. Si escribes letras donde va un
número, el programa se detiene con un error; en el siguiente proyecto vas a
resolverlo.

Símbolos y sintaxis nuevos: los diccionarios anidados, como
`{"lápiz": {"precio": 5.5, "cantidad": 20}}`, el acceso con dos claves, como
`inventario[nombre]["cantidad"]`, el método `values()` y un diccionario
escrito en varias líneas.
