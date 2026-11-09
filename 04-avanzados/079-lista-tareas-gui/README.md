# 079 Lista de tareas con interfaz

Una ventana para llevar tus pendientes. Escribes una tarea y la agregas con
el botón o con la tecla Enter. Para marcarla como hecha, la eliges y pulsas
"Marcar como hecha" o le das doble clic; las tareas hechas se ven en gris.
También puedes eliminarlas. Al cerrar la ventana, tus tareas se guardan en
`tareas.txt`, y la próxima vez que abras el programa siguen ahí.

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

El archivo `tareas.txt` se crea en la carpeta desde donde ejecutas el
programa.

## Qué vas a practicar

En este proyecto vas a mostrar una lista con `Listbox` y a conectarla con
una `Scrollbar` para desplazarte cuando hay muchas tareas. Con `bind()`
conectas un evento con una función: la tecla Enter en la caja de texto y el
doble clic en la lista. Es otra forma de responder a eventos, además del
`command` de los botones.

Para guardar al cerrar, `protocol("WM_DELETE_WINDOW", ...)` cambia lo que
pasa al pulsar la X de la ventana. Los archivos se leen y escriben con
`open()` y `with`, como en el proyecto 048.

Símbolos y sintaxis nuevos: `Listbox` con `insert()`, `delete()`,
`curselection()` e `itemconfig()`, `Scrollbar` con `yscrollcommand` y
`yview`, `bind()` con los eventos `"<Return>"` y `"<Double-Button-1>"`,
`Frame` y `pack()` con `side`, `fill` y `expand`, la constante `tk.END` y
`protocol()` para el cierre de la ventana.
