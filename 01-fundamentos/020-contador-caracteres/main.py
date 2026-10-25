"""Proyecto 020: Contador de caracteres.

Pide un texto, cuenta cuántos caracteres tiene y lo compara con un límite
de 280 caracteres.
"""

LIMITE_CARACTERES = 280

texto = input("Escribe un texto: ")

# len() es una función integrada que devuelve la longitud de una cadena: el
# número de caracteres que tiene. Cuenta todo lo que hay entre las comillas,
# incluidos los espacios, los signos de puntuación y los acentos.
# Por ejemplo, len("hola mundo") es 10: 9 letras y 1 espacio.
cantidad = len(texto)

print()

# Una cadena vacía ("") tiene longitud 0: pasa si presionas Enter sin escribir
if cantidad == 0:
    print("No escribiste nada.")
else:
    print("Tu texto tiene", cantidad, "caracteres.")
    print("Recuerda que los espacios también cuentan como caracteres.")
    print()

    if cantidad <= LIMITE_CARACTERES:
        restantes = LIMITE_CARACTERES - cantidad
        print("Cabe en un mensaje de", LIMITE_CARACTERES, "caracteres.")
        print("Todavía puedes escribir", restantes, "caracteres más.")
    else:
        sobrantes = cantidad - LIMITE_CARACTERES
        print("No cabe en un mensaje de", LIMITE_CARACTERES, "caracteres.")
        print("Tendrías que quitar", sobrantes, "caracteres.")
