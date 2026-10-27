"""Proyecto 030: Contador de vocales.

Pide un texto y cuenta cuántas veces aparece cada vocal, con y sin acento,
y el total de vocales.
"""

texto = input("Escribe un texto: ")

# Un contador por vocal, todos empiezan en cero
cantidad_a = 0
cantidad_e = 0
cantidad_i = 0
cantidad_o = 0
cantidad_u = 0

# Un for también puede recorrer un str: en cada vuelta, la variable letra
# toma el siguiente carácter del texto, del primero al último.
# Se usa lower() para que "A" y "a" cuenten como la misma vocal.
for letra in texto.lower():
    # Fuera de un for, in es un operador de pertenencia: letra in "aá" da
    # True si letra aparece dentro del texto "aá". Así una sola condición
    # sirve para la vocal con acento y sin acento.
    if letra in "aá":
        cantidad_a = cantidad_a + 1
    elif letra in "eé":
        cantidad_e = cantidad_e + 1
    elif letra in "ií":
        cantidad_i = cantidad_i + 1
    elif letra in "oó":
        cantidad_o = cantidad_o + 1
    elif letra in "uúü":
        cantidad_u = cantidad_u + 1

total = cantidad_a + cantidad_e + cantidad_i + cantidad_o + cantidad_u

print()
print(f"a: {cantidad_a}")
print(f"e: {cantidad_e}")
print(f"i: {cantidad_i}")
print(f"o: {cantidad_o}")
print(f"u: {cantidad_u}")
print()

if total == 0:
    print("Tu texto no tiene vocales.")
elif total == 1:
    print("Tu texto tiene 1 vocal.")
else:
    print(f"Tu texto tiene {total} vocales.")
