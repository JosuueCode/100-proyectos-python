"""Proyecto 019: Cuadrado y cubo de un número.

Pide un número y muestra su cuadrado y su cubo, calculados con el operador
de potencia.
"""

numero = float(input("Escribe un número: "))

# ** es el operador aritmético de potencia: numero ** 2 eleva numero a la
# segunda potencia (numero * numero) y numero ** 3 a la tercera
# (numero * numero * numero). El número de la derecha es el exponente.
# Python resuelve ** antes que *, /, + y -.
cuadrado = numero ** 2
cubo = numero ** 3

# Hasta ahora el cuadrado se escribía con multiplicaciones. Se calcula también
# así para comprobar que las dos formas dan lo mismo.
cuadrado_multiplicando = numero * numero

print()
# round() con 4 decimales evita resultados como 1.2100000000000002, que salen
# porque la computadora guarda los decimales de forma aproximada
print("El cuadrado de", numero, "es", round(cuadrado, 4))
print("El cubo de", numero, "es", round(cubo, 4))
print()
print("Con multiplicación da lo mismo:", round(cuadrado_multiplicando, 4))
