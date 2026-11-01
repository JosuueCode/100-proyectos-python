# 051 Clase Persona

Un programa que crea tres personas, cada una con su nombre, edad y ciudad, y
hace que se presenten. Después una de ellas cumple años y el programa revisa
quiénes son mayores de edad.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

Con este proyecto empieza la etapa de programación orientada a objetos. Vas a
escribir tu primera clase, que es un molde, y a crear objetos a partir de ella,
que son las personas concretas. Cada objeto guarda sus propios datos, llamados
atributos, y sabe hacer cosas con ellos a través de sus métodos.

Fíjate en `self`: dentro de un método representa al objeto que lo está usando.
Cuando escribes `ana.presentarse()`, `self` es Ana; cuando escribes
`luis.presentarse()`, `self` es Luis. Así el mismo código sirve para todas las
personas.

Símbolos y sintaxis nuevos: `class` para definir una clase, el método especial
`__init__`, el parámetro `self`, los atributos como `self.nombre`, los
métodos definidos dentro de la clase y la creación de un objeto, como
`Persona("Ana", 28, "Guadalajara")`.
