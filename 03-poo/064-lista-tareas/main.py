"""Proyecto 064: Lista de tareas.

Un gestor de tareas con prioridad. Permite agregar, completar y eliminar
tareas, ver las pendientes y ordenarlas de la más urgente a la menos urgente.
"""

PRIORIDADES = {1: "alta", 2: "media", 3: "baja"}


class Tarea:
    """Tarea con título, prioridad del 1 al 3 y estado."""

    def __init__(self, titulo, prioridad):
        self.titulo = titulo
        self.prioridad = prioridad
        self.completada = False

    def __str__(self):
        """Devuelve la tarea con una casilla que indica su estado."""
        if self.completada:
            casilla = "[x]"
        else:
            casilla = "[ ]"
        nombre_prioridad = PRIORIDADES[self.prioridad]
        return f"{casilla} {self.titulo} (prioridad {nombre_prioridad})"


class GestorTareas:
    """Guarda las tareas en una lista y las administra."""

    def __init__(self):
        self.tareas = []

    def agregar(self, titulo, prioridad):
        """Crea una tarea si los datos son válidos. Devuelve True si sí."""
        if titulo.strip() == "":
            print("La tarea necesita un título.")
            return False
        if prioridad not in PRIORIDADES:
            print(f"La prioridad de {titulo} debe ser 1, 2 o 3.")
            return False
        self.tareas.append(Tarea(titulo, prioridad))
        print(f"Agregaste: {titulo}")
        return True

    def es_numero_valido(self, numero):
        """Devuelve True si existe una tarea con ese número."""
        if 1 <= numero <= len(self.tareas):
            return True
        print(f"No hay una tarea con el número {numero}.")
        return False

    def completar(self, numero):
        """Marca como hecha la tarea con ese número. Devuelve True si sí."""
        if not self.es_numero_valido(numero):
            return False
        # Los números que ve el usuario empiezan en 1 y los índices en 0
        tarea = self.tareas[numero - 1]
        tarea.completada = True
        print(f"Completaste: {tarea.titulo}")
        return True

    def eliminar(self, numero):
        """Quita de la lista la tarea con ese número. Devuelve True si sí."""
        if not self.es_numero_valido(numero):
            return False
        tarea = self.tareas[numero - 1]
        self.tareas.remove(tarea)
        print(f"Eliminaste: {tarea.titulo}")
        return True

    def pendientes(self):
        """Devuelve una lista con las tareas que faltan por hacer."""
        faltan = []
        for tarea in self.tareas:
            if not tarea.completada:
                faltan.append(tarea)
        return faltan

    def ordenadas_por_prioridad(self):
        """Devuelve las tareas ordenadas de prioridad alta a baja."""
        # sorted() sabe comparar números o textos, pero no objetos Tarea.
        # El parámetro key recibe una función que se aplica a cada elemento
        # para obtener el valor con el que se compara.
        #
        # lambda crea una función anónima: una función sin nombre que se
        # escribe en una sola línea. Antes de los dos puntos van sus
        # parámetros y después lo que devuelve, sin escribir return. Esta
        # lambda equivale a:
        #     def obtener_prioridad(tarea):
        #         return tarea.prioridad
        # Conviene usarla cuando la función es tan corta que solo se usa en
        # ese lugar, como aquí. Si hace más de una cosa, es mejor un def.
        return sorted(self.tareas, key=lambda tarea: tarea.prioridad)

    def mostrar(self, tareas, titulo):
        """Muestra una lista de tareas numeradas bajo un título."""
        print(titulo)
        if len(tareas) == 0:
            print("  No hay tareas.")
        for numero, tarea in enumerate(tareas, 1):
            print(f"  {numero}. {tarea}")


def main():
    """Administra una lista de tareas de ejemplo."""
    gestor = GestorTareas()
    gestor.agregar("Lavar los trastes", 3)
    gestor.agregar("Entregar la tarea de física", 1)
    gestor.agregar("Comprar el regalo de mamá", 2)
    gestor.agregar("Pagar el internet", 1)
    gestor.agregar("Ordenar el cuarto", 3)
    gestor.agregar("Llamar al dentista", 5)
    gestor.agregar("   ", 2)
    print()

    gestor.mostrar(gestor.tareas, "Todas las tareas:")
    print()

    gestor.completar(2)
    gestor.eliminar(5)
    gestor.completar(9)
    print()

    gestor.mostrar(gestor.tareas, "Todas las tareas:")
    print()
    gestor.mostrar(gestor.pendientes(), "Pendientes:")
    print()
    # sorted() devuelve una lista nueva, así que self.tareas conserva el
    # orden en que se agregaron
    ordenadas = gestor.ordenadas_por_prioridad()
    gestor.mostrar(ordenadas, "Ordenadas por prioridad:")


if __name__ == "__main__":
    main()
