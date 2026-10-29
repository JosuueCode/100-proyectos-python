"""Proyecto 036: Fibonacci.

Pide cuántos términos quieres y muestra el inicio de la sucesión de
Fibonacci, donde cada número es la suma de los dos anteriores.
"""


def mostrar_fibonacci(cantidad):
    """Muestra los primeros términos de la sucesión de Fibonacci."""
    # La asignación múltiple da valor a varias variables en una sola línea:
    # a recibe 0 y b recibe 1, en el mismo orden en que están escritos.
    # a es el término que toca mostrar y b es el que sigue.
    a, b = 0, 1
    posicion = 1

    while posicion <= cantidad:
        print(f"{posicion}: {a}")
        # Python calcula primero todo lo que está a la derecha del =, con los
        # valores que a y b tienen en ese momento, y después los asigna.
        # Así a + b usa el a viejo aunque a cambie en la misma línea.
        # Con dos líneas separadas, a = b borraría el valor viejo de a antes
        # de sumarlo, y haría falta una variable temporal para guardarlo.
        a, b = b, a + b
        posicion = posicion + 1


cantidad_terminos = int(input("¿Cuántos términos de Fibonacci quieres ver? "))

while cantidad_terminos < 1:
    print("Escribe un número mayor que cero.")
    cantidad_terminos = int(input("¿Cuántos términos quieres ver? "))

print()
mostrar_fibonacci(cantidad_terminos)
