"""Proyecto 040: Eliminar duplicados.

Pide una serie de palabras y quita las repetidas de dos formas: con un set,
que pierde el orden, y con un ciclo for, que conserva el orden original.
"""


def pedir_elementos():
    """Pide palabras hasta recibir una vacía y las devuelve en una lista."""
    elementos = []
    elemento = input("Palabra: ").strip().lower()
    while elemento != "":
        elementos.append(elemento)
        elemento = input("Palabra: ").strip().lower()
    return elementos


def quitar_con_set(lista):
    """Devuelve los elementos sin repetir, usando un set."""
    # Un set es una colección que no admite elementos repetidos: al
    # convertir la lista con set(), cada valor queda una sola vez.
    # A cambio, un set no guarda posiciones, así que el orden en que salen
    # los elementos no tiene que ver con el de la lista y puede cambiar de
    # una ejecución a otra. list() convierte el set de vuelta en una lista.
    return list(set(lista))


def quitar_conservando_orden(lista):
    """Devuelve los elementos sin repetir, en el orden en que aparecieron."""
    sin_repetir = []
    for elemento in lista:
        # not invierte un valor bool: True se vuelve False y al revés.
        # not in da True si el elemento todavía no está en la lista, así que
        # solo se agrega la primera vez que aparece.
        if elemento not in sin_repetir:
            sin_repetir.append(elemento)
    return sin_repetir


print("Escribe palabras, algunas repetidas.")
print("Deja el texto vacío para terminar.")
palabras = pedir_elementos()

if len(palabras) == 0:
    print("No escribiste ninguna palabra.")
else:
    con_set = quitar_con_set(palabras)
    con_orden = quitar_conservando_orden(palabras)
    repetidas = len(palabras) - len(con_orden)

    # Al poner una lista dentro de un f-string, Python la muestra como se
    # escribe en el código: entre corchetes y con comillas en cada texto
    print()
    print(f"Lista original:    {palabras}")
    print(f"Con set:           {con_set}")
    print(f"Conservando orden: {con_orden}")
    print()

    if repetidas == 0:
        print("No había palabras repetidas.")
    elif repetidas == 1:
        print("Se quitó 1 palabra repetida.")
    else:
        print(f"Se quitaron {repetidas} palabras repetidas.")
