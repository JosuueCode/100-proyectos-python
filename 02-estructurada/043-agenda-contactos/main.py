"""Proyecto 043: Agenda de contactos.

Una agenda con menú para agregar, buscar, editar, eliminar y listar
contactos. Cada contacto guarda un nombre y un teléfono en un diccionario.
"""


def mostrar_menu():
    """Muestra las opciones de la agenda."""
    print("=== Agenda de contactos ===")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Editar teléfono")
    print("4. Eliminar contacto")
    print("5. Ver todos")
    print("6. Salir")


def pedir_nombre():
    """Pide un nombre y lo devuelve sin espacios extra y en tipo título."""
    # title() hace que "ana" y "ANA" se guarden igual, como "Ana"
    return input("Nombre: ").strip().title()


def pedir_telefono(mensaje):
    """Pide un teléfono hasta que no esté vacío y lo devuelve."""
    telefono = input(mensaje).strip()
    while telefono == "":
        print("El teléfono no puede estar vacío.")
        telefono = input(mensaje).strip()
    return telefono


# Un diccionario guarda pares clave: valor. La clave sirve para encontrar
# el valor, como en un diccionario de papel la palabra lleva a su
# definición. Aquí la clave es el nombre y el valor es el teléfono.
# Igual que una lista, un diccionario se puede modificar dentro de una
# función y el cambio se ve afuera.
def agregar_contacto(agenda):
    """Agrega un contacto nuevo si el nombre no existe."""
    nombre = pedir_nombre()
    # in en un diccionario revisa las claves, no los valores
    if nombre == "":
        print("El nombre no puede estar vacío.")
    elif nombre in agenda:
        print(f"{nombre} ya existe. Usa la opción 3 para editarlo.")
    else:
        telefono = pedir_telefono("Teléfono: ")
        # Asignar a una clave nueva crea el par en el diccionario
        agenda[nombre] = telefono
        print(f"Guardaste a {nombre}.")


def buscar_contacto(agenda):
    """Muestra el teléfono de un contacto si existe."""
    nombre = pedir_nombre()
    # get() devuelve el valor de la clave. Si la clave no existe, devuelve
    # el segundo valor que recibe en lugar de marcar un error, como sí
    # pasaría con agenda[nombre].
    telefono = agenda.get(nombre, "")
    if telefono == "":
        print(f"No encontré a {nombre} en tu agenda.")
    else:
        print(f"{nombre}: {telefono}")


def editar_contacto(agenda):
    """Cambia el teléfono de un contacto que ya existe."""
    nombre = pedir_nombre()
    if nombre in agenda:
        print(f"Teléfono actual: {agenda[nombre]}")
        # Asignar a una clave que ya existe reemplaza su valor
        agenda[nombre] = pedir_telefono("Teléfono nuevo: ")
        print(f"Actualizaste a {nombre}.")
    else:
        print(f"No encontré a {nombre} en tu agenda.")


def eliminar_contacto(agenda):
    """Borra un contacto de la agenda si existe."""
    nombre = pedir_nombre()
    if nombre in agenda:
        # del borra la clave y su valor. Igual que remove() en las listas,
        # marca un error si la clave no existe, por eso se revisa antes.
        del agenda[nombre]
        print(f"Eliminaste a {nombre}.")
    else:
        print(f"No encontré a {nombre} en tu agenda.")


def listar_contactos(agenda):
    """Muestra todos los contactos con su teléfono."""
    if len(agenda) == 0:
        print("Tu agenda está vacía.")
    else:
        print(f"Contactos guardados: {len(agenda)}")
        # items() entrega cada par clave y valor, que se reciben con
        # asignación múltiple. sorted() sobre los pares los ordena por la
        # clave, así la lista sale en orden alfabético.
        for nombre, telefono in sorted(agenda.items()):
            print(f"  {nombre}: {telefono}")


# Un diccionario se escribe entre llaves, como {"Ana": "555-1234"}.
# {} crea un diccionario vacío.
agenda = {}

opcion = ""

while opcion != "6":
    mostrar_menu()
    opcion = input("Elige una opción: ")
    print()

    if opcion == "1":
        agregar_contacto(agenda)
    elif opcion == "2":
        buscar_contacto(agenda)
    elif opcion == "3":
        editar_contacto(agenda)
    elif opcion == "4":
        eliminar_contacto(agenda)
    elif opcion == "5":
        listar_contactos(agenda)
    elif opcion == "6":
        print("Hasta luego.")
    else:
        print(f"La opción {opcion} no existe. Elige del 1 al 6.")

    print()
