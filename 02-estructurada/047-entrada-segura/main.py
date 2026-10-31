"""Proyecto 047: Entrada segura.

Pide números sin que el programa se detenga si escribes letras, y calcula
un promedio de puntos por partido cuidando la división entre cero.
"""


def pedir_entero(mensaje, minimo, maximo):
    """Pide un entero entre minimo y maximo hasta que sea válido."""
    # while True repite el ciclo sin condición de salida. La única forma de
    # salir es el return, que se ejecuta cuando el dato ya es válido.
    while True:
        texto = input(mensaje)
        # try marca un bloque que puede fallar. Si una línea de adentro
        # provoca un error, Python no detiene el programa: salta al except
        # que corresponde a ese tipo de error.
        try:
            numero = int(texto)
            if minimo <= numero <= maximo:
                return numero
            print(f"Debe estar entre {minimo} y {maximo}.")
        # int() provoca un ValueError cuando el texto no es un entero, como
        # "abc", "3.5" o un texto vacío. Aquí se avisa y el ciclo vuelve a
        # pedir el dato, en lugar de que el programa se cierre.
        except ValueError:
            print(f"'{texto}' no es un número entero. Intenta otra vez.")


def calcular_promedio(puntos, partidos):
    """Devuelve los puntos por partido, o 0 si no hubo partidos."""
    # Dividir entre cero provoca un ZeroDivisionError. Antes se evitaba
    # revisando el divisor con un if; con try se intenta la operación y,
    # si falla, se decide qué hacer en el except.
    try:
        return puntos / partidos
    except ZeroDivisionError:
        print("Sin partidos jugados no se puede sacar un promedio.")
        return 0


print("Escribe lo que quieras: el programa no se va a cerrar por un error.")
print()

puntos = pedir_entero("¿Cuántos puntos anotaste? (0 a 5000) ", 0, 5000)
partidos = pedir_entero("¿Cuántos partidos jugaste? (0 a 100) ", 0, 100)

promedio = calcular_promedio(puntos, partidos)

print()
print(f"Puntos: {puntos}")
print(f"Partidos: {partidos}")
print(f"Promedio por partido: {promedio:.2f}")
