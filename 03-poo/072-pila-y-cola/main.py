"""Proyecto 072: Pila y cola.

Dos estructuras de datos clásicas. La pila revisa si los paréntesis de un
texto están balanceados y la cola simula la fila de un banco.
"""

# collections es un módulo de la biblioteca estándar con estructuras de
# datos extra. deque (se pronuncia "dek", de double-ended queue) es una
# secuencia a la que se le agregan y quitan elementos por los dos extremos.
from collections import deque

APERTURAS = "([{"
PARES = {")": "(", "]": "[", "}": "{"}


class EstructuraVaciaError(Exception):
    """Se intentó sacar o consultar un elemento de una estructura vacía."""


# Una pila funciona como una pila de platos: el último que entra es el
# primero que sale (LIFO, last in, first out). Una lista sirve bien, porque
# append() y pop() trabajan en el final y eso es rápido.
class Pila:
    """Pila de elementos: se agrega y se saca por el tope."""

    def __init__(self):
        self.__elementos = []

    def apilar(self, elemento):
        """Pone un elemento en el tope."""
        self.__elementos.append(elemento)

    def desapilar(self):
        """Saca y devuelve el tope. Lanza EstructuraVaciaError si no hay."""
        if self.esta_vacia():
            raise EstructuraVaciaError("No se puede desapilar: está vacía.")
        # pop() sin argumento quita y devuelve el último elemento
        return self.__elementos.pop()

    def ver_tope(self):
        """Devuelve el tope sin sacarlo."""
        if self.esta_vacia():
            raise EstructuraVaciaError("La pila está vacía.")
        return self.__elementos[-1]

    def esta_vacia(self):
        """Devuelve True si no hay elementos."""
        return len(self.__elementos) == 0

    # __len__ es el método que llama len(). Con él, len(pila) funciona
    # igual que con una lista.
    def __len__(self):
        """Devuelve cuántos elementos hay."""
        return len(self.__elementos)


# Una cola funciona como la fila de un banco: el primero que llega es el
# primero que sale (FIFO, first in, first out). Con una lista habría que
# usar pop(0), que quita el primer elemento pero obliga a Python a recorrer
# todos los demás para moverlos un lugar. Con miles de elementos eso es
# lento. deque está hecha para quitar del inicio con popleft() sin mover
# nada, así que tarda lo mismo con 10 elementos que con un millón.
class Cola:
    """Cola de elementos: se agrega al final y se saca del frente."""

    def __init__(self):
        self.__elementos = deque()

    def encolar(self, elemento):
        """Agrega un elemento al final de la fila."""
        self.__elementos.append(elemento)

    def desencolar(self):
        """Saca y devuelve el primero. Lanza EstructuraVaciaError si no hay."""
        if self.esta_vacia():
            raise EstructuraVaciaError("No se puede desencolar: está vacía.")
        return self.__elementos.popleft()

    def ver_frente(self):
        """Devuelve el primero sin sacarlo."""
        if self.esta_vacia():
            raise EstructuraVaciaError("La cola está vacía.")
        return self.__elementos[0]

    def esta_vacia(self):
        """Devuelve True si no hay elementos."""
        return len(self.__elementos) == 0

    def __len__(self):
        """Devuelve cuántos elementos hay."""
        return len(self.__elementos)


def esta_balanceado(texto):
    """Devuelve True si cada paréntesis abierto se cierra en orden."""
    pila = Pila()
    for caracter in texto:
        if caracter in APERTURAS:
            pila.apilar(caracter)
        elif caracter in PARES:
            # Un cierre sin apertura pendiente, o que no corresponde a la
            # última apertura, deja el texto desbalanceado
            if pila.esta_vacia():
                return False
            if pila.desapilar() != PARES[caracter]:
                return False
    # Si sobra alguna apertura, quedó algo sin cerrar
    return pila.esta_vacia()


def simular_banco(clientes):
    """Forma a los clientes y los atiende en orden de llegada."""
    fila = Cola()
    for cliente in clientes:
        fila.encolar(cliente)
        print(f"  Llega {cliente}. Personas en la fila: {len(fila)}")

    turno = 1
    while not fila.esta_vacia():
        cliente = fila.desencolar()
        print(f"  Turno {turno}: pasa {cliente}. Quedan {len(fila)}")
        turno = turno + 1


def main():
    """Prueba la pila con paréntesis y la cola con la fila de un banco."""
    print("Paréntesis balanceados:")
    for texto in ["(a + b) * [c - d]", "{[()()]}", "(a + b]", "((x)", ")("]:
        if esta_balanceado(texto):
            resultado = "balanceado"
        else:
            resultado = "no balanceado"
        print(f"  {texto:<20} {resultado}")
    print()

    print("Fila del banco:")
    simular_banco(["Ana", "Luis", "Sofía", "Carlos"])
    print()

    # Sacar de una estructura vacía lanza la excepción propia
    try:
        Pila().desapilar()
    except EstructuraVaciaError as error:
        print(f"Error: {error}")
    try:
        Cola().desencolar()
    except EstructuraVaciaError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
