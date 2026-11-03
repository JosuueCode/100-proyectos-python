"""Proyecto 068: Clase Fecha.

Una clase Fecha que revisa que el día exista, incluido el 29 de febrero de
los años bisiestos, y que se puede comparar y ordenar como un número.
"""

# functools es un módulo de la biblioteca estándar con herramientas para
# trabajar con funciones y clases
from functools import total_ordering

MESES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
    "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]
DIAS_POR_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# @total_ordering es un decorador de clase: a partir de __eq__ y __lt__
# genera los demás métodos de comparación, __le__ (<=), __gt__ (>) y
# __ge__ (>=). Sin él habría que escribir los cinco a mano.
@total_ordering
class Fecha:
    """Fecha del calendario con día, mes y año."""

    def __init__(self, dia, mes, anio):
        if anio <= 0:
            raise ValueError(f"El año {anio} no es válido.")
        if mes < 1 or mes > 12:
            raise ValueError(f"El mes {mes} no existe.")
        maximo = Fecha.dias_del_mes(mes, anio)
        if dia < 1 or dia > maximo:
            nombre_mes = MESES[mes - 1].capitalize()
            raise ValueError(f"{nombre_mes} de {anio} no tiene día {dia}.")
        self.dia = dia
        self.mes = mes
        self.anio = anio

    @staticmethod
    def es_bisiesto(anio):
        """Devuelve True si el año es bisiesto."""
        # La misma regla del proyecto 016: divisible entre 4 pero no entre
        # 100, salvo que también lo sea entre 400
        return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

    @staticmethod
    def dias_del_mes(mes, anio):
        """Devuelve cuántos días tiene el mes en ese año."""
        if mes == 2 and Fecha.es_bisiesto(anio):
            return 29
        return DIAS_POR_MES[mes - 1]

    def como_numero(self):
        """Devuelve la fecha como un número aaaammdd, por ejemplo 20240315."""
        # Así una fecha más reciente siempre da un número mayor, y comparar
        # fechas se vuelve comparar números
        return self.anio * 10000 + self.mes * 100 + self.dia

    # __eq__ responde a == y __lt__ (less than, menor que) responde a <.
    # Con estos dos, total_ordering completa el resto.
    def __eq__(self, otra):
        """Devuelve True si las dos fechas son el mismo día."""
        if not isinstance(otra, Fecha):
            return False
        return self.como_numero() == otra.como_numero()

    def __lt__(self, otra):
        """Devuelve True si esta fecha es anterior a la otra."""
        return self.como_numero() < otra.como_numero()

    def __str__(self):
        """Devuelve la fecha escrita, por ejemplo 15 de marzo de 2024."""
        return f"{self.dia} de {MESES[self.mes - 1]} de {self.anio}"


def probar_fecha(dia, mes, anio):
    """Intenta crear una fecha y muestra si existe."""
    try:
        fecha = Fecha(dia, mes, anio)
        print(f"  {dia}/{mes}/{anio}: {fecha} existe.")
    except ValueError as error:
        print(f"  {dia}/{mes}/{anio}: {error}")


def main():
    """Valida fechas, las compara y las ordena."""
    print("Validación:")
    probar_fecha(29, 2, 2024)
    probar_fecha(29, 2, 2023)
    probar_fecha(29, 2, 1900)
    probar_fecha(29, 2, 2000)
    probar_fecha(31, 4, 2025)
    probar_fecha(10, 13, 2025)
    print()

    independencia = Fecha(16, 9, 1810)
    revolucion = Fecha(20, 11, 1910)
    otra_independencia = Fecha(16, 9, 1810)

    # Los operadores <= y > no están escritos en la clase: los generó
    # total_ordering a partir de __eq__ y __lt__
    print("Comparaciones:")
    print(f"  {independencia} < {revolucion}: {independencia < revolucion}")
    print(f"  {independencia} > {revolucion}: {independencia > revolucion}")
    son_iguales = independencia == otra_independencia
    print(f"  ¿Las dos del 16 de septiembre son iguales? {son_iguales}")
    es_menor_o_igual = independencia <= otra_independencia
    print(f"  ¿La primera es <= que la segunda? {es_menor_o_igual}")
    print()

    fechas = [
        Fecha(15, 3, 2024),
        Fecha(1, 1, 2000),
        Fecha(25, 12, 2023),
        Fecha(29, 2, 2024),
        Fecha(5, 5, 1862),
    ]

    # sorted() usa el operador < para ordenar, así que funciona con fechas
    # sin necesidad de key
    print("Ordenadas de la más antigua a la más reciente:")
    for fecha in sorted(fechas):
        print(f"  {fecha}")
    print(f"La más reciente es el {max(fechas)}.")


if __name__ == "__main__":
    main()
