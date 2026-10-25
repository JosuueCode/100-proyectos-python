"""Proyecto 017: Nombre del día de la semana.

Pide un número del 1 al 7 y muestra el día de la semana que le corresponde,
empezando por el lunes.
"""

numero = int(input("Escribe un número del 1 al 7: "))

print()

# Primero se valida el rango. Así la cadena de elif de adentro solo trabaja
# con números que sí tienen un día asignado.
if 1 <= numero <= 7:
    if numero == 1:
        dia = "lunes"
    elif numero == 2:
        dia = "martes"
    elif numero == 3:
        dia = "miércoles"
    elif numero == 4:
        dia = "jueves"
    elif numero == 5:
        dia = "viernes"
    elif numero == 6:
        dia = "sábado"
    else:
        # Si el número está entre 1 y 7 y no fue ninguno de los anteriores,
        # solo puede ser 7
        dia = "domingo"

    print("El día", numero, "de la semana es", dia)

    if numero >= 6:
        print("Es fin de semana.")
    else:
        print("Es día entre semana.")
else:
    print("El número", numero, "está fuera de rango.")
    print("Usa un número del 1 al 7.")
