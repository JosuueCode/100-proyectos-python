"""Proyecto 006: Edad en días.

Pide tu edad en años y calcula cuántos meses, semanas, días y horas has vivido,
de forma aproximada.
"""

# Estos valores no cambian durante el programa, así que se guardan como
# constantes. En Python una constante es una variable normal: escribir su
# nombre en MAYÚSCULAS es la convención de PEP 8 para indicar que no se
# modifica.
MESES_POR_ANIO = 12
SEMANAS_POR_ANIO = 52
DIAS_POR_ANIO = 365
HORAS_POR_DIA = 24

edad = int(input("¿Cuántos años tienes? "))

# Cada multiplicación guarda su resultado en una variable. Una variable con un
# resultado se puede usar en el siguiente cálculo, como dias en horas.
meses = edad * MESES_POR_ANIO
semanas = edad * SEMANAS_POR_ANIO
dias = edad * DIAS_POR_ANIO
horas = dias * HORAS_POR_DIA

print()
print("Con", edad, "años has vivido aproximadamente:")
print(meses, "meses")
print(semanas, "semanas")
print(dias, "días")
print(horas, "horas")
print()

# Es aproximado porque usa 365 días por año para todos los años
print("No cuenta los años bisiestos ni los días desde tu último cumpleaños.")
