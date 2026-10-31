"""Proyecto 045: Ahorcado.

La computadora elige una palabra al azar y tú la adivinas letra por letra
antes de quedarte sin vidas.
"""

import random

# Una lista larga se puede escribir en varias líneas: mientras el corchete
# siga abierto, Python sabe que la instrucción continúa en la línea siguiente
PALABRAS = ["python", "variable", "funcion", "lista", "ciclo",
            "diccionario", "programa", "teclado", "pantalla", "codigo"]
VIDAS_INICIALES = 6
ABECEDARIO = "abcdefghijklmnñopqrstuvwxyz"


def mostrar_palabra(palabra, letras_usadas):
    """Devuelve la palabra con guiones bajos en las letras sin adivinar."""
    partes = []
    for letra in palabra:
        if letra in letras_usadas:
            partes.append(letra)
        else:
            partes.append("_")
    # join() es un método de str que une los elementos de una lista en un
    # solo texto, poniendo entre cada uno el texto sobre el que se llama.
    # Aquí se usa un espacio para que los guiones bajos no se vean pegados.
    return " ".join(partes)


def palabra_completa(palabra, letras_usadas):
    """Devuelve True si ya se adivinaron todas las letras de la palabra."""
    for letra in palabra:
        if letra not in letras_usadas:
            return False
    return True


def pedir_letra(letras_usadas):
    """Pide una letra válida que no se haya usado y la devuelve."""
    letra = input("Escribe una letra: ").strip().lower()
    while len(letra) != 1 or letra not in ABECEDARIO or letra in letras_usadas:
        if len(letra) != 1 or letra not in ABECEDARIO:
            print("Escribe una sola letra, sin acentos ni números.")
        else:
            print(f"Ya usaste la letra {letra}. Prueba con otra.")
        letra = input("Escribe una letra: ").strip().lower()
    return letra


# choice() del módulo random elige un elemento al azar de una lista. Es
# más directo que generar una posición con randint() y usarla como índice.
palabra_secreta = random.choice(PALABRAS)
letras_usadas = []
vidas = VIDAS_INICIALES

print("=== Ahorcado ===")
print(f"La palabra tiene {len(palabra_secreta)} letras.")

while vidas > 0 and not palabra_completa(palabra_secreta, letras_usadas):
    print()
    print(f"Palabra: {mostrar_palabra(palabra_secreta, letras_usadas)}")
    print(f"Vidas: {vidas}")
    if len(letras_usadas) > 0:
        print(f"Letras usadas: {', '.join(letras_usadas)}")

    letra = pedir_letra(letras_usadas)
    letras_usadas.append(letra)

    if letra in palabra_secreta:
        print(f"Bien, la {letra} está en la palabra.")
    else:
        vidas = vidas - 1
        print(f"La {letra} no está en la palabra.")

print()
if vidas > 0:
    print(f"Ganaste. La palabra era {palabra_secreta}.")
    if vidas == 1:
        print("Te sobró 1 vida.")
    else:
        print(f"Te sobraron {vidas} vidas.")
else:
    print(f"Te quedaste sin vidas. La palabra era {palabra_secreta}.")
