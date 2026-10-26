"""Proyecto 025: Cajero con menú.

Versión mejorada del cajero del proyecto 009. Muestra un menú que se repite
para consultar el saldo, depositar y retirar, hasta que elijas salir.
"""

SALDO_INICIAL = 5000.0

saldo = SALDO_INICIAL
operaciones = 0

# El ciclo depende de la opción elegida. Antes de entrar se le da un valor
# vacío ("") para que la condición sea True en la primera vuelta y el menú
# se muestre al menos una vez.
opcion = ""

# El menú se repite mientras la opción sea distinta de "4". Cuando eliges
# salir, la condición da False y el ciclo termina.
while opcion != "4":
    print("=== Cajero ===")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    print()

    if opcion == "1":
        print("Tu saldo es", round(saldo, 2))
    elif opcion == "2":
        deposito = float(input("¿Cuánto quieres depositar? "))
        if deposito <= 0:
            print("El depósito debe ser mayor que cero.")
        else:
            saldo = saldo + deposito
            operaciones = operaciones + 1
            print("Depositaste", deposito)
            print("Tu nuevo saldo es", round(saldo, 2))
    elif opcion == "3":
        retiro = float(input("¿Cuánto quieres retirar? "))
        if retiro <= 0:
            print("El retiro debe ser mayor que cero.")
        elif retiro > saldo:
            print("Saldo insuficiente. Tu saldo es", round(saldo, 2))
        else:
            saldo = saldo - retiro
            operaciones = operaciones + 1
            print("Retiraste", retiro)
            print("Tu nuevo saldo es", round(saldo, 2))
    elif opcion == "4":
        print("Gracias por usar el cajero.")
        print("Operaciones realizadas:", operaciones)
        print("Saldo final:", round(saldo, 2))
    else:
        print("La opción", opcion, "no existe. Elige del 1 al 4.")

    print()
