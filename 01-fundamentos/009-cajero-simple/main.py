"""Proyecto 009: Cajero simple.

Simula un retiro en un cajero: parte de un saldo fijo, pide cuánto retirar y
revisa que haya saldo suficiente.
"""

SALDO_INICIAL = 5000.0

saldo = SALDO_INICIAL

print("Tu saldo disponible es", saldo)
retiro = float(input("¿Cuánto quieres retirar? "))

print()

# <= es el operador "menor o igual que" y >= es "mayor o igual que".
# Dan True también cuando los dos valores son iguales, a diferencia de < y >.
if retiro <= 0:
    print("El monto debe ser mayor que cero.")
elif saldo >= retiro:
    # Una variable se puede actualizar usando su propio valor: Python calcula
    # primero saldo - retiro y después guarda el resultado en saldo.
    saldo = saldo - retiro
    print("Retiraste", retiro)
    print("Tu nuevo saldo es", saldo)
else:
    faltante = retiro - saldo
    print("Saldo insuficiente. Te faltan", faltante, "para ese retiro.")
