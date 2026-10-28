"""Proyecto 032: Piedra, papel o tijera.

Juegas contra la computadora, que elige al azar. El programa lleva el marcador
y te deja jugar las rondas que quieras hasta que eliges salir.
"""

import random

victorias = 0
derrotas = 0
empates = 0

opcion = ""

while opcion != "4":
    print("=== Piedra, papel o tijera ===")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    print()

    if opcion == "1" or opcion == "2" or opcion == "3":
        # Convertir la opción del menú en el nombre de la jugada hace que
        # las comparaciones de abajo se lean como las reglas del juego
        if opcion == "1":
            jugador = "piedra"
        elif opcion == "2":
            jugador = "papel"
        else:
            jugador = "tijera"

        # La computadora elige un entero del 1 al 3 y se convierte en jugada
        # con if/elif, de la misma forma que la opción del jugador
        numero_computadora = random.randint(1, 3)
        if numero_computadora == 1:
            computadora = "piedra"
        elif numero_computadora == 2:
            computadora = "papel"
        else:
            computadora = "tijera"

        print(f"Tú elegiste {jugador} y la computadora eligió {computadora}.")

        # Cada variable bool guarda si se cumple una de las tres formas de
        # ganar. Así la condición de victoria queda corta y fácil de leer.
        gana_con_piedra = jugador == "piedra" and computadora == "tijera"
        gana_con_papel = jugador == "papel" and computadora == "piedra"
        gana_con_tijera = jugador == "tijera" and computadora == "papel"

        # Basta con que una forma de ganar se cumpla. Si no es empate ni
        # victoria, solo queda la derrota.
        if jugador == computadora:
            empates = empates + 1
            print("Empate.")
        elif gana_con_piedra or gana_con_papel or gana_con_tijera:
            victorias = victorias + 1
            print("Ganaste esta ronda.")
        else:
            derrotas = derrotas + 1
            print("Perdiste esta ronda.")

        print(f"Tú {victorias} - {derrotas} computadora. Empates: {empates}")
    elif opcion == "4":
        print("Marcador final:")
        print(f"  Victorias: {victorias}")
        print(f"  Derrotas:  {derrotas}")
        print(f"  Empates:   {empates}")
        if victorias > derrotas:
            print("Le ganaste a la computadora.")
        elif victorias < derrotas:
            print("La computadora ganó esta vez.")
        else:
            print("Quedaron parejos.")
    else:
        print(f"La opción {opcion} no existe. Elige del 1 al 4.")

    print()
