"""Proyecto 042: Ordenar números.

Genera una lista de números al azar y la ordena de tres formas: con sorted(),
con sort() y con un ordenamiento burbuja hecho a mano.
"""

import random

CANTIDAD_NUMEROS = 8


def generar_numeros(cantidad):
    """Devuelve una lista con números al azar del 1 al 99."""
    numeros = []
    # _ es un nombre de variable válido. Se usa por costumbre cuando el
    # valor de la vuelta no importa y solo se quiere repetir algo
    for _ in range(cantidad):
        numeros.append(random.randint(1, 99))
    return numeros


def ordenar_burbuja(lista):
    """Devuelve una copia ordenada de la lista y muestra cada vuelta."""
    # list() crea una lista nueva con los mismos elementos. Así el
    # ordenamiento trabaja sobre la copia y la lista original no cambia.
    copia = list(lista)
    total = len(copia)

    # El ordenamiento burbuja compara cada par de vecinos y los intercambia
    # si están al revés. En cada vuelta el número más grande que falta
    # "sube" hasta el final, como una burbuja, así que la siguiente vuelta
    # ya no necesita revisar esa última posición.
    for vuelta in range(total - 1):
        for posicion in range(total - 1 - vuelta):
            actual = copia[posicion]
            siguiente = copia[posicion + 1]
            if actual > siguiente:
                # A diferencia de un str, en una lista se puede asignar un
                # valor a una posición. Con asignación múltiple los dos
                # vecinos cambian de lugar en una sola línea.
                copia[posicion], copia[posicion + 1] = siguiente, actual
        print(f"  Vuelta {vuelta + 1}: {copia}")

    return copia


numeros = generar_numeros(CANTIDAD_NUMEROS)
print(f"Lista original: {numeros}")
print()

# sorted() devuelve una lista nueva ordenada de menor a mayor y deja la
# original como estaba. Con reverse=True ordena de mayor a menor.
# reverse=True es un argumento con nombre: se indica qué parámetro recibe
# el valor escribiendo su nombre, un = y el valor.
ascendente = sorted(numeros)
descendente = sorted(numeros, reverse=True)
print("Con sorted(), la original no cambia:")
print(f"  De menor a mayor: {ascendente}")
print(f"  De mayor a menor: {descendente}")
print(f"  Original:         {numeros}")
print()

print("Con ordenamiento burbuja, paso a paso:")
con_burbuja = ordenar_burbuja(numeros)
print(f"  Resultado:  {con_burbuja}")
# == también compara listas: da True si tienen los mismos elementos en el
# mismo orden
print(f"  ¿Igual que sorted()? {con_burbuja == ascendente}")
print()

# sort() es un método que ordena la misma lista y no devuelve una nueva.
# Después de llamarlo, la lista original queda ordenada para siempre.
# También acepta reverse=True.
numeros.sort()
print("Con sort(), la original sí cambia:")
print(f"  Original después de sort(): {numeros}")
