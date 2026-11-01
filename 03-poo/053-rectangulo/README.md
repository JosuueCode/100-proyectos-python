# 053 Clase Rectángulo

Un programa que crea varios rectángulos y, de cada uno, te muestra su área, su
perímetro y si es un cuadrado. Cada rectángulo revisa sus medidas al crearse:
si alguna es cero o negativa, avisa y queda marcado como no válido.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a ver la diferencia entre la programación estructurada y
la orientada a objetos. En el proyecto 008 el área del rectángulo era una
operación suelta: pedías la base y la altura, multiplicabas y mostrabas el
resultado. Los datos y el cálculo vivían separados, y para un segundo
rectángulo tenías que repetir todo.

Aquí el rectángulo es un objeto que guarda sus propias medidas y sabe hacer
sus cálculos. Puedes crear todos los que quieras, meterlos en una lista y
pedirle a cada uno su área, sin repetir la fórmula. Y como la validación vive
en `__init__`, ningún rectángulo empieza con medidas imposibles.

No hay símbolos nuevos, pero vas a ver que un método puede llamar a otros del
mismo objeto con `self`, como `self.area()` dentro de `describir()`.
