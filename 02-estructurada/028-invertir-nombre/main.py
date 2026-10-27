"""Proyecto 028: Invertir nombre.

Pide tu nombre y lo recorta de varias formas con índices y slicing: la primera
letra, la última, una parte del nombre y el nombre al revés.
"""

# strip() se aplica directo al texto que devuelve input(), así se quitan los
# espacios de los extremos antes de guardar el nombre
nombre = input("¿Cómo te llamas? ").strip()

while nombre == "":
    print("El nombre no puede estar vacío.")
    nombre = input("Escribe tu nombre otra vez: ").strip()

# Cada carácter de un str tiene una posición, llamada índice, que empieza
# en 0. Con corchetes se toma el carácter de una posición: nombre[0] es la
# primera letra. Un índice negativo cuenta desde el final: nombre[-1] es la
# última letra, sin tener que saber cuántas tiene el nombre.
primera_letra = nombre[0]
ultima_letra = nombre[-1]

print()
print(f"Tu nombre tiene {len(nombre)} caracteres.")
print(f"Primera letra: {primera_letra}")
print(f"Última letra: {ultima_letra}")

# El slicing toma un pedazo del texto con la forma [inicio:fin:paso].
# inicio es la posición donde empieza, fin es donde se detiene sin incluirla,
# y paso dice de cuánto en cuánto avanza, igual que en range().
# Si un valor se omite, Python usa el inicio del texto, el final del texto
# o un paso de 1. Si el fin pasa del largo del texto, no hay error: el
# pedazo llega hasta donde haya letras.
primeras_tres = nombre[0:3]
desde_la_segunda = nombre[1:]
saltando_una = nombre[::2]

print()
print(f"Primeras tres letras [0:3]: {primeras_tres}")
print(f"Desde la segunda letra [1:]: {desde_la_segunda}")
print(f"Una letra sí y otra no [::2]: {saltando_una}")

# Con un paso negativo el slicing avanza hacia atrás. Sin inicio ni fin,
# [::-1] recorre todo el texto desde la última letra hasta la primera.
nombre_al_reves = nombre[::-1]

print()
print(f"Tu nombre al revés [::-1]: {nombre_al_reves}")

# El slicing también devuelve un texto nuevo, así que se puede combinar con
# un método. Aquí cada palabra del nombre al revés empieza con mayúscula.
print(f"Al revés y en tipo título: {nombre_al_reves.title()}")
