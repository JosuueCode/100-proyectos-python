"""Proyecto 057: Vehículos con herencia.

Una clase base Vehiculo con lo que comparten todos los vehículos, y dos
clases hijas, Auto y Moto, que agregan sus propios datos y acciones.
"""


class Vehiculo:
    """Datos y acciones comunes a cualquier vehículo."""

    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def describir(self):
        """Muestra la marca, el modelo y el año."""
        print(f"{self.marca} {self.modelo} ({self.anio})")

    def arrancar(self):
        """Muestra que el vehículo encendió."""
        print("  Arrancó el motor.")


# La herencia permite crear una clase a partir de otra. El nombre entre
# paréntesis es la clase padre: Auto recibe todos sus atributos y métodos
# sin escribirlos de nuevo, y además puede agregar los suyos.
class Auto(Vehiculo):
    """Vehículo con un número de puertas."""

    def __init__(self, marca, modelo, anio, puertas):
        # super() da acceso a la clase padre. Aquí se llama al __init__ de
        # Vehiculo para que guarde marca, modelo y año, y después se agrega
        # el atributo propio del auto.
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    def abrir_cajuela(self):
        """Acción que solo tienen los autos."""
        print(f"  Se abrió la cajuela del {self.modelo}.")


class Moto(Vehiculo):
    """Vehículo con una cilindrada en centímetros cúbicos."""

    def __init__(self, marca, modelo, anio, cilindrada):
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada

    def hacer_caballito(self):
        """Acción que solo tienen las motos."""
        print(f"  La {self.modelo} levantó la llanta delantera.")


def main():
    """Crea autos y motos, y usa lo heredado y lo propio de cada uno."""
    vehiculos = [
        Auto("Nissan", "Versa", 2021, 4),
        Moto("Italika", "FT150", 2023, 150),
        Auto("Volkswagen", "Vento", 2019, 4),
        Moto("Yamaha", "MT-03", 2022, 321),
    ]

    for vehiculo in vehiculos:
        # describir() y arrancar() vienen de Vehiculo, así que los tienen
        # todos los objetos de la lista
        vehiculo.describir()
        vehiculo.arrancar()

        # isinstance(objeto, Clase) da True si el objeto es de esa clase o
        # de una clase hija. Sirve para usar lo que solo tiene un tipo.
        if isinstance(vehiculo, Auto):
            print(f"  Tiene {vehiculo.puertas} puertas.")
            vehiculo.abrir_cajuela()
        elif isinstance(vehiculo, Moto):
            print(f"  Tiene un motor de {vehiculo.cilindrada} cc.")
            vehiculo.hacer_caballito()
        print()

    # Un auto también es un vehículo, pero no es una moto
    versa = vehiculos[0]
    print(f"¿El Versa es un Vehiculo? {isinstance(versa, Vehiculo)}")
    print(f"¿El Versa es un Auto?     {isinstance(versa, Auto)}")
    print(f"¿El Versa es una Moto?    {isinstance(versa, Moto)}")


if __name__ == "__main__":
    main()
