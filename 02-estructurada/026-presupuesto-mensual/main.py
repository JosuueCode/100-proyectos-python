"""Proyecto 026: Presupuesto mensual.

Pide tu ingreso y tus gastos del mes por categoría, y muestra cuánto gastas,
cuánto te sobra y qué porcentaje de tu ingreso usas.
"""

ingreso = float(input("¿Cuál es tu ingreso mensual? "))

while ingreso <= 0:
    print("El ingreso debe ser mayor que cero.")
    ingreso = float(input("Escribe tu ingreso otra vez: "))

print()
print("Ahora escribe cuánto gastas al mes en cada categoría.")
renta = float(input("Renta: "))
comida = float(input("Comida: "))
transporte = float(input("Transporte: "))
otros = float(input("Otros gastos: "))

if renta < 0 or comida < 0 or transporte < 0 or otros < 0:
    print()
    print("Los gastos no pueden ser negativos.")
else:
    total_gastos = renta + comida + transporte + otros

    # Qué parte del ingreso se va en cada categoría
    porcentaje_renta = renta / ingreso * 100
    porcentaje_comida = comida / ingreso * 100
    porcentaje_transporte = transporte / ingreso * 100
    porcentaje_otros = otros / ingreso * 100

    # Un f-string es una cadena con una f antes de las comillas. Dentro, lo que
    # va entre llaves {} se reemplaza por su valor, así la frase se escribe
    # completa y se lee igual que va a salir en pantalla.
    # Para hacer lo mismo con +, habría que convertir cada número a texto y
    # cuidar los espacios a mano: "Ingreso: $" + str(ingreso). Con varias
    # variables eso se vuelve difícil de leer y es fácil equivocarse.
    # El :.2f después del nombre es un formato de número: muestra el valor
    # como decimal (f) con exactamente 2 decimales (.2), incluso si terminan
    # en cero. round() no hace eso: round(127.5, 2) se ve como 127.5.
    print()
    print(f"Ingreso mensual: ${ingreso:.2f}")
    print()

    # Un f-string puede tener varios valores, cada uno con su propio formato
    print("Gastos por categoría:")
    print(f"  Renta:      ${renta:.2f} ({porcentaje_renta:.1f} %)")
    print(f"  Comida:     ${comida:.2f} ({porcentaje_comida:.1f} %)")
    print(f"  Transporte: ${transporte:.2f} ({porcentaje_transporte:.1f} %)")
    print(f"  Otros:      ${otros:.2f} ({porcentaje_otros:.1f} %)")
    print()
    print(f"Total gastado: ${total_gastos:.2f}")

    # Dentro de las llaves también puede ir una operación: Python la calcula
    # y muestra el resultado con el formato indicado
    print(f"Usas el {total_gastos / ingreso * 100:.1f} % de tu ingreso.")

    if total_gastos <= ingreso:
        sobrante = ingreso - total_gastos
        print(f"Te sobran ${sobrante:.2f} al mes.")
    else:
        faltante = total_gastos - ingreso
        print(f"Gastas ${faltante:.2f} más de lo que ganas.")
