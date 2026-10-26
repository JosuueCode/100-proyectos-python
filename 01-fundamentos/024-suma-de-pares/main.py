"""Proyecto 024: Suma de números pares.

Pide un límite y suma todos los números pares desde 2 hasta ese límite.
"""

limite = int(input("¿Hasta qué número quieres sumar los pares? "))

while limite < 0:
    print("El límite debe ser cero o mayor.")
    limite = int(input("Escribe el límite otra vez: "))

# Acumulador: una variable que empieza en 0 y en cada vuelta del ciclo recibe
# lo que vale ella más el nuevo valor. Al terminar, guarda el total.
suma = 0
# Contador: también empieza en 0, pero en cada vuelta solo suma 1
cantidad_pares = 0

# range() con tres valores: inicio, fin y paso. El paso es cuánto avanza en
# cada vuelta. range(2, limite + 1, 2) genera 2, 4, 6, ... sin pasar del
# límite. Se usa limite + 1 porque range() se detiene antes del fin, y así el
# límite queda incluido si es par.
for numero_par in range(2, limite + 1, 2):
    suma = suma + numero_par
    cantidad_pares = cantidad_pares + 1

print()

# Si el límite es menor que 2, range() no genera ningún número, el ciclo no da
# ni una vuelta y el contador se queda en 0
if cantidad_pares == 0:
    print("No hay números pares desde 2 hasta", limite)
else:
    print("Números pares sumados:", cantidad_pares)
    print("La suma de los pares desde 2 hasta", limite, "es", suma)
