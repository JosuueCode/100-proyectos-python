# 080 Reloj digital

Un reloj digital en una ventana negra con números verdes. Muestra la hora con
segundos y, debajo, la fecha en español, por ejemplo "lunes 3 de marzo de
2025". Se actualiza cada segundo, y con el botón cambias entre el formato de
24 horas y el de 12 horas con a. m. y p. m.

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

En este proyecto vas a repetir una tarea cada cierto tiempo sin congelar la
ventana. `after(1000, self.actualizar)` le pide a tkinter que llame a
`actualizar()` dentro de 1000 milisegundos, y `actualizar()` se vuelve a
programar cada vez, así el reloj avanza solo.

Podrías pensar en un ciclo con `time.sleep(1)`, pero en una interfaz gráfica
eso detiene todo el programa, incluido el `mainloop()` que atiende los
eventos. Mientras duerme, la ventana no responde a clics ni se redibuja: se
congela. Con `after()` el `mainloop()` queda libre entre una actualización y
otra.

La hora sale de `datetime.now()` y se le da formato con `strftime()`, como en
el proyecto 075. Para la fecha se usan listas propias con los nombres de los
días y meses, porque `strftime()` los escribe en el idioma del sistema.

Símbolos y sintaxis nuevos: el método `after()` de tkinter, `weekday()` y
los atributos `hour`, `day`, `month` y `year` de un `datetime`, los códigos
`%H`, `%I` y `%S` de `strftime()` y los colores en hexadecimal, como
`"#00e676"`.
