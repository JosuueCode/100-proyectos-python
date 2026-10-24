"""Proyecto 011: Mayor de tres números.

Pide tres números y dice cuál es el mayor usando solo condicionales anidados.
"""

numero1 = float(input("Escribe el primer número: "))
numero2 = float(input("Escribe el segundo número: "))
numero3 = float(input("Escribe el tercer número: "))

# Primero se comparan numero1 y numero2. El que gane se compara después con
# numero3, dentro de un condicional anidado. Así cada camino termina con el
# mayor de los tres.
# Se usa >= y no > para que un empate también tenga respuesta.
if numero1 >= numero2:
    if numero1 >= numero3:
        mayor = numero1
    else:
        mayor = numero3
else:
    if numero2 >= numero3:
        mayor = numero2
    else:
        mayor = numero3

# La variable mayor recibe su valor en uno de los cuatro bloques de arriba,
# y como todos los caminos le asignan algo, aquí ya existe.
print()
print("El número mayor es", mayor)
