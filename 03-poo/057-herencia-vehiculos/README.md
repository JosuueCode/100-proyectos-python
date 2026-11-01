# 057 Vehículos con herencia

Un programa con autos y motos. Todos los vehículos comparten marca, modelo y
año, y saben describirse y arrancar. Además, los autos tienen puertas y
pueden abrir la cajuela, y las motos tienen cilindrada y pueden hacer
caballito.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a usar la herencia. Lo que tienen en común todos los
vehículos se escribe una sola vez en la clase `Vehiculo`, y `Auto` y `Moto`
lo heredan para agregar solo lo que las hace distintas. Si mañana quieres una
clase `Camion`, no tienes que volver a escribir la marca ni el método
`arrancar()`.

Con `super()` reutilizas el `__init__` de la clase padre, y con `isinstance()`
revisas de qué tipo es cada objeto antes de usar algo que solo tiene un auto
o una moto.

Símbolos y sintaxis nuevos: la herencia con la clase padre entre paréntesis,
como `class Auto(Vehiculo):`, la función `super()` y la función
`isinstance()`.
