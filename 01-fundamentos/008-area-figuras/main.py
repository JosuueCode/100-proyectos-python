"""Proyecto 008: Área de figuras.

Muestra un menú de figuras, pide sus medidas y calcula el área de la que
elijas.
"""

# Valor aproximado de pi, guardado como constante para usarlo en el círculo
PI = 3.1416

print("¿De qué figura quieres calcular el área?")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Triángulo")
print("4. Círculo")
opcion = input("Escribe el número de la opción: ")

print()

# La opción se compara como texto ("1", no 1) porque input() devuelve una
# cadena. Cada bloque pide solo las medidas que necesita su figura.
if opcion == "1":
    lado = float(input("Medida del lado: "))
    area = lado * lado
    print("El área del cuadrado es", round(area, 2))
elif opcion == "2":
    base = float(input("Medida de la base: "))
    altura = float(input("Medida de la altura: "))
    area = base * altura
    print("El área del rectángulo es", round(area, 2))
elif opcion == "3":
    base = float(input("Medida de la base: "))
    altura = float(input("Medida de la altura: "))
    area = base * altura / 2
    print("El área del triángulo es", round(area, 2))
elif opcion == "4":
    radio = float(input("Medida del radio: "))
    # El radio al cuadrado se escribe como radio * radio
    area = PI * radio * radio
    print("El área del círculo es", round(area, 2))
else:
    print("La opción", opcion, "no existe. Elige un número del 1 al 4.")
