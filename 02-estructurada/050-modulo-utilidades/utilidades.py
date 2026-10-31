"""Funciones reutilizables para pedir datos y mostrar resultados.

Este archivo es un módulo propio: cualquier programa de la misma carpeta
puede usar sus funciones con import utilidades.
"""


def pedir_entero(mensaje, minimo, maximo):
    """Pide un entero entre minimo y maximo hasta que sea válido."""
    while True:
        texto = input(mensaje)
        try:
            numero = int(texto)
            if minimo <= numero <= maximo:
                return numero
            print(f"Debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print(f"'{texto}' no es un número entero. Intenta otra vez.")


def pedir_decimal(mensaje, minimo):
    """Pide un número decimal mayor o igual que minimo."""
    while True:
        texto = input(mensaje)
        try:
            numero = float(texto)
            if numero >= minimo:
                return numero
            print(f"Debe ser {minimo} o más.")
        except ValueError:
            print(f"'{texto}' no es un número. Intenta otra vez.")


def pedir_texto(mensaje):
    """Pide un texto que no esté vacío y lo devuelve sin espacios extra."""
    texto = input(mensaje).strip()
    while texto == "":
        print("Este dato no puede quedar vacío.")
        texto = input(mensaje).strip()
    return texto


def confirmar(mensaje):
    """Hace una pregunta de sí o no y devuelve True o False."""
    respuesta = input(f"{mensaje} (s/n): ").strip().lower()
    while respuesta != "s" and respuesta != "n":
        print("Responde con s o n.")
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
    return respuesta == "s"


def formatear_dinero(cantidad):
    """Devuelve la cantidad como texto de dinero, por ejemplo $12.50."""
    return f"${cantidad:.2f}"


# Cada archivo de Python tiene una variable especial llamada __name__.
# Cuando ejecutas este archivo directamente, Python le pone el valor
# "__main__". Cuando otro archivo lo importa, __name__ vale el nombre del
# módulo, "utilidades". Así este bloque solo corre si ejecutas
# python utilidades.py, y no cada vez que otro programa hace el import.
if __name__ == "__main__":
    print("Este archivo es un módulo de utilidades.")
    print(f"Ahora __name__ vale '{__name__}' porque lo ejecutaste directo.")
    print(f"Prueba de formatear_dinero(7.5): {formatear_dinero(7.5)}")
