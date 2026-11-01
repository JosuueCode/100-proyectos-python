"""Proyecto 059: Animales y sonidos.

Varias clases de animales con el mismo método hacer_sonido(). Un solo ciclo
for los recorre a todos y cada uno responde a su manera.
"""


class Animal:
    """Animal con nombre. Cada tipo de animal define su propio sonido."""

    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        """Devuelve el sonido del animal."""
        return "..."

    def presentarse(self):
        """Muestra el nombre del animal y su sonido."""
        print(f"{self.nombre} dice: {self.hacer_sonido()}")


class Perro(Animal):
    """Animal que ladra."""

    def hacer_sonido(self):
        """Devuelve el ladrido del perro."""
        return "Guau"


class Gato(Animal):
    """Animal que maúlla."""

    def hacer_sonido(self):
        """Devuelve el maullido del gato."""
        return "Miau"


class Vaca(Animal):
    """Animal que muge."""

    def hacer_sonido(self):
        """Devuelve el mugido de la vaca."""
        return "Muuu"


class Pato(Animal):
    """Animal que grazna."""

    def hacer_sonido(self):
        """Devuelve el graznido del pato."""
        return "Cuac"


# Esta clase no hereda de Animal, pero también tiene hacer_sonido() y
# presentarse(). Python no revisa de qué clase es un objeto antes de llamar
# a un método: solo le importa que el método exista. A esto se le llama
# duck typing: "si camina como pato y hace cuac como pato, es un pato".
class Robot:
    """Juguete que imita sonidos, sin ser un animal."""

    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        """Devuelve el sonido del robot."""
        return "Bip bup"

    def presentarse(self):
        """Muestra el nombre del robot y su sonido."""
        print(f"{self.nombre} dice: {self.hacer_sonido()}")


def main():
    """Recorre una lista mezclada y hace que todos se presenten."""
    granja = [
        Perro("Firulais"),
        Gato("Michi"),
        Vaca("Lola"),
        Pato("Lucas"),
        Robot("R2"),
    ]

    # El polimorfismo es que objetos de clases distintas respondan al mismo
    # método, cada uno a su manera. El for no necesita saber qué animal es
    # cada uno ni usar isinstance(): solo llama a presentarse() y cada
    # objeto usa su propio hacer_sonido().
    for habitante in granja:
        habitante.presentarse()


if __name__ == "__main__":
    main()
