"""Proyecto 056: Estudiante y calificaciones.

Cada estudiante guarda sus calificaciones en una lista, calcula su promedio
y sabe si aprueba. El programa muestra al estudiante con mejor promedio.
"""

NOTA_MINIMA = 0
NOTA_MAXIMA = 10
NOTA_APROBATORIA = 6


class Estudiante:
    """Estudiante con nombre y una lista de calificaciones."""

    def __init__(self, nombre):
        self.nombre = nombre
        # Un atributo puede ser una lista. Se crea aquí, dentro de __init__,
        # para que cada estudiante tenga la suya. Si fuera un atributo de
        # clase, como en el proyecto 054, todos compartirían la misma lista
        # y las calificaciones de uno aparecerían en los demás.
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        """Agrega la calificación si es válida. Devuelve True si se agregó."""
        if NOTA_MINIMA <= calificacion <= NOTA_MAXIMA:
            self.calificaciones.append(calificacion)
            return True
        print(f"{calificacion} no es válida para {self.nombre}.")
        return False

    def promedio(self):
        """Devuelve el promedio de las calificaciones, o 0 si no hay."""
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def aprueba(self):
        """Devuelve True si el promedio es aprobatorio."""
        return self.promedio() >= NOTA_APROBATORIA

    def __str__(self):
        """Devuelve el nombre, las calificaciones y el promedio."""
        promedio = self.promedio()
        return f"{self.nombre} {self.calificaciones}, promedio {promedio:.2f}"


def buscar_mejor(estudiantes):
    """Devuelve el estudiante con el promedio más alto."""
    mejor = estudiantes[0]
    for estudiante in estudiantes:
        if estudiante.promedio() > mejor.promedio():
            mejor = estudiante
    return mejor


def main():
    """Crea un grupo, le asigna calificaciones y muestra los resultados."""
    ana = Estudiante("Ana")
    luis = Estudiante("Luis")
    sofia = Estudiante("Sofía")

    for calificacion in [9, 8.5, 10]:
        ana.agregar_calificacion(calificacion)
    for calificacion in [5, 6, 4.5, 11]:
        luis.agregar_calificacion(calificacion)
    for calificacion in [7, 9.5, 8]:
        sofia.agregar_calificacion(calificacion)
    print()

    # Una lista puede guardar objetos, y cada uno conserva sus atributos
    grupo = [ana, luis, sofia]

    for estudiante in grupo:
        if estudiante.aprueba():
            resultado = "aprueba"
        else:
            resultado = "no aprueba"
        # print() usa el __str__ del estudiante, como en el proyecto 055
        print(f"{estudiante}, {resultado}")

    mejor = buscar_mejor(grupo)
    print()
    print(f"Mejor promedio: {mejor.nombre} con {mejor.promedio():.2f}")


if __name__ == "__main__":
    main()
