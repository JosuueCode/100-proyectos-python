# 068 Clase Fecha

Un programa con una clase `Fecha` que solo acepta fechas que existen. Revisa
el mes, el día y los años bisiestos, así que acepta el 29 de febrero de 2024
pero no el de 2023 ni el de 1900. Si la fecha no existe, lanza un
`ValueError` que te dice por qué. Después compara fechas con `<`, `>`, `==`
y `<=`, y ordena una lista de fechas históricas.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a retomar la regla del año bisiesto del proyecto 016,
ahora dentro de un método estático de la clase, y a validar en `__init__`
lanzando un `ValueError`, como aprendiste en el proyecto 066.

Para comparar fechas, la clase escribe solo dos métodos: `__eq__` para `==`
y `__lt__` para `<`. El decorador `@total_ordering` del módulo `functools`
genera los otros tres, `<=`, `>` y `>=`, a partir de esos dos. Y como
`sorted()` y `max()` usan esas comparaciones, también funcionan con fechas
sin necesidad de `key`.

Símbolos y sintaxis nuevos: el módulo `functools`, el decorador de clase
`@total_ordering` y el método `__lt__` para el operador `<`.
