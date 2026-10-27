"""Proyecto 029: Detector de palíndromos.

Revisa si una palabra o frase se lee igual al derecho y al revés, sin tomar
en cuenta las mayúsculas ni los espacios.
"""

print("Un palíndromo se lee igual al derecho y al revés.")
print("Escribe una palabra o frase, o deja el texto vacío para salir.")
print()

frase = input("Palabra o frase: ").strip()

while frase != "":
    # Para comparar sin importar mayúsculas ni espacios, primero se limpia el
    # texto: lower() lo pasa a minúsculas y replace(" ", "") cambia cada
    # espacio por un texto vacío, o sea, lo quita.
    # Los métodos se pueden encadenar: cada uno trabaja sobre el texto nuevo
    # que devolvió el anterior, de izquierda a derecha.
    limpia = frase.lower().replace(" ", "")
    al_reves = limpia[::-1]

    print(f"Texto limpio: {limpia}")
    print(f"Al revés:     {al_reves}")

    # Dos textos son iguales con == solo si tienen los mismos caracteres en
    # el mismo orden
    if limpia == al_reves:
        print(f"'{frase}' es un palíndromo.")
    else:
        print(f"'{frase}' no es un palíndromo.")

    print()
    frase = input("Palabra o frase: ").strip()

print("Hasta luego.")
