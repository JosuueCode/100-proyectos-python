"""Proyecto 048: Bloc de notas.

Guarda tus notas en un archivo de texto para que sigan ahí la próxima vez
que abras el programa. Puedes escribir una nota, verlas todas y borrarlas.
"""

# El archivo se crea en la carpeta desde donde ejecutas el programa
ARCHIVO_NOTAS = "notas.txt"


def mostrar_menu():
    """Muestra las opciones del bloc de notas."""
    print("=== Bloc de notas ===")
    print("1. Escribir una nota")
    print("2. Ver mis notas")
    print("3. Borrar todas las notas")
    print("4. Salir")


def escribir_nota():
    """Agrega una nota al final del archivo."""
    nota = input("Escribe tu nota: ").strip()
    # Un return sin valor solo sale de la función. Así, si la nota está
    # vacía, no se llega a abrir el archivo.
    if nota == "":
        print("La nota está vacía, no se guardó.")
        return

    # open() abre un archivo y devuelve un objeto para trabajar con él. El
    # modo "a" (append) escribe al final sin borrar lo que ya había, y crea
    # el archivo si no existe. encoding="utf-8" asegura que los acentos y
    # la ñ se guarden bien en cualquier sistema.
    # with abre el archivo y lo cierra solo al terminar el bloque, aunque
    # ocurra un error. as le pone nombre al archivo abierto dentro del bloque.
    with open(ARCHIVO_NOTAS, "a", encoding="utf-8") as archivo:
        # write() no agrega un salto de línea, por eso se pone \n al final.
        # \n es una secuencia de escape: dentro de un texto representa el
        # salto de línea, así cada nota queda en su propia línea.
        archivo.write(f"{nota}\n")
    print("Nota guardada.")


def ver_notas():
    """Muestra las notas guardadas, numeradas."""
    # El modo "r" (read) abre el archivo solo para leer. Si el archivo no
    # existe, open() provoca un FileNotFoundError, que se atrapa con except
    # en lugar de cerrar el programa.
    try:
        with open(ARCHIVO_NOTAS, "r", encoding="utf-8") as archivo:
            # readlines() devuelve una lista con cada línea del archivo
            lineas = archivo.readlines()
    except FileNotFoundError:
        print("Todavía no tienes notas. Escribe la primera con la opción 1.")
        return

    if len(lineas) == 0:
        print("No tienes notas guardadas.")
    else:
        print("Tus notas:")
        for numero, linea in enumerate(lineas, 1):
            # strip() quita el \n del final de cada línea
            print(f"  {numero}. {linea.strip()}")


def borrar_notas():
    """Deja el archivo de notas vacío, si el usuario confirma."""
    respuesta = input("¿Seguro que quieres borrar todo? (s/n): ").strip()
    if respuesta.lower() == "s":
        # El modo "w" (write) borra todo el contenido al abrir el archivo.
        # Abrirlo sin escribir nada lo deja vacío.
        with open(ARCHIVO_NOTAS, "w", encoding="utf-8"):
            print("Borraste todas tus notas.")
    else:
        print("No se borró nada.")


opcion = ""

while opcion != "4":
    mostrar_menu()
    opcion = input("Elige una opción: ")
    print()

    if opcion == "1":
        escribir_nota()
    elif opcion == "2":
        ver_notas()
    elif opcion == "3":
        borrar_notas()
    elif opcion == "4":
        print(f"Hasta luego. Tus notas quedan en {ARCHIVO_NOTAS}.")
    else:
        print(f"La opción {opcion} no existe. Elige del 1 al 4.")

    print()
