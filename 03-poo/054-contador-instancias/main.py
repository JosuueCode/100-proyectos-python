"""Proyecto 054: Contador de instancias.

Registra jugadores de un torneo y lleva la cuenta de cuántos se han creado
con un atributo de clase.
"""


class Jugador:
    """Jugador de un torneo con número de registro automático."""

    # Un atributo de clase se escribe dentro de la clase pero fuera de los
    # métodos. Hay uno solo, compartido por todos los objetos, a diferencia
    # de los atributos de instancia como self.nombre, que cada objeto tiene
    # por separado.
    total_creados = 0

    def __init__(self, nombre):
        # Para cambiar el atributo de clase se usa el nombre de la clase.
        # Con self.total_creados = ... se crearía un atributo nuevo solo en
        # este objeto y el contador compartido no cambiaría.
        Jugador.total_creados = Jugador.total_creados + 1
        self.nombre = nombre
        self.numero = Jugador.total_creados

    def presentarse(self):
        """Muestra el nombre y el número de registro del jugador."""
        print(f"Jugador {self.numero}: {self.nombre}")

    # @classmethod hace que el método reciba la clase, llamada cls por
    # convención, en lugar de un objeto. Sirve para trabajar con los datos
    # de la clase y se puede llamar sin haber creado ningún jugador.
    @classmethod
    def cantidad_registrada(cls):
        """Devuelve cuántos jugadores se han creado."""
        return cls.total_creados

    # @staticmethod define un método que no recibe ni self ni cls. Es una
    # función normal que se guarda dentro de la clase porque tiene que ver
    # con ella, aunque no usa sus datos.
    @staticmethod
    def es_nombre_valido(nombre):
        """Devuelve True si el nombre tiene al menos dos letras."""
        return len(nombre.strip()) >= 2


def main():
    """Registra varios jugadores y muestra el contador de la clase."""
    print(f"Jugadores al iniciar: {Jugador.cantidad_registrada()}")
    print()

    nombres = ["Ana", "L", "Carlos", "Sofía", ""]
    jugadores = []

    for nombre in nombres:
        # El método estático se llama desde la clase, antes de crear nada
        if Jugador.es_nombre_valido(nombre):
            jugadores.append(Jugador(nombre))
        else:
            print(f"'{nombre}' no es un nombre válido, no se registró.")

    print()
    for jugador in jugadores:
        jugador.presentarse()

    print()
    # El atributo de clase se lee igual desde la clase o desde un objeto,
    # porque todos lo comparten
    print(f"Jugadores registrados: {Jugador.cantidad_registrada()}")
    print(f"Visto desde el primer jugador: {jugadores[0].total_creados}")


if __name__ == "__main__":
    main()
