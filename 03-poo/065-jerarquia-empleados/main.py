"""Proyecto 065: Jerarquía de empleados.

Una empresa con empleados, desarrolladores y gerentes. Algunos puestos
reciben un bono, que se agrega con una clase mixin y herencia múltiple.
"""


class Empleado:
    """Empleado con nombre y sueldo base mensual."""

    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        """Devuelve el sueldo del mes: para un empleado, su sueldo base."""
        return self.sueldo_base

    def puesto(self):
        """Devuelve el nombre del puesto."""
        return "Empleado"

    def mostrar_recibo(self):
        """Muestra el nombre, el puesto y el sueldo en columnas."""
        sueldo = self.calcular_sueldo()
        print(f"{self.nombre:<10} {self.puesto():<26} ${sueldo:>10.2f}")


# Un mixin es una clase pequeña que no representa nada por sí sola: solo
# aporta una habilidad que se mezcla con otras clases. Esta agrega un bono
# a cualquier clase que tenga calcular_sueldo(). No se usa sola, siempre se
# combina con una clase de la jerarquía de Empleado.
class BonoMixin:
    """Agrega un bono, como porcentaje del sueldo base, al sueldo."""

    porcentaje_bono = 0

    def calcular_bono(self):
        """Devuelve el bono según el porcentaje de la clase."""
        return self.sueldo_base * self.porcentaje_bono / 100

    def calcular_sueldo(self):
        """Devuelve el sueldo de la otra clase padre más el bono."""
        # Aquí super() no llama a la clase padre de BonoMixin, porque no
        # tiene. Llama a la siguiente clase en el MRO del objeto: en un
        # Gerente, esa clase es Empleado.
        return super().calcular_sueldo() + self.calcular_bono()


class Desarrollador(Empleado):
    """Empleado que programa en un lenguaje principal."""

    def __init__(self, nombre, sueldo_base, lenguaje):
        super().__init__(nombre, sueldo_base)
        self.lenguaje = lenguaje

    def puesto(self):
        """Devuelve el puesto con el lenguaje que usa."""
        return f"Desarrollador {self.lenguaje}"


# La herencia múltiple es heredar de varias clases a la vez, separándolas
# con comas. Gerente recibe calcular_bono() de BonoMixin y todo lo demás de
# Empleado. El mixin va primero para que su calcular_sueldo() se use antes
# que el de Empleado.
class Gerente(BonoMixin, Empleado):
    """Empleado que dirige un área y recibe un bono del 20 %."""

    porcentaje_bono = 20

    def __init__(self, nombre, sueldo_base, area):
        super().__init__(nombre, sueldo_base)
        self.area = area

    def puesto(self):
        """Devuelve el puesto con el área que dirige."""
        return f"Gerente de {self.area}"


class DesarrolladorSenior(BonoMixin, Desarrollador):
    """Desarrollador con experiencia que recibe un bono del 10 %."""

    porcentaje_bono = 10

    def puesto(self):
        """Devuelve el puesto con el lenguaje que usa."""
        return f"Desarrollador senior {self.lenguaje}"


def mostrar_mro(clase):
    """Muestra en qué orden busca Python los métodos de una clase."""
    # El MRO (method resolution order, orden de resolución de métodos) es
    # la lista de clases que Python revisa, en orden, para encontrar un
    # método. clase.mro() la devuelve. Al final siempre aparece object, la
    # clase de la que heredan todas las clases de Python.
    nombres = []
    for clase_padre in clase.mro():
        nombres.append(clase_padre.__name__)
    print(f"{clase.__name__}: {' -> '.join(nombres)}")


def main():
    """Muestra el MRO de las clases y calcula la nómina del mes."""
    print("Orden de resolución de métodos:")
    mostrar_mro(Gerente)
    mostrar_mro(DesarrolladorSenior)
    print()

    nomina = [
        Empleado("Ana", 14000),
        Desarrollador("Luis", 22000, "Python"),
        DesarrolladorSenior("Marta", 32000, "Java"),
        Gerente("Carlos", 40000, "Ventas"),
        Desarrollador("Sofía", 24000, "JavaScript"),
    ]

    print(f"{'Nombre':<10} {'Puesto':<26} {'Sueldo':>11}")
    total = 0
    # Polimorfismo: el for llama a los mismos métodos en todos y cada
    # objeto usa su versión, con bono o sin él
    for empleado in nomina:
        empleado.mostrar_recibo()
        total = total + empleado.calcular_sueldo()

    print()
    print(f"Total de la nómina: ${total:.2f}")

    # isinstance() también reconoce a las clases de la herencia múltiple
    con_bono = []
    for empleado in nomina:
        if isinstance(empleado, BonoMixin):
            con_bono.append(empleado.nombre)
    print(f"Reciben bono: {', '.join(con_bono)}")


if __name__ == "__main__":
    main()
