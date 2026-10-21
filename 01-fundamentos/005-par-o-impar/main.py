"""Proyecto 005: Par o impar.

Pide un número entero y dice si es par o impar, y si es positivo, negativo
o cero.
"""

# int() es otra conversión de tipo: convierte el texto en un número entero
# (tipo int), sin decimales. Aquí se usa int() y no float() porque "par" e
# "impar" solo tienen sentido con enteros.
numero = int(input("Escribe un número entero: "))

print()

# % es el operador módulo: da el residuo de una división entera.
# Un número es par si al dividirlo entre 2 el residuo es 0.
# Python calcula primero numero % 2 y después compara ese resultado con 0.
if numero % 2 == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")

# Esta segunda estructura condicional es independiente de la primera:
# se revisa siempre, sin importar si el número fue par o impar.
# > y < son operadores de comparación: > da True si el valor de la izquierda
# es mayor que el de la derecha, y < da True si es menor.
if numero > 0:
    print(numero, "es positivo")
elif numero < 0:
    print(numero, "es negativo")
else:
    print("El número es cero")
