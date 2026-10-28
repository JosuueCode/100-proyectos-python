"""Proyecto 034: Calculadora con funciones.

Versión de la calculadora del proyecto 004 organizada con funciones: una por
operación y un menú que se repite hasta que eliges salir.
"""


def sumar(numero1, numero2):
    """Devuelve la suma de dos números."""
    return numero1 + numero2


def restar(numero1, numero2):
    """Devuelve la resta del primer número menos el segundo."""
    return numero1 - numero2


def multiplicar(numero1, numero2):
    """Devuelve el producto de dos números."""
    return numero1 * numero2


def dividir(dividendo, divisor):
    """Devuelve el cociente. El divisor no debe ser cero."""
    return dividendo / divisor


# Una función no siempre necesita parámetros ni return. Esta solo agrupa
# los print del menú para que el ciclo de abajo quede más corto.
def mostrar_menu():
    """Muestra las opciones de la calculadora."""
    print("=== Calculadora ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def pedir_numero(mensaje):
    """Pide un número con el mensaje indicado y lo devuelve como float."""
    return float(input(mensaje))


def mostrar_resultado(numero1, simbolo, numero2, resultado):
    """Muestra la operación completa con su resultado."""
    print(f"{numero1} {simbolo} {numero2} = {resultado}")


opcion = ""

while opcion != "5":
    mostrar_menu()
    opcion = input("Elige una opción: ")
    print()

    if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
        numero1 = pedir_numero("Primer número: ")
        numero2 = pedir_numero("Segundo número: ")

        # Cada rama llama a la función de su operación y guarda lo que
        # devuelve return, para después pasarlo a mostrar_resultado()
        if opcion == "1":
            resultado = sumar(numero1, numero2)
            mostrar_resultado(numero1, "+", numero2, resultado)
        elif opcion == "2":
            resultado = restar(numero1, numero2)
            mostrar_resultado(numero1, "-", numero2, resultado)
        elif opcion == "3":
            resultado = multiplicar(numero1, numero2)
            mostrar_resultado(numero1, "*", numero2, resultado)
        else:
            # Se revisa el divisor antes de llamar a dividir(), porque
            # dividir entre cero detiene el programa con un error
            if numero2 == 0:
                print("No se puede dividir entre cero.")
            else:
                resultado = dividir(numero1, numero2)
                mostrar_resultado(numero1, "/", numero2, resultado)
    elif opcion == "5":
        print("Gracias por usar la calculadora.")
    else:
        print(f"La opción {opcion} no existe. Elige del 1 al 5.")

    print()
