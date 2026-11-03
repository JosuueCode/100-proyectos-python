"""Proyecto 069: Puntos y distancias.

Una clase Punto creada con @dataclass que suma y resta puntos, mide la
distancia entre ellos y calcula el perímetro de un triángulo.
"""

import math

# dataclasses es un módulo de la biblioteca estándar para crear clases que
# sobre todo guardan datos, escribiendo mucho menos código
from dataclasses import dataclass


# @dataclass lee los atributos declarados en la clase y genera solo tres
# métodos: __init__, que recibe x y y en ese orden; __repr__, que muestra
# Punto(x=1, y=2); y __eq__, que compara los atributos uno por uno. Sin el
# decorador habría que escribir esos tres métodos a mano.
@dataclass
class Punto:
    """Punto del plano con coordenadas x y y."""

    # Cada atributo se declara con su nombre, dos puntos y su tipo. Esto se
    # llama anotación de tipo: indica qué tipo de dato se espera, aunque
    # Python no lo obliga. El = 0 es el valor si no se da ninguno.
    x: float = 0
    y: float = 0

    # El @dataclass no genera operaciones como la suma: estas se escriben
    # igual que en el proyecto 067
    def __add__(self, otro):
        """Devuelve un punto con las coordenadas sumadas."""
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        """Devuelve un punto con las coordenadas restadas."""
        return Punto(self.x - otro.x, self.y - otro.y)

    def distancia_a(self, otro):
        """Devuelve la distancia en línea recta hasta otro punto."""
        # Teorema de Pitágoras: la resta da cuánto se avanza en x y en y, y
        # la distancia es la raíz de la suma de sus cuadrados
        diferencia = self - otro
        return math.sqrt(diferencia.x ** 2 + diferencia.y ** 2)


def perimetro_triangulo(a, b, c):
    """Devuelve el perímetro del triángulo con vértices en a, b y c."""
    return a.distancia_a(b) + b.distancia_a(c) + c.distancia_a(a)


def main():
    """Opera con puntos y mide un triángulo."""
    a = Punto(0, 0)
    b = Punto(3, 0)
    c = Punto(3, 4)
    origen = Punto()

    # print() usa el __repr__ que generó @dataclass
    print(f"A = {a}")
    print(f"B = {b}")
    print(f"C = {c}")
    print(f"Punto sin datos: {origen}")
    print()

    print(f"B + C = {b + c}")
    print(f"C - B = {c - b}")
    # El __eq__ generado compara x y y, no si son el mismo objeto
    print(f"¿A es igual al origen? {a == origen}")
    print(f"¿A es igual a B? {a == b}")
    print()

    print(f"Distancia de A a B: {a.distancia_a(b):.2f}")
    print(f"Distancia de B a C: {b.distancia_a(c):.2f}")
    print(f"Distancia de C a A: {c.distancia_a(a):.2f}")
    perimetro = perimetro_triangulo(a, b, c)
    print(f"Perímetro del triángulo ABC: {perimetro:.2f}")


if __name__ == "__main__":
    main()
