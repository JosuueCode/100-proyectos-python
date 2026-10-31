"""Proyecto 049: Registro de gastos en CSV.

Registra tus gastos con fecha, categoría y monto en un archivo CSV, y muestra
el total general y el total por categoría.
"""

# csv es un módulo de la biblioteca estándar para leer y escribir archivos
# CSV: texto donde cada línea es un registro y los datos van separados por
# comas, como una hoja de cálculo sencilla
import csv

ARCHIVO_GASTOS = "gastos.csv"
CAMPOS = ["fecha", "categoria", "monto"]


def mostrar_menu():
    """Muestra las opciones del registro."""
    print("=== Registro de gastos ===")
    print("1. Registrar un gasto")
    print("2. Ver gastos y totales")
    print("3. Salir")


def pedir_texto(mensaje):
    """Pide un texto que no esté vacío."""
    texto = input(mensaje).strip()
    while texto == "":
        print("Este dato no puede quedar vacío.")
        texto = input(mensaje).strip()
    return texto


def pedir_monto():
    """Pide un monto mayor que cero, sin cerrar el programa con letras."""
    while True:
        texto = input("Monto: ")
        try:
            monto = float(texto)
            if monto > 0:
                return monto
            print("El monto debe ser mayor que cero.")
        except ValueError:
            print(f"'{texto}' no es un número. Intenta otra vez.")


def archivo_existe():
    """Devuelve True si el archivo de gastos ya existe."""
    try:
        with open(ARCHIVO_GASTOS, "r", encoding="utf-8"):
            return True
    except FileNotFoundError:
        return False


def registrar_gasto():
    """Pide los datos de un gasto y los agrega al archivo CSV."""
    fecha = pedir_texto("Fecha (por ejemplo 2026-10-30): ")
    categoria = pedir_texto("Categoría (comida, transporte...): ").lower()
    monto = pedir_monto()

    # Hay que saberlo antes de abrir el archivo, porque el modo "a" lo crea
    # si no existe y ya no se podría distinguir un archivo nuevo
    es_nuevo = not archivo_existe()

    # newline="" es necesario al escribir un CSV: el módulo csv pone sus
    # propios saltos de línea, y sin esto en Windows quedan líneas vacías
    # entre cada registro
    with open(ARCHIVO_GASTOS, "a", newline="", encoding="utf-8") as archivo:
        # DictWriter escribe cada registro a partir de un diccionario. Las
        # claves del diccionario tienen que coincidir con fieldnames, que es
        # la lista de columnas y define su orden.
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        # La primera línea de un CSV suele ser el encabezado con los nombres
        # de las columnas. Solo se escribe cuando el archivo es nuevo.
        if es_nuevo:
            escritor.writeheader()
        escritor.writerow({
            "fecha": fecha,
            "categoria": categoria,
            "monto": f"{monto:.2f}",
        })
    print(f"Guardaste un gasto de ${monto:.2f} en {categoria}.")


def leer_gastos():
    """Devuelve una lista con los gastos guardados, cada uno un diccionario."""
    gastos = []
    # Si no se indica el modo, open() usa "r", el modo de lectura
    try:
        with open(ARCHIVO_GASTOS, newline="", encoding="utf-8") as archivo:
            # DictReader usa el encabezado como claves y entrega cada línea
            # como un diccionario, por ejemplo {"fecha": "2026-10-30",
            # "categoria": "comida", "monto": "85.50"}
            for fila in csv.DictReader(archivo):
                gastos.append(fila)
    except FileNotFoundError:
        print("Todavía no hay gastos registrados.")
    return gastos


def mostrar_resumen(gastos):
    """Muestra cada gasto, el total general y el total por categoría."""
    total_general = 0
    totales_por_categoria = {}

    print("Gastos registrados:")
    for gasto in gastos:
        # Todo lo que se lee de un CSV es texto, así que el monto se
        # convierte a float antes de sumarlo
        monto = float(gasto["monto"])
        categoria = gasto["categoria"]
        print(f"  {gasto['fecha']}  {categoria}: ${monto:.2f}")

        total_general = total_general + monto
        anterior = totales_por_categoria.get(categoria, 0)
        totales_por_categoria[categoria] = anterior + monto

    print()
    print("Total por categoría:")
    for categoria, total in sorted(totales_por_categoria.items()):
        print(f"  {categoria}: ${total:.2f}")
    print()
    print(f"Total general: ${total_general:.2f}")


opcion = ""

while opcion != "3":
    mostrar_menu()
    opcion = input("Elige una opción: ")
    print()

    if opcion == "1":
        registrar_gasto()
    elif opcion == "2":
        gastos = leer_gastos()
        if len(gastos) > 0:
            mostrar_resumen(gastos)
    elif opcion == "3":
        print(f"Hasta luego. Tus gastos quedan en {ARCHIVO_GASTOS}.")
    else:
        print(f"La opción {opcion} no existe. Elige del 1 al 3.")

    print()
