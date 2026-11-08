# 071 Patrón observador

Un programa con una estación meteorológica y varias pantallas: una muestra la
temperatura actual, otra lleva la mínima, la máxima y el promedio, otra avisa
si hace demasiado calor y una bitácora anota cada medición. Cada vez que la
estación mide, todas se enteran solas. A mitad del programa la bitácora se
desuscribe y deja de recibir avisos.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a conocer los patrones de diseño: soluciones probadas
para problemas que aparecen seguido al programar. El patrón observador sirve
cuando un objeto cambia y otros necesitan enterarse. La estación (el sujeto)
no sabe qué hace cada pantalla: solo guarda una lista de observadores y, al
medir, los llama a todos. Por eso puedes agregar o quitar pantallas sin tocar
el código de la estación.

En Python no hace falta que un observador sea un objeto. Las funciones
también son objetos, así que la estación acepta el método de una pantalla,
como `actual.actualizar`, o una función suelta, como `registrar_en_bitacora`.

Símbolos y sintaxis nuevos: los patrones de diseño, el patrón observador con
sus métodos para suscribir, desuscribir y notificar, y llamar a una función
guardada en una lista, como `observador(self.temperatura)`.
