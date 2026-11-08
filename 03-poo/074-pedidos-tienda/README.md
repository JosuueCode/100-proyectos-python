# 074 Tienda en línea con pedidos

Un programa que simula una tienda en línea de accesorios de computadora. Dos
clientes arman pedidos, la tienda aparta las piezas del inventario y cada
pedido pasa por sus estados: pendiente, pagado, enviado y entregado, o
cancelado. Al final ves el detalle de un pedido con el IVA del 16 % y las
existencias que quedan. En el camino aparecen errores a propósito: pedir más
piezas de las que hay, un código que no existe o enviar algo sin pagar.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a escribir anotaciones de tipo (type hints) en los
parámetros y en lo que devuelven los métodos, como
`def retirar(self, codigo: str, cantidad: int)` o `def total(self) -> float`.
En el proyecto 069 ya las usaste en los atributos de un `@dataclass`; aquí
las ves en todo el programa, también en colecciones como `list[Pedido]` o
`dict[str, int]`.

Las anotaciones documentan el código: al leer una función sabes qué le
tienes que pasar, y editores como VS Code te avisan si te equivocas. Pero
Python no las obliga. Si pasas un texto donde dice `int`, el programa se
ejecuta igual y el error aparece después, o no aparece.

También vas a combinar lo que viste en la etapa: `Enum` para los estados del
pedido, `@dataclass` para las clases que solo guardan datos y una jerarquía
de excepciones propias, con `StockInsuficienteError` cuando no alcanzan las
existencias.

Símbolos y sintaxis nuevos: las anotaciones de tipo en parámetros, como
`cantidad: int`, en el valor de retorno con `->`, como `-> float`, y en
colecciones, como `list[Pedido]` y `dict[str, int]`. También una `lambda`
sin parámetros para guardar una llamada y ejecutarla después.
