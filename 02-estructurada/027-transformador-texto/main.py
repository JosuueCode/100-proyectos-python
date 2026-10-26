"""Proyecto 027: Transformador de texto.

Pide un texto y muestra un menú para transformarlo con métodos de str:
mayúsculas, minúsculas, tipo título, quitar espacios, reemplazar y contar.
"""

texto = input("Escribe un texto: ")
print()

opcion = ""

while opcion != "7":
    print("=== Transformador de texto ===")
    print(f"Texto actual: '{texto}'")
    print("1. Todo en mayúsculas")
    print("2. Todo en minúsculas")
    print("3. Tipo título")
    print("4. Quitar espacios de los extremos")
    print("5. Reemplazar una letra o palabra")
    print("6. Contar cuántas veces aparece algo")
    print("7. Salir")
    opcion = input("Elige una opción: ")
    print()

    # Un método es una función que pertenece a un tipo de dato. Se llama con
    # un punto después del valor: texto.upper(). Los métodos de str no cambian
    # el texto original, porque en Python un str no se puede modificar.
    # Lo que hacen es devolver un texto nuevo, y por eso el resultado se
    # guarda en otra variable. La variable texto sigue igual en cada vuelta.
    if opcion == "1":
        resultado = texto.upper()
        print(f"Resultado: '{resultado}'")
    elif opcion == "2":
        resultado = texto.lower()
        print(f"Resultado: '{resultado}'")
    elif opcion == "3":
        # title() pone en mayúscula la primera letra de cada palabra
        resultado = texto.title()
        print(f"Resultado: '{resultado}'")
    elif opcion == "4":
        # strip() quita los espacios del inicio y del final, no los de en
        # medio. Las comillas en el mensaje ayudan a ver la diferencia.
        resultado = texto.strip()
        print(f"Resultado: '{resultado}'")
    elif opcion == "5":
        buscar = input("¿Qué letra o palabra quieres reemplazar? ")
        nueva = input("¿Por cuál la cambias? ")
        # Algunos métodos reciben valores entre los paréntesis, igual que
        # print(). replace() recibe lo que se busca y lo que va en su lugar,
        # y cambia todas las veces que aparece.
        resultado = texto.replace(buscar, nueva)
        print(f"Resultado: '{resultado}'")
    elif opcion == "6":
        buscar = input("¿Qué letra o palabra quieres contar? ")
        # count() devuelve un número entero, no un texto. Distingue entre
        # mayúsculas y minúsculas: "A" y "a" se cuentan por separado.
        veces = texto.count(buscar)
        if veces == 1:
            print(f"'{buscar}' aparece 1 vez.")
        else:
            print(f"'{buscar}' aparece {veces} veces.")
    elif opcion == "7":
        print("Hasta luego. Tu texto original nunca cambió:")
        print(f"'{texto}'")
    else:
        print(f"La opción {opcion} no existe. Elige del 1 al 7.")

    print()
