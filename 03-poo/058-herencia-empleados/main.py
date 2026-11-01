"""Proyecto 058: Empleados y sueldos.

Una clase base Empleado y dos clases hijas, Gerente y Practicante, que
calculan su sueldo mensual de forma distinta.
"""

PORCENTAJE_PRACTICANTE = 60


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
        """Muestra el nombre, el puesto y el sueldo del mes."""
        # Aunque este método está en Empleado, self.calcular_sueldo() llama
        # a la versión de la clase del objeto. Un gerente usa la suya.
        sueldo = self.calcular_sueldo()
        # :<10 alinea el texto a la izquierda en un espacio de 10 caracteres
        # y :>10.2f alinea el número a la derecha con dos decimales. Así las
        # columnas quedan derechas aunque los nombres midan distinto.
        print(f"{self.nombre:<10} {self.puesto():<12} ${sueldo:>10.2f}")


class Gerente(Empleado):
    """Empleado que recibe un bono mensual además de su sueldo base."""

    def __init__(self, nombre, sueldo_base, bono):
        super().__init__(nombre, sueldo_base)
        self.bono = bono

    # Sobrescribir un método es volver a definirlo en la clase hija con el
    # mismo nombre. Python usa esta versión para los gerentes en lugar de
    # la de Empleado. Aquí super() reutiliza el cálculo del padre y solo
    # le suma el bono, así no se repite la lógica.
    def calcular_sueldo(self):
        """Devuelve el sueldo base más el bono."""
        return super().calcular_sueldo() + self.bono

    def puesto(self):
        """Devuelve el nombre del puesto."""
        return "Gerente"


class Practicante(Empleado):
    """Empleado que recibe una parte del sueldo base como apoyo."""

    # Aquí no tiene sentido usar super(): el practicante no recibe el
    # sueldo base completo, sino un porcentaje, así que la versión nueva
    # reemplaza por completo a la del padre
    def calcular_sueldo(self):
        """Devuelve el porcentaje del sueldo base que le toca."""
        return self.sueldo_base * PORCENTAJE_PRACTICANTE / 100

    def puesto(self):
        """Devuelve el nombre del puesto."""
        return "Practicante"


def main():
    """Muestra la nómina del mes con el sueldo de cada empleado."""
    nomina = [
        Empleado("Ana", 15000),
        Gerente("Carlos", 25000, 8000),
        Practicante("Luis", 10000),
        Empleado("Sofía", 16500),
    ]

    # Entre las llaves también puede ir un texto fijo, para alinear los
    # títulos de las columnas con el mismo formato que los datos
    print(f"{'Nombre':<10} {'Puesto':<12} {'Sueldo':>11}")
    total = 0
    for empleado in nomina:
        empleado.mostrar_recibo()
        total = total + empleado.calcular_sueldo()

    print()
    print(f"Total de la nómina: ${total:.2f}")


if __name__ == "__main__":
    main()
