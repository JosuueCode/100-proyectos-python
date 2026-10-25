"""Proyecto 018: Descuento de tienda.

Pide el total de la compra, aplica un descuento según el monto y muestra el
descuento y el total a pagar.
"""

# Montos a partir de los cuales cambia el descuento, y el porcentaje de cada
# rango. Al tenerlos en constantes, cambiar la promoción no obliga a tocar
# la lógica de abajo.
MONTO_DESCUENTO_MEDIO = 500
MONTO_DESCUENTO_ALTO = 1000
PORCENTAJE_MEDIO = 10
PORCENTAJE_ALTO = 20

total_compra = float(input("¿Cuál es el total de tu compra? "))

print()

if total_compra <= 0:
    print("El total debe ser mayor que cero.")
else:
    # Se revisa del monto más alto al más bajo, igual que las calificaciones
    # del proyecto 015
    if total_compra >= MONTO_DESCUENTO_ALTO:
        porcentaje = PORCENTAJE_ALTO
    elif total_compra >= MONTO_DESCUENTO_MEDIO:
        porcentaje = PORCENTAJE_MEDIO
    else:
        porcentaje = 0

    descuento = total_compra * porcentaje / 100
    total_a_pagar = total_compra - descuento

    print("Total de la compra:", round(total_compra, 2))
    print("Descuento aplicado:", porcentaje, "%")
    print("Ahorras:", round(descuento, 2))
    print("Total a pagar:", round(total_a_pagar, 2))

    if porcentaje == 0:
        print()
        print("Con compras desde", MONTO_DESCUENTO_MEDIO, "tienes descuento.")
