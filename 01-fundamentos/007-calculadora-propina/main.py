"""Proyecto 007: Calculadora de propina.

Pide el total de la cuenta y el porcentaje de propina, y muestra cuánto dejar
de propina y cuánto pagar en total.
"""

total_cuenta = float(input("¿Cuánto es el total de la cuenta? "))
porcentaje = float(input("¿Qué porcentaje de propina quieres dejar? "))

# Un porcentaje es una parte de 100: el 15 % de algo es ese algo por 15 / 100.
# Por la jerarquía de operaciones, aquí se multiplica primero y después
# se divide.
propina = total_cuenta * porcentaje / 100
total_a_pagar = total_cuenta + propina

# round() con 2 como segundo valor deja dos decimales, como en el dinero
print()
print("Propina:", round(propina, 2))
print("Total a pagar:", round(total_a_pagar, 2))
