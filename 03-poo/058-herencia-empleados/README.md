# 058 Empleados y sueldos

Un programa que arma la nómina del mes de una pequeña empresa. Hay empleados,
gerentes y practicantes, y cada tipo calcula su sueldo a su manera: el
empleado cobra su sueldo base, el gerente cobra su sueldo base más un bono, y
el practicante recibe el 60 % del sueldo base como apoyo.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a sobrescribir métodos: las clases hijas vuelven a
definir `calcular_sueldo()` con el mismo nombre, y Python usa la versión que
corresponde a cada objeto.

Fíjate en las dos formas de hacerlo. El gerente reutiliza el cálculo del
padre con `super().calcular_sueldo()` y solo le suma su bono. El practicante
no lo reutiliza, porque su sueldo se calcula de otra manera. Y aunque
`mostrar_recibo()` solo está escrito en `Empleado`, cada objeto muestra su
propio sueldo.

Símbolos y sintaxis nuevos: la sobrescritura de métodos, `super()` para
llamar a un método del padre, como `super().calcular_sueldo()`, y el formato
de alineación en f-strings, como `:<10` y `:>10.2f`.
