"""Proyecto 003: Conversor de temperatura.

Convierte una temperatura de Celsius a Fahrenheit y otra de Fahrenheit a Celsius.
"""

# De Celsius a Fahrenheit

# input() siempre devuelve una cadena de texto, y con texto no se puede
# calcular. float() hace una conversión de tipo: convierte ese texto en un
# número decimal (tipo float).
# El guion bajo _ separa palabras en el nombre de una variable (estilo de PEP 8).
texto_celsius = input("Escribe una temperatura en grados Celsius: ")
celsius = float(texto_celsius)

# Operadores aritméticos: * multiplica, / divide, + suma y - resta.
# Python sigue la jerarquía de operaciones: primero * y /, después + y -.
# Por eso aquí se multiplica y divide antes de sumar 32.
resultado_fahrenheit = celsius * 9 / 5 + 32

# round() es una función integrada que redondea un número. El segundo valor
# indica cuántos decimales dejar.
print(celsius, "°C equivalen a", round(resultado_fahrenheit, 1), "°F")
print()

# De Fahrenheit a Celsius

# Aquí input() va dentro de float(): primero se ejecuta input() y su resultado
# pasa directo a float(). Hace lo mismo que las dos líneas de arriba.
fahrenheit = float(input("Escribe una temperatura en grados Fahrenheit: "))

# Los paréntesis agrupan una operación para que se haga primero:
# aquí se resta 32 antes de multiplicar por 5 y dividir entre 9.
resultado_celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "°F equivalen a", round(resultado_celsius, 1), "°C")
