"""Proyecto 022: Cuenta regresiva.

Pide un número y cuenta hacia atrás desde ese número hasta cero.
"""

inicio = int(input("¿Desde qué número quieres contar? "))

# Misma validación del proyecto 021: no se avanza con un número negativo
while inicio < 0:
    print("El número debe ser cero o mayor.")
    inicio = int(input("Escribe el número otra vez: "))

print()

# Un contador es una variable que cambia en cada vuelta de un ciclo para llevar
# la cuenta. Empieza en el número que escribiste y baja de uno en uno.
contador = inicio

# La condición se revisa antes de cada vuelta. Mientras contador sea 0 o más,
# se muestra y se le resta 1. Cuando llega a -1, la condición da False y el
# ciclo termina.
while contador >= 0:
    print(contador)
    # Actualizar el contador es lo que acerca el ciclo a su fin. Si se borrara
    # esta línea, contador valdría siempre lo mismo, la condición daría True
    # para siempre y el programa quedaría en un ciclo infinito. Si te pasa al
    # probar, detenlo con Ctrl + C.
    contador = contador - 1

print("¡Despegue!")
