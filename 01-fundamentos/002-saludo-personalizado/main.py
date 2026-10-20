"""Proyecto 002: Saludo personalizado.

Pide algunos datos a quien lo ejecuta y responde con un saludo hecho con ellos.
"""

# input() muestra la pregunta y espera a que escribas algo.
# Lo que escribas se guarda como texto en la variable de la izquierda.
nombre = input("¿Cómo te llamas? ")
ciudad = input("¿Desde qué ciudad me escribes? ")
meta = input("¿Qué te gustaría crear con Python? ")

print()

# Unir texto con +: funciona, pero los espacios y la puntuación van a mano
print("Hola, " + nombre + ".")

# Con un f-string las variables van entre llaves dentro del texto,
# así la frase completa se lee de corrido
print(f"Qué gusto que me escribas desde {ciudad}.")
print(f"Si quieres crear {meta}, vas por buen camino: esta ruta te va a llevar ahí.")
