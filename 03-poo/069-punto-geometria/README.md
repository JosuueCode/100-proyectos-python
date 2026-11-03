# 069 Puntos y distancias

Un programa con una clase `Punto` para trabajar en el plano. Suma y resta
puntos con `+` y `-`, mide la distancia entre dos puntos y, con eso, calcula
el perímetro de un triángulo a partir de sus tres vértices. El ejemplo usa el
triángulo de lados 3, 4 y 5.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a crear una clase con el decorador `@dataclass`. En
lugar de escribir `__init__`, solo declaras los atributos con su tipo, como
`x: float = 0`, y el decorador genera tres métodos por ti:

- `__init__`, que recibe los atributos en el orden en que los declaraste.
- `__repr__`, que muestra el objeto como `Punto(x=3, y=4)`.
- `__eq__`, que compara los atributos uno por uno con `==`.

Lo que no genera, como la suma o la distancia, lo escribes tú. La distancia
usa el teorema de Pitágoras con `math.sqrt()`, que conociste en el proyecto
060.

Símbolos y sintaxis nuevos: el módulo `dataclasses`, el decorador
`@dataclass` y las anotaciones de tipo en atributos, como `x: float = 0`.
