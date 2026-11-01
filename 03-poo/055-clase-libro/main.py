"""Proyecto 055: Clase Libro.

Define una clase Libro que sabe mostrarse como texto de dos formas: una para
leerla en pantalla y otra pensada para quien programa.
"""


class Libro:
    """Libro con título, autor y año de publicación."""

    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    # Los métodos especiales tienen dos guiones bajos antes y después del
    # nombre, como __init__. Python los llama solo en ciertos momentos.
    # __str__ devuelve el texto pensado para las personas. Se usa con
    # print(libro), con str(libro) y dentro de un f-string.
    def __str__(self):
        """Devuelve el libro como texto para leer."""
        return f"{self.titulo}, de {self.autor} ({self.anio})"

    # __repr__ devuelve un texto pensado para quien programa: debe dejar
    # claro qué objeto es y, si se puede, verse como el código que lo crea.
    # Se usa con repr(libro) y cuando el objeto aparece dentro de una lista
    # que se imprime.
    def __repr__(self):
        """Devuelve el libro como el código que lo crea."""
        return f"Libro('{self.titulo}', '{self.autor}', {self.anio})"


def main():
    """Crea una lista de libros y la muestra de varias formas."""
    libros = [
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967),
        Libro("Pedro Páramo", "Juan Rulfo", 1955),
        Libro("Como agua para chocolate", "Laura Esquivel", 1989),
    ]

    print("Con print() se usa __str__:")
    for libro in libros:
        print(f"  {libro}")
    print()

    print("Con repr() se usa __repr__:")
    print(f"  {repr(libros[0])}")
    print()

    # Al imprimir una lista, Python muestra cada elemento con su __repr__.
    # Sin este método se vería algo como <__main__.Libro object at 0x...>,
    # que no dice nada del libro.
    print("Una lista impresa usa __repr__ en cada elemento:")
    print(libros)


if __name__ == "__main__":
    main()
