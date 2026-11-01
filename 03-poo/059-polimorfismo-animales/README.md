# 059 Animales y sonidos

Un programa con una granja donde viven un perro, un gato, una vaca, un pato y
un robot de juguete. Un solo ciclo recorre a todos y cada uno se presenta con
su propio sonido.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a ver el polimorfismo: objetos de clases distintas que
responden al mismo método, cada uno a su manera. El `for` no pregunta qué
animal es cada uno ni necesita un `if` por tipo; solo llama a
`presentarse()`. Si mañana agregas una clase `Oveja` con su `hacer_sonido()`,
el ciclo funciona sin cambiar una sola línea.

El robot no hereda de `Animal` y aun así funciona en el mismo ciclo. Eso es
el duck typing de Python: lo que importa es que el objeto tenga el método que
se le pide, no de qué clase viene.

No hay símbolos nuevos: el polimorfismo usa la sobrescritura de métodos que
viste en el proyecto 058.
