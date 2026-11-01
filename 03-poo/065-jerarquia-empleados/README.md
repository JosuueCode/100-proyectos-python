# 065 Jerarquía de empleados

Un programa que arma la nómina de una empresa con empleados, desarrolladores,
desarrolladores senior y gerentes. Los gerentes y los desarrolladores senior
reciben un bono sobre su sueldo base. Antes de la nómina, el programa te
muestra en qué orden busca Python los métodos de las clases con bono.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a usar herencia múltiple: una clase que hereda de dos
clases a la vez, como `class Gerente(BonoMixin, Empleado)`. `BonoMixin` es un
mixin, una clase pequeña que no representa a nadie por sí sola y solo aporta
una habilidad, en este caso sumar un bono. Gracias a eso, el bono se escribe
una sola vez y se lo das tanto al gerente como al desarrollador senior, que
están en ramas distintas de la jerarquía.

Cuando una clase tiene varios padres, Python necesita saber en cuál buscar
primero cada método. Ese orden es el MRO (orden de resolución de métodos) y
lo puedes ver con `Clase.mro()`. Por eso el `super()` del mixin no apunta a
un padre fijo, sino a la siguiente clase del MRO del objeto.

La herencia múltiple conviene para agregar habilidades pequeñas e
independientes, como el bono, a clases que no están emparentadas. Hay que
usarla con cuidado: si dos padres tienen métodos con el mismo nombre, el
resultado depende del orden en que los escribas, y con muchas clases
mezcladas cuesta saber de dónde sale cada método. Si dudas, la composición
del proyecto 061 suele ser una opción más sencilla.

Símbolos y sintaxis nuevos: la herencia múltiple con varias clases entre
paréntesis, separadas por comas, los mixins y el método `mro()` para ver el
orden de resolución de métodos.
