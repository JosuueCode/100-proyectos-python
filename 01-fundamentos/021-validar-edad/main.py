"""Proyecto 021: Validar edad.

Pide tu edad y la vuelve a pedir hasta que esté dentro de un rango válido.
"""

EDAD_MINIMA = 0
EDAD_MAXIMA = 120

edad = int(input("¿Cuántos años tienes? "))

# while es un ciclo: repite el bloque con sangría mientras su condición sea
# True. Antes de cada vuelta revisa la condición otra vez; cuando da False,
# el ciclo termina y el programa sigue con lo que está debajo.
# Aquí la condición da True cuando la edad está fuera del rango, así que el
# programa no avanza hasta recibir una edad válida. Si la primera ya es
# válida, la condición da False desde el inicio y el bloque no se ejecuta.
while edad < EDAD_MINIMA or edad > EDAD_MAXIMA:
    print("La edad debe estar entre", EDAD_MINIMA, "y", EDAD_MAXIMA, "años.")
    # Volver a pedir la edad es lo que permite que la condición cambie.
    # Sin esta línea, edad nunca cambiaría y el ciclo no terminaría.
    edad = int(input("Escribe tu edad otra vez: "))

# Si el programa llega aquí, la edad ya pasó la validación
print()
print("Edad registrada:", edad, "años")

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
