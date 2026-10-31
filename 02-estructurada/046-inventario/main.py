"""Proyecto 046: Inventario.

Administra el inventario de una papelería: agrega productos, actualiza
existencias, registra ventas y calcula el valor total de la mercancía.
"""


def mostrar_menu():
    """Muestra las opciones del inventario."""
    print("=== Inventario ===")
    print("1. Agregar producto")
    print("2. Agregar existencias")
    print("3. Vender")
    print("4. Ver inventario")
    print("5. Salir")


def pedir_nombre():
    """Pide el nombre de un producto, sin espacios extra y en minúsculas."""
    return input("Producto: ").strip().lower()


def pedir_cantidad(mensaje):
    """Pide una cantidad entera mayor que cero."""
    cantidad = int(input(mensaje))
    while cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
        cantidad = int(input(mensaje))
    return cantidad


def pedir_precio():
    """Pide un precio mayor que cero."""
    precio = float(input("Precio por unidad: "))
    while precio <= 0:
        print("El precio debe ser mayor que cero.")
        precio = float(input("Precio por unidad: "))
    return precio


def agregar_producto(inventario):
    """Agrega un producto nuevo con su precio y su cantidad."""
    nombre = pedir_nombre()
    if nombre == "":
        print("El nombre no puede estar vacío.")
    elif nombre in inventario:
        print(f"{nombre} ya existe. Usa la opción 2 para sumar unidades.")
    else:
        precio = pedir_precio()
        cantidad = pedir_cantidad("Cantidad inicial: ")
        # El valor de la clave es otro diccionario, con sus propias claves
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}
        print(f"Agregaste {cantidad} unidades de {nombre}.")


def agregar_existencias(inventario):
    """Suma unidades a un producto que ya existe."""
    nombre = pedir_nombre()
    if nombre in inventario:
        unidades = pedir_cantidad("¿Cuántas unidades llegaron? ")
        # Con dos pares de corchetes se entra primero al producto y después
        # a su dato: inventario[nombre] es el diccionario del producto y
        # inventario[nombre]["cantidad"] es el número dentro de él
        actual = inventario[nombre]["cantidad"]
        inventario[nombre]["cantidad"] = actual + unidades
        # Dentro de un f-string con comillas dobles, la clave se escribe con
        # comillas simples para no cerrar el texto antes de tiempo
        print(f"Ahora hay {inventario[nombre]['cantidad']} de {nombre}.")
    else:
        print(f"{nombre} no está en el inventario.")


def vender(inventario):
    """Descuenta unidades vendidas si hay suficientes."""
    nombre = pedir_nombre()
    if nombre in inventario:
        # Guardar el diccionario del producto en una variable acorta las
        # líneas. Los cambios en producto se ven en el inventario, porque
        # las dos variables apuntan al mismo diccionario.
        producto = inventario[nombre]
        unidades = pedir_cantidad("¿Cuántas unidades vendes? ")
        if unidades > producto["cantidad"]:
            print(f"Solo hay {producto['cantidad']} de {nombre}.")
        else:
            producto["cantidad"] = producto["cantidad"] - unidades
            total_venta = unidades * producto["precio"]
            print(f"Vendiste {unidades} de {nombre} por ${total_venta:.2f}.")
            print(f"Quedan {producto['cantidad']}.")
    else:
        print(f"{nombre} no está en el inventario.")


def calcular_valor_total(inventario):
    """Devuelve el valor de toda la mercancía: precio por cantidad."""
    valor_total = 0
    # values() entrega solo los valores del diccionario, sin las claves.
    # Aquí cada valor es el diccionario con el precio y la cantidad.
    for producto in inventario.values():
        valor_total = valor_total + producto["precio"] * producto["cantidad"]
    return valor_total


def mostrar_inventario(inventario):
    """Muestra cada producto con su precio, cantidad y valor."""
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        for nombre, producto in sorted(inventario.items()):
            cantidad = producto["cantidad"]
            precio = producto["precio"]
            valor = precio * cantidad
            print(f"  {nombre}: {cantidad} x ${precio:.2f} = ${valor:.2f}")
        print(f"Valor total: ${calcular_valor_total(inventario):.2f}")


# Un diccionario anidado tiene otros diccionarios como valores. Cada
# producto es una clave, y su valor guarda el precio y la cantidad.
# Escrito en varias líneas se lee mejor. La coma después del último par es
# opcional y facilita agregar productos después.
inventario = {
    "lápiz": {"precio": 5.5, "cantidad": 20},
    "cuaderno": {"precio": 32.0, "cantidad": 10},
    "borrador": {"precio": 4.0, "cantidad": 15},
}

opcion = ""

while opcion != "5":
    mostrar_menu()
    opcion = input("Elige una opción: ")
    print()

    if opcion == "1":
        agregar_producto(inventario)
    elif opcion == "2":
        agregar_existencias(inventario)
    elif opcion == "3":
        vender(inventario)
    elif opcion == "4":
        mostrar_inventario(inventario)
    elif opcion == "5":
        print("Hasta luego.")
    else:
        print(f"La opción {opcion} no existe. Elige del 1 al 5.")

    print()
