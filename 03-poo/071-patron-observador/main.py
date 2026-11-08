"""Proyecto 071: Patrón observador.

Una estación meteorológica avisa a varias pantallas cada vez que cambia la
temperatura. Las pantallas se suscriben y se desuscriben cuando quieren.
"""

UMBRAL_CALOR = 35


# Un patrón de diseño es una solución conocida y probada para un problema
# que aparece una y otra vez al programar. No es código que se copia, sino
# una forma de organizar las clases.
#
# El patrón observador resuelve este problema: un objeto (el sujeto)
# cambia y otros objetos (los observadores) necesitan enterarse. Sin el
# patrón, la estación tendría que conocer cada pantalla y llamarla a mano,
# y agregar una pantalla nueva obligaría a cambiar la estación. Con el
# patrón, la estación solo guarda una lista de observadores y avisa a todos
# por igual, sin saber qué hace cada uno.
class EstacionMeteorologica:
    """Sujeto: guarda la temperatura y avisa a sus observadores."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.temperatura = 0
        self.__observadores = []

    # Cada observador es algo que se puede llamar con la temperatura: el
    # método de un objeto, como pantalla.actualizar, o una función normal.
    # En Python las funciones también son objetos, así que cualquier
    # función que reciba la temperatura sirve como observador.
    def suscribir(self, observador):
        """Agrega un observador. Lanza ValueError si ya estaba."""
        if observador in self.__observadores:
            raise ValueError("Ese observador ya está suscrito.")
        self.__observadores.append(observador)

    def desuscribir(self, observador):
        """Quita un observador. Lanza ValueError si no estaba."""
        if observador not in self.__observadores:
            raise ValueError("Ese observador no está suscrito.")
        self.__observadores.remove(observador)

    def notificar(self):
        """Llama a cada observador con la temperatura actual."""
        for observador in self.__observadores:
            observador(self.temperatura)

    def medir(self, temperatura):
        """Registra una medición nueva y avisa a todos."""
        print(f"{self.nombre} mide {temperatura} °C")
        self.temperatura = temperatura
        self.notificar()


class PantallaActual:
    """Observador que muestra la última temperatura."""

    def actualizar(self, temperatura):
        """Muestra la temperatura recibida."""
        print(f"  [Pantalla actual] Ahora: {temperatura} °C")


class PantallaEstadisticas:
    """Observador que lleva la mínima, la máxima y el promedio."""

    def __init__(self):
        self.mediciones = []

    def actualizar(self, temperatura):
        """Guarda la temperatura y muestra las estadísticas."""
        self.mediciones.append(temperatura)
        minima = min(self.mediciones)
        maxima = max(self.mediciones)
        promedio = sum(self.mediciones) / len(self.mediciones)
        resumen = f"mín {minima}, máx {maxima}, promedio {promedio:.1f}"
        print(f"  [Estadísticas] {resumen}")


class AlertaCalor:
    """Observador que solo avisa cuando hace demasiado calor."""

    def actualizar(self, temperatura):
        """Muestra una alerta si se pasa del umbral."""
        if temperatura >= UMBRAL_CALOR:
            print(f"  [Alerta] Calor extremo: {temperatura} °C")


def registrar_en_bitacora(temperatura):
    """Función usada como observador, sin ninguna clase."""
    print(f"  [Bitácora] Se registró {temperatura} °C")


def main():
    """Suscribe observadores, hace mediciones y desuscribe uno."""
    estacion = EstacionMeteorologica("Estación Centro")
    actual = PantallaActual()
    estadisticas = PantallaEstadisticas()
    alerta = AlertaCalor()

    # Se pasa el método sin paréntesis, como en el proyecto 070: la
    # estación lo llamará después, cuando haya una medición
    estacion.suscribir(actual.actualizar)
    estacion.suscribir(estadisticas.actualizar)
    estacion.suscribir(alerta.actualizar)
    estacion.suscribir(registrar_en_bitacora)

    estacion.medir(28)
    estacion.medir(36)
    print()

    # La bitácora deja de recibir avisos y la estación no cambia en nada
    estacion.desuscribir(registrar_en_bitacora)
    estacion.medir(31)
    print()

    try:
        estacion.suscribir(actual.actualizar)
    except ValueError as error:
        print(f"Error: {error}")
    try:
        estacion.desuscribir(registrar_en_bitacora)
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
