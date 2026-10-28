"""Proyecto 031: Adivina el número.

La computadora elige un número secreto del 1 al 100 y tú intentas adivinarlo.
Después de cada intento te dice si el número es mayor o menor.
"""

# import carga un módulo para usar lo que trae dentro. Un módulo es un
# archivo de Python con funciones ya escritas. random viene en la biblioteca
# estándar, el conjunto de módulos que se instala junto con Python, así que
# no hay que descargar nada. Los import van al inicio del archivo.
import random

MINIMO = 1
MAXIMO = 100

# Las funciones de un módulo se llaman con el nombre del módulo, un punto y
# el nombre de la función. randint(a, b) devuelve un entero al azar entre
# a y b, incluyendo los dos extremos, a diferencia de range().
numero_secreto = random.randint(MINIMO, MAXIMO)

print(f"Estoy pensando en un número del {MINIMO} al {MAXIMO}.")
print("Intenta adivinarlo.")
print()

intentos = 0
# Empieza en 0, un valor fuera del rango, para que el ciclo se ejecute al
# menos una vez
intento = 0

while intento != numero_secreto:
    intento = int(input("Tu número: "))

    if intento < MINIMO or intento > MAXIMO:
        print(f"Ese número no cuenta. Elige uno del {MINIMO} al {MAXIMO}.")
    else:
        intentos = intentos + 1
        if intento < numero_secreto:
            print("El número secreto es mayor.")
        elif intento > numero_secreto:
            print("El número secreto es menor.")

print()
if intentos == 1:
    print(f"Adivinaste a la primera. El número era {numero_secreto}.")
else:
    print(f"Adivinaste. El número era {numero_secreto}.")
    print(f"Lo lograste en {intentos} intentos.")
