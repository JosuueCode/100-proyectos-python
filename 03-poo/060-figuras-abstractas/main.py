"""Proyecto 060: Figuras con clase abstracta.

Una clase abstracta Figura obliga a cada figura a saber calcular su área y su
perímetro. Círculo, rectángulo y triángulo cumplen ese contrato.
"""

# math es el módulo de la biblioteca estándar con funciones y constantes
# matemáticas, como math.pi y math.sqrt()
import math

# from ... import trae nombres concretos de un módulo, así se escriben sin
# el prefijo: ABC en lugar de abc.ABC. El módulo abc (abstract base
# classes) sirve para crear clases abstractas.
from abc import ABC, abstractmethod


# Una clase abstracta es un molde incompleto: define qué métodos deben
# tener sus hijas, pero no se pueden crear objetos de ella directamente.
# Para que una clase sea abstracta hereda de ABC.
class Figura(ABC):
    """Figura geométrica que sabe calcular su área y su perímetro."""

    # @abstractmethod marca un método que la clase no implementa. Cada
    # clase hija está obligada a escribirlo; si le falta alguno, Python no
    # deja crear objetos de esa clase. El cuerpo solo lleva el docstring.
    @abstractmethod
    def area(self):
        """Devuelve el área de la figura."""

    @abstractmethod
    def perimetro(self):
        """Devuelve el perímetro de la figura."""

    # Un método normal en la clase abstracta lo heredan todas las figuras.
    # Funciona porque cada una tiene su propio area() y perimetro().
    def describir(self):
        """Muestra el nombre de la figura, su área y su perímetro."""
        # type(self) devuelve la clase del objeto, y su atributo __name__ es
        # el nombre de esa clase como texto, por ejemplo "Circulo"
        nombre = type(self).__name__
        area = self.area()
        perimetro = self.perimetro()
        print(f"{nombre}: área {area:.2f}, perímetro {perimetro:.2f}")


class Circulo(Figura):
    """Círculo definido por su radio."""

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        """Devuelve pi por el radio al cuadrado."""
        return math.pi * self.radio ** 2

    def perimetro(self):
        """Devuelve la circunferencia: 2 por pi por el radio."""
        return 2 * math.pi * self.radio


class Rectangulo(Figura):
    """Rectángulo definido por su base y su altura."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        """Devuelve la base por la altura."""
        return self.base * self.altura

    def perimetro(self):
        """Devuelve la suma de los cuatro lados."""
        return 2 * (self.base + self.altura)


class Triangulo(Figura):
    """Triángulo definido por la medida de sus tres lados."""

    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def perimetro(self):
        """Devuelve la suma de los tres lados."""
        return self.lado_a + self.lado_b + self.lado_c

    def area(self):
        """Devuelve el área con la fórmula de Herón."""
        # La fórmula de Herón calcula el área solo con los lados, usando el
        # semiperímetro s. math.sqrt() devuelve la raíz cuadrada.
        s = self.perimetro() / 2
        diferencias = (s - self.lado_a) * (s - self.lado_b) * (s - self.lado_c)
        return math.sqrt(s * diferencias)


def main():
    """Crea varias figuras y muestra que Figura no se puede crear sola."""
    figuras = [
        Circulo(3),
        Rectangulo(4, 6),
        Triangulo(3, 4, 5),
    ]

    for figura in figuras:
        figura.describir()
    print()

    # Crear un objeto de una clase abstracta provoca un TypeError. Con
    # except ... as error se guarda el error en una variable para mostrar
    # el mensaje que da Python.
    try:
        Figura()
    except TypeError as error:
        print("No se puede crear una Figura sin decir qué figura es.")
        print(f"Python dice: {error}")


if __name__ == "__main__":
    main()
