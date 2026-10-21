"""Proyecto 002: Saludo personalizado.

Pide algunos datos a quien lo ejecuta y responde con un saludo hecho con ellos.
"""

# input() es una función integrada: muestra el mensaje entre paréntesis y
# espera a que escribas algo y presiones Enter. Lo que escribes siempre llega
# como cadena de texto (str).
# El signo = es el operador de asignación: guarda el valor de la derecha en la
# variable de la izquierda. Una variable es un nombre que apunta a un valor.
nombre = input("¿Cómo te llamas? ")
ciudad = input("¿Desde qué ciudad me escribes? ")
meta = input("¿Qué te gustaría crear con Python? ")

print()

# print() acepta varios valores separados por comas y los muestra en la misma
# línea, con un espacio entre cada uno. Las variables van sin comillas para que
# se muestre su valor y no su nombre.
print("Hola", nombre)
print("Qué gusto que me escribas desde", ciudad)
print("Esta ruta te va a ayudar a crear", meta)
