# 076 Primera ventana con tkinter

Tu primer programa con ventana. Se abre una ventana pequeña con una caja de
texto y un botón: escribes tu nombre, pulsas "Saludar" y la ventana te
saluda. Si pulsas el botón sin escribir nada, te pide tu nombre.

Con este proyecto empieza la etapa de programas visuales e interactivos.

## Cómo ejecutarlo

tkinter ya viene con Python, así que no necesitas instalar nada. En algunas
distribuciones de Linux viene aparte; si al ejecutar ves un error que menciona
`tkinter`, instálalo con `sudo apt install python3-tk` o el comando de tu
distribución.

Desde esta carpeta:

```bash
python main.py
```

En Windows también puedes usar `py main.py`, y en macOS o Linux `python3 main.py`.

## Qué vas a practicar

En este proyecto vas a crear una ventana con `Tk()` y a llenarla de widgets,
los elementos de una interfaz: `Label` para mostrar texto, `Entry` para que
el usuario escriba y `Button` para un botón. Cada widget se coloca con
`pack()`, que los acomoda uno debajo de otro. Toda la interfaz vive en la
clase `App`, así los widgets son atributos y los métodos pueden usarlos.

Hasta ahora tus programas se ejecutaban de arriba abajo y terminaban. Una
interfaz gráfica funciona distinto: está orientada a eventos. El programa
prepara la ventana y luego espera a que pase algo, como un clic, y entonces
llama a la función que le indicaste, como `saludar()` en el `command` del
botón. Esa espera es `mainloop()`: un ciclo que atiende los eventos y
redibuja la ventana, y por eso la mantiene abierta hasta que la cierras.

Símbolos y sintaxis nuevos: `import ... as`, el módulo `tkinter` con `Tk`,
`Label`, `Entry`, `Button`, `pack()` y `mainloop()`, los métodos `get()` y
`config()` de los widgets, el parámetro `command` y las tuplas, como
`("Arial", 14)`.
