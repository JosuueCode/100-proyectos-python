# 034 Calculadora con funciones

Una calculadora con menú para sumar, restar, multiplicar y dividir dos
números. Se repite hasta que eliges salir y, antes de dividir, revisa que el
divisor no sea cero.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a organizar un programa completo con funciones. Compáralo
con la calculadora del proyecto 004: allá todo el cálculo y lo que se muestra
en pantalla estaba junto dentro de cada `if`, y la línea de `print()` se
repetía casi igual cuatro veces. Aquí cada operación vive en su propia función
con un nombre que dice lo que hace, el menú y la forma de mostrar el resultado
se escriben una sola vez, y el ciclo principal solo decide qué función llamar.

Así, si quieres agregar una operación nueva, escribes una función más y una
rama en el menú, sin tocar el resto del código.

No hay símbolos nuevos, pero vas a ver dos tipos de funciones: las que
devuelven un valor con `return`, como `sumar()`, y las que solo hacen algo sin
devolver nada, como `mostrar_menu()`.
