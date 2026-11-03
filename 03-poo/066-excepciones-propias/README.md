# 066 Excepciones personalizadas

Un programa con una cuenta bancaria que, cuando algo sale mal, lanza sus
propios errores: `MontoInvalidoError` si la cantidad es cero o negativa y
`SaldoInsuficienteError` si quieres retirar más de lo que hay. El programa
hace retiros, depósitos y hasta intenta crear una cuenta con saldo negativo,
y te muestra cómo se atiende cada error.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a crear tus propias excepciones. Son clases que heredan
de `Exception`, y entre ellas forman una jerarquía: las dos heredan de
`ErrorCuenta`, así que puedes atrapar un error concreto o cualquiera de los
dos con un solo `except ErrorCuenta`. Con `raise` lanzas el error justo donde
se detecta el problema.

Compáralo con el proyecto 052. Ahí `retirar()` devolvía `False` y mostraba un
mensaje. Eso tiene dos problemas: si quien llama al método no revisa el
`False`, el programa sigue como si nada, y el mensaje queda fijo dentro de la
clase. Una excepción no se puede ignorar sin querer: si nadie la atrapa, el
programa se detiene y te dice qué pasó. Además lleva información, como
`error.faltante`, y cada programa decide qué hacer con ella: mostrar un
mensaje, pedir otra cantidad o guardarlo en un registro.

También vas a completar el bloque `try` con dos partes nuevas: `else`, que
solo se ejecuta si no hubo error, y `finally`, que se ejecuta siempre.

Símbolos y sintaxis nuevos: `raise`, las excepciones propias que heredan de
`Exception`, la clase base `Exception` y los bloques `else` y `finally` de
`try`.
