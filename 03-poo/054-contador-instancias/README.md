# 054 Contador de instancias

Un programa que registra a los jugadores de un torneo. Cada jugador recibe un
número de registro automático y la clase lleva la cuenta de cuántos jugadores
se han creado. Antes de registrar a alguien revisa que su nombre tenga al
menos dos letras.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a distinguir dos tipos de atributos. Los atributos de
instancia, como `self.nombre`, son propios de cada jugador. El atributo de
clase `total_creados` es uno solo para todos, y por eso sirve como contador.

También vas a conocer dos tipos de métodos nuevos. Un método de clase recibe
la clase en lugar de un objeto, así que puedes preguntar cuántos jugadores hay
aunque todavía no exista ninguno. Un método estático no recibe ni la clase ni
un objeto: es una función que vive dentro de la clase porque tiene que ver
con ella.

Símbolos y sintaxis nuevos: los atributos de clase, como
`total_creados = 0` dentro de la clase, los decoradores `@classmethod` y
`@staticmethod`, y el parámetro `cls`.
