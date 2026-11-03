# 070 Sistema de tickets

Un programa que simula el soporte técnico de una oficina. Se registran
tickets con problemas, se asignan a dos agentes y cada ticket avanza por sus
estados: abierto, en proceso, resuelto y cerrado. No se vale cualquier
cambio: un ticket abierto no puede pasar directo a resuelto, y uno cerrado ya
no cambia. Al final ves los tickets agrupados por estado.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a usar una enumeración con el módulo `enum`. `Estado`
hereda de `Enum` y tiene cuatro valores fijos con nombre. Si guardaras el
estado como un texto, un error como escribir `"resulto"` pasaría sin aviso;
con `Estado.RESUELTO` Python te avisa al momento si te equivocas. Cada valor
tiene un `.name` y un `.value`, y con un `for` puedes recorrerlos todos.

Las transiciones permitidas están en un diccionario. Si pides una que no
está, el ticket lanza `TransicionInvalidaError`, una excepción propia como
las del proyecto 066. Todas heredan de `ErrorTickets`, así que un solo
`except` atiende cualquier error del sistema.

Símbolos y sintaxis nuevos: el módulo `enum`, las clases que heredan de
`Enum`, los atributos `.name` y `.value`, recorrer una enumeración con `for`
y pasar un método como argumento, como `intentar(sistema.asignar, 1, marta)`.
