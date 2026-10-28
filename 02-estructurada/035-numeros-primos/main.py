"""Proyecto 035: Números primos.

Pide un límite y muestra todos los números primos desde 2 hasta ese límite,
usando una función que revisa si un número es primo.
"""


def es_primo(numero):
    """Devuelve True si el número es primo y False si no lo es."""
    # Los primos empiezan en 2: el 0, el 1 y los negativos no lo son
    if numero < 2:
        return False

    primo = True

    # Un número es primo si ningún número entre 2 y él mismo lo divide
    # exacto. Para saberlo se prueba cada divisor con el operador módulo.
    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            # break termina el ciclo de inmediato, aunque range() todavía
            # tenga números. En cuanto aparece un divisor ya se sabe que el
            # número no es primo, así que revisar los demás sería trabajo
            # inútil. Con 1000, por ejemplo, el ciclo se detiene en el 2 en
            # lugar de hacer 998 revisiones.
            break

    return primo


limite = int(input("¿Hasta qué número quieres buscar primos? "))

while limite < 2:
    print("El límite debe ser 2 o mayor, porque 2 es el primer primo.")
    limite = int(input("Escribe el límite otra vez: "))

print()
print(f"Números primos del 2 al {limite}:")

cantidad_primos = 0

# es_primo() devuelve un bool, así que se puede usar directo como condición
for numero in range(2, limite + 1):
    if es_primo(numero):
        cantidad_primos = cantidad_primos + 1
        print(numero)

print()
if cantidad_primos == 1:
    print(f"Hay 1 número primo hasta el {limite}.")
else:
    print(f"Hay {cantidad_primos} números primos hasta el {limite}.")
