# 052 Cuenta bancaria

Un programa con una cuenta bancaria que cuida su propio saldo. Puedes depositar
y retirar, y cada operación revisa que la cantidad sea mayor que cero y que
alcance el dinero. Al final intenta cambiar el saldo a mano para mostrarte que
la cuenta no lo permite.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a aplicar el encapsulamiento: el saldo es un atributo
privado y solo cambia a través de `depositar()` y `retirar()`, que revisan
cada operación. Si cualquier parte del programa pudiera escribir
`cuenta.saldo = 1000000`, nada impediría inventar dinero o dejar la cuenta en
negativo.

Para que el saldo se pueda consultar sin poder modificarlo usas `@property`,
tu primer decorador. Compáralo con el cajero del proyecto 025: allá el saldo
era una variable que cualquier línea del programa podía cambiar.

Símbolos y sintaxis nuevos: los atributos privados con dos guiones bajos,
como `self.__saldo`, los decoradores con `@` y el decorador `@property`, y el
error `AttributeError`.
