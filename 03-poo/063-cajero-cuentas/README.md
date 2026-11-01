# 063 Cajero con varias cuentas

Un cajero automático con tres cuentas de prueba. Escribes tu número de cuenta
y tu PIN, con un máximo de tres intentos, y después puedes consultar tu
saldo, depositar, retirar y transferir dinero a otra cuenta. Si escribes
letras donde va un número, el cajero te lo vuelve a pedir.

Cuentas de prueba:

| Cuenta | Titular | PIN |
|---|---|---|
| 1001 | Ana | 1234 |
| 1002 | Luis | 4321 |
| 1003 | Sofía | 0000 |

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a juntar varias cosas que ya conoces. La clase `Cuenta`
retoma la idea del proyecto 052: el saldo y el PIN son privados, y el PIN
nunca sale de la cuenta, solo se compara con `verificar_pin()`. El `Cajero`
guarda las cuentas en un diccionario donde la llave es el número de cuenta,
así encuentra cualquiera de inmediato. Transferir usa dos cuentas a la vez:
primero retira de una y, solo si se pudo, deposita en la otra.

Las entradas numéricas usan `try`/`except ValueError` del proyecto 047 para
que el programa no se detenga si escribes algo que no es un número.

Símbolos y sintaxis nuevos: no hay símbolos nuevos. Lo nuevo es combinar
clases con diccionarios, validaciones y `try`/`except` en un programa
interactivo.
