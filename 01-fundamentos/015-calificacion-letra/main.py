"""Proyecto 015: Calificación con letra.

Pide una calificación de 0 a 100 y la convierte en una letra de la A a la F.
"""

calificacion = float(input("Escribe tu calificación (de 0 a 100): "))

print()

# Comparación encadenada: 0 <= calificacion <= 100 da True solo si la
# calificación está entre 0 y 100, incluyendo los extremos. Es lo mismo que
# escribir 0 <= calificacion and calificacion <= 100, pero más corto.
if 0 <= calificacion <= 100:
    # La cadena de elif va de la letra más alta a la más baja. Como se detiene
    # en la primera condición que se cumple, un 85 no llega a revisar >= 70:
    # ya se quedó en la B.
    if calificacion >= 90:
        letra = "A"
    elif calificacion >= 80:
        letra = "B"
    elif calificacion >= 70:
        letra = "C"
    elif calificacion >= 60:
        letra = "D"
    else:
        letra = "F"

    print("Tu calificación", calificacion, "equivale a una", letra)

    if letra == "F":
        print("No te desanimes: repasa los temas y vuelve a intentarlo.")
    else:
        print("Aprobaste.")
else:
    print("La calificación debe estar entre 0 y 100.")
