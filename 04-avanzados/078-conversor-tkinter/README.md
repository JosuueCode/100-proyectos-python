# 078 Conversor con interfaz

Una ventana para convertir unidades de temperatura (Celsius, Fahrenheit y
Kelvin), longitud (metros, kilómetros, centímetros, millas, pies y pulgadas)
y peso (kilogramos, gramos, libras y onzas). Eliges la categoría, escribes
el valor, eliges las unidades y pulsas "Convertir". Si escribes algo que no
es un número, una longitud negativa o una temperatura bajo el cero absoluto,
aparece un cuadro de mensaje que te explica el error.

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

En este proyecto vas a usar `ttk`, la versión de los widgets de tkinter con
el estilo de tu sistema operativo, y su `Combobox`, una lista desplegable
para elegir una opción. Los widgets se conectan con variables `StringVar`:
cuando el usuario escribe o elige algo, la variable cambia, y cuando tú
cambias la variable con `set()`, el widget se actualiza solo. Con
`trace_add()` las listas de unidades cambian en cuanto eliges otra
categoría.

Las entradas se validan con `try`/`except`. Si `float()` no puede convertir
el texto o la conversión lanza un `ValueError`, el error se muestra con
`messagebox.showerror()`, un cuadro que espera a que pulses Aceptar.

Símbolos y sintaxis nuevos: el módulo `ttk` con `Frame`, `Combobox`, `Label`,
`Entry` y `Button`, `StringVar` con `get()`, `set()` y `trace_add()`, la
opción `textvariable`, `messagebox.showerror()` y `list()` aplicado a un
diccionario para obtener sus llaves.
