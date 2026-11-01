"""Proyecto 062: Biblioteca con préstamos.

Una biblioteca presta y recibe libros. Antes de cada préstamo revisa que el
libro esté disponible y que el usuario no tenga demasiados libros.
"""

LIMITE_PRESTAMOS = 2


class Libro:
    """Libro con título, autor y estado de disponibilidad."""

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        """Devuelve el título, el autor y si está disponible."""
        if self.disponible:
            estado = "disponible"
        else:
            estado = "prestado"
        return f"{self.titulo}, de {self.autor} ({estado})"


class Usuario:
    """Persona que se lleva libros prestados."""

    def __init__(self, nombre):
        self.nombre = nombre
        # Esta lista solo apunta a libros que ya existen en la biblioteca.
        # El usuario no los crea ni es su dueño: eso es una asociación.
        self.prestados = []

    def puede_pedir(self):
        """Devuelve True si aún no llega al límite de préstamos."""
        return len(self.prestados) < LIMITE_PRESTAMOS


class Biblioteca:
    """Biblioteca que guarda sus libros y lleva el control de préstamos."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = {}

    # La biblioteca crea sus propios objetos Libro y los guarda: eso es
    # composición, porque los libros son parte de ella y no existen fuera.
    # Los usuarios, en cambio, se crean aparte y solo se relacionan con la
    # biblioteca cuando piden o devuelven un libro: eso es una asociación.
    # En la asociación cada objeto vive por su cuenta y puede existir
    # aunque el otro desaparezca.
    def agregar_libro(self, titulo, autor):
        """Crea un libro y lo agrega al catálogo."""
        self.libros[titulo] = Libro(titulo, autor)

    def prestar(self, titulo, usuario):
        """Presta el libro si se puede. Devuelve True si se prestó."""
        if titulo not in self.libros:
            print(f"No hay ningún libro llamado {titulo}.")
            return False

        libro = self.libros[titulo]
        if not libro.disponible:
            print(f"{titulo} ya está prestado.")
            return False
        if not usuario.puede_pedir():
            print(f"{usuario.nombre} ya tiene {LIMITE_PRESTAMOS} libros.")
            return False

        libro.disponible = False
        usuario.prestados.append(libro)
        print(f"{usuario.nombre} se llevó {titulo}.")
        return True

    def devolver(self, titulo, usuario):
        """Recibe el libro si el usuario lo tenía. Devuelve True si sí."""
        for libro in usuario.prestados:
            if libro.titulo == titulo:
                usuario.prestados.remove(libro)
                libro.disponible = True
                print(f"{usuario.nombre} devolvió {titulo}.")
                return True
        print(f"{usuario.nombre} no tiene {titulo}.")
        return False

    def mostrar_catalogo(self):
        """Muestra todos los libros con su estado."""
        print(f"Catálogo de {self.nombre}:")
        for libro in self.libros.values():
            print(f"  {libro}")


def mostrar_prestamos(usuario):
    """Muestra los títulos que tiene un usuario."""
    titulos = []
    for libro in usuario.prestados:
        titulos.append(libro.titulo)
    if len(titulos) == 0:
        print(f"{usuario.nombre} no tiene libros.")
    else:
        print(f"{usuario.nombre} tiene: {', '.join(titulos)}")


def main():
    """Hace varios préstamos y devoluciones, algunos no permitidos."""
    biblioteca = Biblioteca("Biblioteca Central")
    biblioteca.agregar_libro("Pedro Páramo", "Juan Rulfo")
    biblioteca.agregar_libro("Aura", "Carlos Fuentes")
    biblioteca.agregar_libro("Ficciones", "Jorge Luis Borges")
    biblioteca.agregar_libro("Rayuela", "Julio Cortázar")

    ana = Usuario("Ana")
    luis = Usuario("Luis")

    biblioteca.prestar("Pedro Páramo", ana)
    biblioteca.prestar("Aura", ana)
    biblioteca.prestar("Rayuela", ana)
    biblioteca.prestar("Aura", luis)
    biblioteca.prestar("Don Quijote", luis)
    biblioteca.prestar("Ficciones", luis)
    print()

    biblioteca.devolver("Aura", ana)
    biblioteca.devolver("Rayuela", luis)
    biblioteca.prestar("Aura", luis)
    print()

    mostrar_prestamos(ana)
    mostrar_prestamos(luis)
    print()
    biblioteca.mostrar_catalogo()


if __name__ == "__main__":
    main()
