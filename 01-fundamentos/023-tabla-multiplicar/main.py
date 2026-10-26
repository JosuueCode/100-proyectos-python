"""Proyecto 023: Tabla de multiplicar.

Pide un número y muestra su tabla de multiplicar del 1 al 10.
"""

numero = int(input("¿De qué número quieres la tabla? "))

print()
print("Tabla del", numero)

# range() es una función integrada que genera una secuencia de números enteros.
# range(1, 11) genera 1, 2, 3, ..., 10: empieza en el primer valor y se
# detiene justo antes del segundo. Por eso, para llegar hasta 10, el segundo
# valor tiene que ser 11.
# for es un ciclo que recorre una secuencia: en cada vuelta, la variable
# multiplicador toma el siguiente valor de range() y se ejecuta el bloque.
# A diferencia del while del proyecto 022, aquí no hace falta crear ni
# actualizar un contador a mano: for lo hace solo y termina al acabar la
# secuencia.
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)
