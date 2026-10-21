"""Proyecto 004: Calculadora básica.

Pide dos números y una operación, y muestra el resultado. Avisa si intentas
dividir entre cero o si la operación no es válida.
"""

numero1 = float(input("Escribe el primer número: "))
numero2 = float(input("Escribe el segundo número: "))
operacion = input("Escribe la operación (+, -, *, /): ")

print()

# if, elif y else forman una estructura condicional: Python revisa cada
# condición en orden y ejecuta solo el bloque de la primera que se cumpla.
# Si ninguna se cumple, ejecuta el bloque de else.
# == es el operador de comparación de igualdad: da True si los dos valores son
# iguales y False si no (True y False son valores de tipo bool). No hay que
# confundirlo con =, que asigna un valor a una variable.
# Los dos puntos : abren un bloque, y las líneas con sangría de 4 espacios
# debajo son las que pertenecen a ese bloque.
if operacion == "+":
    resultado = numero1 + numero2
    print(numero1, "+", numero2, "=", resultado)
elif operacion == "-":
    resultado = numero1 - numero2
    print(numero1, "-", numero2, "=", resultado)
elif operacion == "*":
    resultado = numero1 * numero2
    print(numero1, "*", numero2, "=", resultado)
elif operacion == "/":
    # Dividir entre cero provoca un error en Python, por eso se revisa antes
    # de calcular. Este if dentro de otro bloque es un condicional anidado.
    # != es el operador de comparación de desigualdad: da True si los valores
    # son distintos.
    if numero2 != 0:
        resultado = numero1 / numero2
        print(numero1, "/", numero2, "=", resultado)
    else:
        print("No se puede dividir entre cero.")
else:
    print("La operación", operacion, "no es válida. Usa +, -, * o /.")
