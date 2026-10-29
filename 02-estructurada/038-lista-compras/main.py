"""Proyecto 038: Lista de compras.

Un menú para armar tu lista de compras: agregar y quitar productos, verla
numerada y vaciarla. Cada acción está en su propia función.
"""


def mostrar_menu():
    """Muestra las opciones del menú."""
    print("=== Lista de compras ===")
    print("1. Agregar producto")
    print("2. Quitar producto")
    print("3. Ver lista")
    print("4. Vaciar lista")
    print("5. Salir")


def pedir_producto(mensaje):
    """Pide el nombre de un producto, sin espacios extra y en minúsculas."""
    return input(mensaje).strip().lower()


# Una lista guarda varios valores en orden dentro de una sola variable. Se
# escribe entre corchetes, con los elementos separados por comas, como
# ["leche", "pan"]. La lista de compras se crea más abajo, vacía.
# Estas funciones reciben la lista como parámetro y la cambian directamente.
# A diferencia de un str, una lista sí se puede modificar, así que los
# cambios que hace la función se ven en la lista original y no hace falta
# devolverla con return.
def agregar_producto(lista):
    """Agrega un producto a la lista si no está vacío ni repetido."""
    producto = pedir_producto("¿Qué producto quieres agregar? ")

    # in también funciona con listas: da True si el valor es uno de los
    # elementos de la lista
    if producto == "":
        print("No escribiste ningún producto.")
    elif producto in lista:
        print(f"{producto} ya está en tu lista.")
    else:
        # append() es un método de las listas que agrega un elemento al final
        lista.append(producto)
        print(f"Agregaste {producto}.")


def quitar_producto(lista):
    """Quita un producto de la lista si está en ella."""
    producto = pedir_producto("¿Qué producto quieres quitar? ")

    # remove() quita la primera vez que aparece el valor. Si el valor no
    # está en la lista, Python marca un error, por eso se revisa antes con in.
    if producto == "":
        print("No escribiste ningún producto.")
    elif producto in lista:
        lista.remove(producto)
        print(f"Quitaste {producto}.")
    else:
        print(f"{producto} no está en tu lista.")


def ver_lista(lista):
    """Muestra los productos numerados y cuántos son."""
    # len() también cuenta los elementos de una lista, igual que contaba
    # los caracteres de un str
    cantidad = len(lista)
    if cantidad == 0:
        print("Tu lista está vacía.")
    else:
        if cantidad == 1:
            print("Tu lista tiene 1 producto:")
        else:
            print(f"Tu lista tiene {cantidad} productos:")
        # enumerate() recorre la lista y en cada vuelta entrega dos valores:
        # la posición y el elemento. Se reciben con asignación múltiple, como
        # en el proyecto 036. El 1 indica que la cuenta empiece en 1 y no
        # en 0, que es como cuentan las personas.
        for numero, producto in enumerate(lista, 1):
            print(f"  {numero}. {producto}")


def vaciar_lista(lista):
    """Quita todos los productos de la lista."""
    # clear() deja la lista sin elementos. Escribir lista = [] aquí no
    # serviría: crearía una lista nueva solo dentro de la función.
    lista.clear()
    print("Tu lista quedó vacía.")


# [] crea una lista vacía, sin elementos, que se va llenando con append()
lista_compras = []

opcion = ""

while opcion != "5":
    mostrar_menu()
    opcion = input("Elige una opción: ")
    print()

    if opcion == "1":
        agregar_producto(lista_compras)
    elif opcion == "2":
        quitar_producto(lista_compras)
    elif opcion == "3":
        ver_lista(lista_compras)
    elif opcion == "4":
        vaciar_lista(lista_compras)
    elif opcion == "5":
        print("Hasta luego. Que te vaya bien con las compras.")
    else:
        print(f"La opción {opcion} no existe. Elige del 1 al 5.")

    print()
