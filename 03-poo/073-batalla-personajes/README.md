# 073 Batalla de personajes

Un pequeño torneo por turnos entre una guerrera, un mago y un arquero. En el
primer combate se enfrentan la guerrera y el mago; el ganador descansa y
pelea la final contra el arquero. Cada turno el personaje ataca con un daño
al azar, y cada tres turnos usa su habilidad especial: la guerrera da un
golpe doble, el mago se cura y el arquero lanza tres flechas. Como el daño es
aleatorio, cada vez que lo ejecutes puede ganar alguien distinto.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a juntar varias ideas de la etapa. `Personaje` es una
clase abstracta, como `Figura` en el proyecto 060: define cómo se ataca y
cómo se toma un turno, pero obliga a cada personaje a escribir su propia
`habilidad_especial()`. El combate llama a `tomar_turno()` sin saber qué
personaje es, y cada uno responde a su manera gracias al polimorfismo.

La vida está protegida con `@property`, ahora con un setter. Cada vez que
asignas `personaje.vida = valor`, el valor pasa por el setter, que lo recorta
para que nunca baje de cero ni pase de la vida máxima. Así, ni un golpe
enorme deja la vida negativa ni la curación del mago la sube de más.

Símbolos y sintaxis nuevos: el decorador `@vida.setter` para controlar lo
que se asigna a una propiedad.
