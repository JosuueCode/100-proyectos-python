"""Proyecto 013: Clasificador de IMC.

Pide el peso y la altura, calcula el índice de masa corporal (IMC) y dice en
qué categoría queda.
"""

peso = float(input("¿Cuánto pesas en kilogramos? "))
altura = float(input("¿Cuánto mides en metros? (por ejemplo, 1.70) "))

print()

if peso <= 0 or altura <= 0:
    print("El peso y la altura deben ser mayores que cero.")
else:
    # Fórmula del IMC: peso / altura al cuadrado. El cuadrado se escribe
    # altura * altura, y los paréntesis hacen que se calcule antes de dividir.
    imc = peso / (altura * altura)
    print("Tu IMC es", round(imc, 1))

    # En una cadena de elif las condiciones se revisan en orden y se detiene
    # en la primera que se cumple. Por eso basta con revisar el límite
    # superior: si imc llegó a la segunda condición, ya se sabe que no es
    # menor que 18.5.
    if imc < 18.5:
        print("Categoría: bajo peso")
    elif imc < 25:
        print("Categoría: peso normal")
    elif imc < 30:
        print("Categoría: sobrepeso")
    else:
        print("Categoría: obesidad")

    print()
    print("El IMC es solo una referencia; no sustituye una consulta médica.")
