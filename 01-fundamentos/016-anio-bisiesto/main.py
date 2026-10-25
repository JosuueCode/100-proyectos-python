"""Proyecto 016: Año bisiesto.

Pide un año y dice si es bisiesto, aplicando la regla completa del calendario.
"""

anio = int(input("Escribe un año: "))

print()

# Regla del año bisiesto: es divisible entre 4, pero no entre 100,
# salvo que también sea divisible entre 400.
# "Divisible entre 4" se revisa con el operador módulo: anio % 4 == 0.
# Los paréntesis agrupan las dos primeras condiciones para que se evalúen
# juntas. Python ya resuelve and antes que or, pero con paréntesis la regla
# se lee igual que se dice.
es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

if anio <= 0:
    print("Escribe un año mayor que cero.")
elif es_bisiesto:
    print(anio, "es bisiesto: tiene 366 días y febrero tiene 29.")
else:
    print(anio, "no es bisiesto: tiene 365 días y febrero tiene 28.")
