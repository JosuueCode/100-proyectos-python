"""Proyecto 012: Validador de triángulos.

Pide la medida de tres lados, dice si pueden formar un triángulo y, si pueden,
indica si es equilátero, isósceles o escaleno.
"""

lado1 = float(input("Medida del primer lado: "))
lado2 = float(input("Medida del segundo lado: "))
lado3 = float(input("Medida del tercer lado: "))

print()

# Una comparación da True o False, y ese valor (tipo bool) se puede guardar en
# una variable como cualquier otro. Python resuelve primero la suma y después
# la comparación.
# Regla de la desigualdad del triángulo: cada par de lados debe sumar más que
# el lado que queda.
cumple1 = lado1 + lado2 > lado3
cumple2 = lado1 + lado3 > lado2
cumple3 = lado2 + lado3 > lado1

# or es un operador lógico: da True si al menos una de las condiciones es True.
# Aquí basta con que un lado no sea positivo para descartar el triángulo.
if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Todos los lados deben ser mayores que cero.")
# and es un operador lógico: da True solo si todas las condiciones son True
elif cumple1 and cumple2 and cumple3:
    print("Con esos lados sí se forma un triángulo.")

    if lado1 == lado2 and lado2 == lado3:
        print("Es equilátero: sus tres lados son iguales.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Es isósceles: tiene dos lados iguales.")
    else:
        print("Es escaleno: sus tres lados son distintos.")
else:
    print("Con esos lados no se forma un triángulo.")
    print("Cada par de lados debe sumar más que el lado que queda.")
