"""Proyecto 067: Clase Matriz.

Una clase Matriz que se suma, se resta, se multiplica y se compara con los
operadores de siempre: +, -, * y ==.
"""


class Matriz:
    """Matriz de números guardada como una lista de filas."""

    def __init__(self, filas):
        # La matriz es una lista de listas: cada elemento de filas es una
        # lista con los números de una fila. Todas deben medir lo mismo.
        if len(filas) == 0:
            raise ValueError("La matriz necesita al menos una fila.")
        for fila in filas:
            if len(fila) != len(filas[0]):
                raise ValueError("Todas las filas deben tener igual largo.")

        # Se guarda una copia de cada fila para que cambiar la lista
        # original desde fuera no cambie la matriz
        self.__filas = []
        for fila in filas:
            self.__filas.append(list(fila))
        self.num_filas = len(filas)
        self.num_columnas = len(filas[0])

    # __getitem__ es el método que Python llama al usar corchetes con un
    # objeto. matriz[1] llama a matriz.__getitem__(1) y devuelve la fila
    # 1, así que matriz[1][0] da el primer número de esa fila. Se devuelve
    # una copia para que nadie modifique la matriz por esa vía.
    def __getitem__(self, fila):
        """Devuelve una copia de la fila pedida."""
        return list(self.__filas[fila])

    def dimensiones(self):
        """Devuelve las dimensiones como texto, por ejemplo 2x3."""
        return f"{self.num_filas}x{self.num_columnas}"

    def revisar_mismas_dimensiones(self, otra, operacion):
        """Lanza ValueError si las dos matrices no miden lo mismo."""
        primera = self.dimensiones()
        segunda = otra.dimensiones()
        if primera != segunda:
            inicio = f"No se puede {operacion} una {primera} con una {segunda}"
            raise ValueError(f"{inicio}: deben medir lo mismo.")

    # Sobrecargar un operador es definir qué hace con objetos de la clase.
    # Python traduce a + b en a.__add__(b), así que este método decide qué
    # significa sumar dos matrices: sumar los números en la misma posición.
    def __add__(self, otra):
        """Devuelve la suma elemento por elemento."""
        self.revisar_mismas_dimensiones(otra, "sumar")
        resultado = []
        for i in range(self.num_filas):
            fila = []
            for j in range(self.num_columnas):
                fila.append(self[i][j] + otra[i][j])
            resultado.append(fila)
        return Matriz(resultado)

    # a - b se traduce en a.__sub__(b)
    def __sub__(self, otra):
        """Devuelve la resta elemento por elemento."""
        self.revisar_mismas_dimensiones(otra, "restar")
        resultado = []
        for i in range(self.num_filas):
            fila = []
            for j in range(self.num_columnas):
                fila.append(self[i][j] - otra[i][j])
            resultado.append(fila)
        return Matriz(resultado)

    # a * b se traduce en a.__mul__(b). Aquí es el producto de matrices:
    # cada número del resultado sale de multiplicar una fila de la primera
    # por una columna de la segunda y sumar esos productos. Por eso las
    # columnas de la primera deben ser tantas como las filas de la segunda.
    def __mul__(self, otra):
        """Devuelve el producto de matrices."""
        if self.num_columnas != otra.num_filas:
            primera = self.dimensiones()
            segunda = otra.dimensiones()
            inicio = f"No se puede multiplicar una {primera} por una {segunda}"
            detalle = "la primera debe tener tantas columnas como filas tiene"
            raise ValueError(f"{inicio}: {detalle} la segunda.")
        resultado = []
        for i in range(self.num_filas):
            fila = []
            for j in range(otra.num_columnas):
                suma = 0
                for k in range(self.num_columnas):
                    suma = suma + self[i][k] * otra[k][j]
                fila.append(suma)
            resultado.append(fila)
        return Matriz(resultado)

    # a == b se traduce en a.__eq__(b). Sin este método, == solo diría
    # True si a y b fueran el mismo objeto, aunque tuvieran los mismos
    # números.
    def __eq__(self, otra):
        """Devuelve True si las dos matrices tienen los mismos números."""
        if not isinstance(otra, Matriz):
            return False
        return self.__filas == otra.__filas

    def __str__(self):
        """Devuelve la matriz con una fila por renglón."""
        renglones = []
        for fila in self.__filas:
            numeros = []
            for numero in fila:
                numeros.append(f"{numero:>5}")
            renglones.append("".join(numeros))
        return "\n".join(renglones)


def mostrar(titulo, matriz):
    """Muestra un título y la matriz debajo."""
    print(f"{titulo} ({matriz.dimensiones()}):")
    print(matriz)
    print()


def main():
    """Opera con varias matrices y muestra los errores de dimensiones."""
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    c = Matriz([[1, 0, 2], [0, 1, 3]])

    mostrar("A", a)
    mostrar("B", b)
    mostrar("A + B", a + b)
    mostrar("B - A", b - a)
    mostrar("A * B", a * b)
    mostrar("A * C", a * c)

    print(f"El elemento de la fila 2, columna 1 de A es {a[1][0]}")
    print(f"¿A == A copiada? {a == Matriz([[1, 2], [3, 4]])}")
    print(f"¿A == B? {a == b}")
    print()

    # Las operaciones con dimensiones incompatibles lanzan ValueError
    try:
        a + c
    except ValueError as error:
        print(error)
    try:
        c * a
    except ValueError as error:
        print(error)
    try:
        Matriz([[1, 2], [3]])
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
