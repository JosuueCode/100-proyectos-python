# 061 Carrito de compras

Un programa que simula el carrito de una tienda. Agregas productos con su
cantidad, quitas los que ya no quieres, aplicas un descuento y al final ves un
ticket con el importe de cada producto, el subtotal, el descuento y el total.
Si agregas un producto que ya estaba, solo aumenta su cantidad.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a usar la composición: un objeto formado por otros
objetos. El `Carrito` no hereda de nadie, pero guarda en un diccionario sus
objetos `Renglon`, y cada renglón guarda un `Producto` y una cantidad. La
herencia se lee "un auto es un vehículo"; la composición se lee "un carrito
tiene renglones". Cada objeto hace su parte: el renglón calcula su subtotal y
el carrito suma todos los renglones.

También vas a repasar el formato de ancho fijo del proyecto 058 para que el
ticket salga en columnas, con anchos como `{nombre:<20}` y `{importe:>10.2f}`.

Símbolos y sintaxis nuevos: la composición, es decir, guardar objetos como
atributos de otro objeto, como `self.renglones` con objetos `Renglon`, y
encadenar atributos, como `renglon.producto.precio`.
