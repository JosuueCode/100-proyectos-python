"""Proyecto 033: Máximo con función.

Pide tres números y muestra el mayor de los dos primeros y el mayor de los
tres, usando una función propia que compara dos números.
"""


# def define una función propia: un bloque de código con nombre que se
# puede usar las veces que haga falta. Entre paréntesis van los parámetros,
# variables que reciben los valores con los que se llama a la función.
# Definirla solo le enseña a Python qué hacer; el código de adentro no se
# ejecuta hasta que alguien la llama.
# El texto entre triples comillas justo debajo de def es el docstring de la
# función: explica qué hace, igual que el docstring al inicio del archivo.
def mayor_de_dos(primero, segundo):
    """Devuelve el mayor de dos números."""
    # return termina la función y entrega un valor a quien la llamó.
    # No muestra nada en pantalla: eso lo hace print(). Con return, el
    # resultado se puede guardar en una variable o usar en otra operación.
    # Como return sale de la función, si el if se cumple ya no se llega a
    # la última línea, y por eso no hace falta un else.
    if primero > segundo:
        return primero
    return segundo


# Una función puede llamar a otra. Aquí se reutiliza mayor_de_dos: primero
# se compara el primer número con el segundo, y el ganador con el tercero.
def mayor_de_tres(primero, segundo, tercero):
    """Devuelve el mayor de tres números."""
    mayor_parcial = mayor_de_dos(primero, segundo)
    return mayor_de_dos(mayor_parcial, tercero)


numero1 = float(input("Escribe el primer número: "))
numero2 = float(input("Escribe el segundo número: "))
numero3 = float(input("Escribe el tercer número: "))

# Llamar a la función es escribir su nombre con los valores entre
# paréntesis. Cada valor se guarda en el parámetro de la misma posición, y
# el valor que entrega return queda en la variable de la izquierda.
mayor_entre_dos = mayor_de_dos(numero1, numero2)
mayor_entre_tres = mayor_de_tres(numero1, numero2, numero3)

print()
print(f"El mayor entre {numero1} y {numero2} es {mayor_entre_dos}.")
print(f"El mayor de los tres números es {mayor_entre_tres}.")
