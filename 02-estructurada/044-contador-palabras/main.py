"""Proyecto 044: Contador de palabras.

Pide un texto, cuenta cuántas veces aparece cada palabra con un diccionario
y muestra cuál es la más frecuente.
"""

# Signos de puntuación que se quitan antes de contar
SIGNOS = ".,;:!?¡¿()"


def limpiar_texto(texto):
    """Devuelve el texto en minúsculas y sin signos de puntuación."""
    limpio = texto.lower()
    # Se recorre cada signo y se reemplaza por un texto vacío, para que
    # "hola," y "hola" cuenten como la misma palabra
    for signo in SIGNOS:
        limpio = limpio.replace(signo, "")
    return limpio


def separar_palabras(texto):
    """Devuelve una lista con las palabras del texto."""
    # split() corta el texto en cada espacio y devuelve una lista con los
    # pedazos. Si hay varios espacios seguidos, no deja pedazos vacíos.
    return texto.split()


def contar_palabras(palabras):
    """Devuelve un diccionario con cada palabra y sus apariciones."""
    conteo = {}
    for palabra in palabras:
        # get() devuelve 0 la primera vez que aparece la palabra, porque
        # todavía no es clave del diccionario. Así una sola línea sirve
        # tanto para crear la clave como para sumarle uno.
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def palabra_mas_frecuente(conteo):
    """Devuelve la palabra que más se repite y cuántas veces aparece."""
    mas_frecuente = ""
    mayor_cantidad = 0
    # Se guarda la mejor hasta el momento y se reemplaza solo si aparece
    # una con más repeticiones. Si hay empate, gana la que salió primero.
    for palabra, cantidad in conteo.items():
        if cantidad > mayor_cantidad:
            mas_frecuente = palabra
            mayor_cantidad = cantidad
    # Una función puede devolver varios valores separados por comas, y se
    # reciben con asignación múltiple
    return mas_frecuente, mayor_cantidad


texto = input("Escribe un texto: ")
palabras = separar_palabras(limpiar_texto(texto))

if len(palabras) == 0:
    print("No escribiste ninguna palabra.")
else:
    conteo = contar_palabras(palabras)
    palabra, cantidad = palabra_mas_frecuente(conteo)

    print()
    print("Veces que aparece cada palabra:")
    for palabra_contada, veces in conteo.items():
        print(f"  {palabra_contada}: {veces}")

    print()
    print(f"Palabras en total: {len(palabras)}")
    print(f"Palabras distintas: {len(conteo)}")
    if cantidad == 1:
        print("Ninguna palabra se repite.")
    else:
        print(f"La más frecuente es '{palabra}', con {cantidad} apariciones.")
