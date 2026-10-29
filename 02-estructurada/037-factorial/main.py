"""Proyecto 037: Factorial.

Calcula el factorial de un número de dos formas, con un ciclo y con
recursión, y comprueba que las dos dan el mismo resultado.
"""

# Cada llamada recursiva ocupa memoria hasta que termina, y Python corta el
# programa con un error si hay demasiadas llamadas pendientes (unas 1000).
# Este límite deja el número dentro de un rango seguro y fácil de leer.
MAXIMO = 100


def factorial_iterativo(numero):
    """Devuelve el factorial de numero usando un ciclo for."""
    # El factorial es la multiplicación de 1 * 2 * 3 * ... * numero.
    # El acumulador empieza en 1 porque multiplicar por 1 no cambia nada.
    resultado = 1
    for factor in range(1, numero + 1):
        resultado = resultado * factor
    return resultado


def factorial_recursivo(numero):
    """Devuelve el factorial de numero usando recursión."""
    # Una función recursiva es la que se llama a sí misma con un problema
    # más pequeño. Aquí se usa que 5! = 5 * 4!, y 4! = 4 * 3!, y así.
    # El caso base es el punto donde la función deja de llamarse y responde
    # directo: el factorial de 0 y de 1 es 1. Sin el caso base, la función
    # se llamaría con 0, -1, -2... sin parar, hasta que Python la detenga
    # con un error por exceso de llamadas (RecursionError).
    if numero <= 1:
        return 1
    return numero * factorial_recursivo(numero - 1)


numero_elegido = int(input(f"Escribe un número entero del 0 al {MAXIMO}: "))

while numero_elegido < 0 or numero_elegido > MAXIMO:
    if numero_elegido < 0:
        print("El factorial no existe para números negativos.")
    else:
        print(f"Elige un número que no pase de {MAXIMO}.")
    numero_elegido = int(input("Escribe el número otra vez: "))

con_ciclo = factorial_iterativo(numero_elegido)
con_recursion = factorial_recursivo(numero_elegido)

print()
print(f"Con un ciclo for:  {numero_elegido}! = {con_ciclo}")
print(f"Con recursión:     {numero_elegido}! = {con_recursion}")

if con_ciclo == con_recursion:
    print("Las dos funciones dan el mismo resultado.")
else:
    print("Los resultados no coinciden, algo está mal en una función.")
