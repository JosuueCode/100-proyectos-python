"""Proyecto 041: Buscador en lista.

Busca frutas en una lista con una búsqueda lineal propia y compara el
resultado con las herramientas que trae Python: in, index() y count().
"""

FRUTAS = ["manzana", "pera", "uva", "mango", "pera", "kiwi", "uva", "pera"]


def buscar_posicion(lista, buscado):
    """Devuelve la posición de la primera aparición de buscado, o -1."""
    # La búsqueda lineal revisa los elementos uno por uno, desde el inicio,
    # hasta encontrar el que se busca. return sale de la función en cuanto
    # lo encuentra, así que no se revisa el resto de la lista.
    for posicion, elemento in enumerate(lista):
        if elemento == buscado:
            return posicion
    # Si el ciclo termina sin encontrarlo, se devuelve -1. Las posiciones
    # válidas empiezan en 0, así que -1 sirve como señal de "no está".
    return -1


def contar_apariciones(lista, buscado):
    """Devuelve cuántas veces aparece buscado en la lista."""
    veces = 0
    for elemento in lista:
        if elemento == buscado:
            veces = veces + 1
    return veces


def mostrar_frutas(lista):
    """Muestra la lista con la posición de cada elemento."""
    print("Frutas en la lista:")
    # Sin el segundo valor, enumerate() cuenta desde 0, igual que los índices
    for posicion, fruta in enumerate(lista):
        print(f"  {posicion}: {fruta}")


mostrar_frutas(FRUTAS)
print()
print("Escribe una fruta para buscarla, o deja el texto vacío para salir.")

buscada = input("Fruta: ").strip().lower()

while buscada != "":
    posicion = buscar_posicion(FRUTAS, buscada)
    veces = contar_apariciones(FRUTAS, buscada)

    print()
    if posicion == -1:
        print(f"Búsqueda propia: {buscada} no está en la lista.")
    else:
        # Las listas también usan índices entre corchetes, como los str:
        # FRUTAS[posicion] es el elemento que está en esa posición
        print(f"Búsqueda propia: está en la posición {posicion}.")
        print(f"  FRUTAS[{posicion}] es {FRUTAS[posicion]}")
        if veces == 1:
            print("  Aparece 1 vez.")
        else:
            print(f"  Aparece {veces} veces.")

    # Lo mismo con las herramientas de Python. in solo responde si está o
    # no. index() devuelve la primera posición, pero marca un error si el
    # elemento no existe, por eso se usa después de revisar con in.
    # count() cuenta las apariciones, igual que en los str.
    if buscada in FRUTAS:
        print("Con Python: in da True.")
        print(f"  index() da {FRUTAS.index(buscada)}")
        print(f"  count() da {FRUTAS.count(buscada)}")
    else:
        print("Con Python: in da False y count() da 0.")

    print()
    buscada = input("Fruta: ").strip().lower()

print("Hasta luego.")
