# 060 Figuras con clase abstracta

Un programa con tres figuras, un círculo, un rectángulo y un triángulo, que te
muestra el área y el perímetro de cada una. Todas vienen de una clase
abstracta `Figura` que define qué debe saber calcular cualquier figura. Al
final intenta crear una `Figura` sola para mostrarte que Python no lo permite.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a escribir una clase abstracta, que funciona como un
contrato: `Figura` dice que toda figura debe tener `area()` y `perimetro()`,
pero no dice cómo calcularlos. Cada clase hija está obligada a escribirlos, y
si se le olvida alguno, Python no te deja crear objetos de ella. En el
proyecto 059 nada te obligaba a que cada animal tuviera `hacer_sonido()`;
aquí el error aparece antes de que el programa falle a medio camino.

También vas a usar el módulo `math` para tener el valor exacto de pi, en
lugar de la constante 3.1416 del proyecto 008, y su raíz cuadrada para la
fórmula de Herón del triángulo.

Símbolos y sintaxis nuevos: `from ... import`, como
`from abc import ABC, abstractmethod`, la clase `ABC`, el decorador
`@abstractmethod`, el módulo `math` con `math.pi` y `math.sqrt()`,
`type(self).__name__` para obtener el nombre de la clase, el error
`TypeError` y `except ... as error` para guardar el error en una variable.
