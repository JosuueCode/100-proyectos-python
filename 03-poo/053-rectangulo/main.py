"""Proyecto 053: Clase Rectángulo.

Define un rectángulo que valida sus medidas al crearse y sabe calcular su
área, su perímetro y si es un cuadrado.
"""


class Rectangulo:
    """Rectángulo con base y altura mayores que cero."""

    def __init__(self, base, altura):
        # La validación va en __init__ para que ningún rectángulo empiece
        # con medidas imposibles. Si alguna no sirve, el objeto se crea con
        # medidas en cero y queda marcado como no válido en el atributo
        # valido. En el proyecto 066 vas a ver una forma de impedir que el
        # objeto se cree.
        if base > 0 and altura > 0:
            self.base = base
            self.altura = altura
            self.valido = True
        else:
            print(f"Medidas no válidas: {base} x {altura}.")
            print("  Deben ser mayores que cero.")
            self.base = 0
            self.altura = 0
            self.valido = False

    def area(self):
        """Devuelve el área del rectángulo."""
        return self.base * self.altura

    def perimetro(self):
        """Devuelve el perímetro del rectángulo."""
        return 2 * (self.base + self.altura)

    def es_cuadrado(self):
        """Devuelve True si la base y la altura miden lo mismo."""
        return self.valido and self.base == self.altura

    def describir(self):
        """Muestra las medidas y los cálculos del rectángulo."""
        # Un método puede llamar a otros métodos del mismo objeto con self
        print(f"Rectángulo de {self.base} x {self.altura}")
        print(f"  Área:      {self.area()}")
        print(f"  Perímetro: {self.perimetro()}")
        if self.es_cuadrado():
            print("  Es un cuadrado.")
        else:
            print("  No es un cuadrado.")


def main():
    """Crea varios rectángulos y muestra los que tienen medidas válidas."""
    rectangulos = [
        Rectangulo(5, 3),
        Rectangulo(4, 4),
        Rectangulo(-2, 6),
        Rectangulo(2.5, 10),
    ]
    print()

    for rectangulo in rectangulos:
        if rectangulo.valido:
            rectangulo.describir()
            print()

    # Un rectángulo no válido tiene área 0, así que no cambia la suma
    areas = []
    for rectangulo in rectangulos:
        areas.append(rectangulo.area())
    print(f"Área total de los rectángulos válidos: {sum(areas)}")


if __name__ == "__main__":
    main()
