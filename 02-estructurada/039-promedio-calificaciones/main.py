"""Proyecto 039: Promedio de calificaciones.

Captura varias calificaciones en una lista y muestra el promedio, la más
alta, la más baja y cuántas son aprobatorias.
"""

NOTA_MINIMA = 0
NOTA_MAXIMA = 10
NOTA_APROBATORIA = 6


def pedir_cantidad():
    """Pide cuántas calificaciones se van a capturar, al menos una."""
    cantidad = int(input("¿Cuántas calificaciones vas a capturar? "))
    while cantidad < 1:
        print("Necesitas capturar al menos una calificación.")
        cantidad = int(input("¿Cuántas calificaciones vas a capturar? "))
    return cantidad


def pedir_calificacion(numero):
    """Pide una calificación válida y la devuelve como float."""
    calificacion = float(input(f"Calificación {numero}: "))
    while calificacion < NOTA_MINIMA or calificacion > NOTA_MAXIMA:
        print(f"Debe ir del {NOTA_MINIMA} al {NOTA_MAXIMA}.")
        calificacion = float(input(f"Calificación {numero}: "))
    return calificacion


def capturar_calificaciones(cantidad):
    """Pide la cantidad indicada de calificaciones y las devuelve en lista."""
    calificaciones = []
    for numero in range(1, cantidad + 1):
        calificaciones.append(pedir_calificacion(numero))
    return calificaciones


def calcular_promedio(calificaciones):
    """Devuelve el promedio de una lista de calificaciones."""
    # sum() suma todos los elementos de una lista de números. Dividir entre
    # len(), que es cuántos elementos hay, da el promedio sin escribir un
    # ciclo con acumulador.
    return sum(calificaciones) / len(calificaciones)


def contar_aprobatorias(calificaciones):
    """Devuelve cuántas calificaciones son aprobatorias."""
    aprobatorias = 0
    # Un for recorre la lista elemento por elemento, igual que recorría los
    # caracteres de un str en el proyecto 030
    for calificacion in calificaciones:
        if calificacion >= NOTA_APROBATORIA:
            aprobatorias = aprobatorias + 1
    return aprobatorias


cantidad = pedir_cantidad()
print()
calificaciones = capturar_calificaciones(cantidad)

promedio = calcular_promedio(calificaciones)
# max() y min() recorren la lista y devuelven el valor más grande y el más
# pequeño. Hacen lo mismo que la comparación del proyecto 033, pero con
# todos los elementos a la vez.
mas_alta = max(calificaciones)
mas_baja = min(calificaciones)
aprobatorias = contar_aprobatorias(calificaciones)

print()
print(f"Promedio:          {promedio:.2f}")
print(f"Calificación alta: {mas_alta}")
print(f"Calificación baja: {mas_baja}")
print(f"Aprobatorias:      {aprobatorias} de {cantidad}")

if promedio >= NOTA_APROBATORIA:
    print("El promedio es aprobatorio.")
else:
    print("El promedio no es aprobatorio.")
