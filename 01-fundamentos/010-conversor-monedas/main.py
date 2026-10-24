"""Proyecto 010: Conversor de monedas.

Convierte una cantidad en pesos mexicanos a dólares, euros o yenes usando
tasas de cambio fijas.
"""

# Cuántos pesos cuesta una unidad de cada moneda. Son valores de ejemplo:
# las tasas reales cambian todos los días.
PESOS_POR_DOLAR = 18.50
PESOS_POR_EURO = 20.00
PESOS_POR_YEN = 0.12

print("Aviso: las tasas de cambio de este programa son de ejemplo,")
print("no son reales.")
print()

pesos = float(input("¿Cuántos pesos mexicanos quieres convertir? "))

print("1. Dólares")
print("2. Euros")
print("3. Yenes")
opcion = input("¿A qué moneda los quieres convertir? ")

print()

# Si un dólar cuesta 18.50 pesos, la cantidad de dólares es pesos / 18.50
if pesos <= 0:
    print("La cantidad debe ser mayor que cero.")
elif opcion == "1":
    dolares = pesos / PESOS_POR_DOLAR
    print(pesos, "pesos son", round(dolares, 2), "dólares")
elif opcion == "2":
    euros = pesos / PESOS_POR_EURO
    print(pesos, "pesos son", round(euros, 2), "euros")
elif opcion == "3":
    yenes = pesos / PESOS_POR_YEN
    print(pesos, "pesos son", round(yenes, 2), "yenes")
else:
    print("La opción", opcion, "no existe. Elige un número del 1 al 3.")
