# 089 Editor de dibujo

Un pequeño programa de dibujo. Arrastras el mouse sobre el lienzo para
pintar a mano alzada, eliges el color en la paleta y el grosor del pincel
con un control deslizante. También tienes un borrador, un botón para
limpiar todo y la opción de deshacer el último trazo con Ctrl+Z.

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

## Controles

| Acción | Control |
|---|---|
| Dibujar | Arrastrar con el botón izquierdo |
| Elegir color | Clic en un cuadro de la paleta |
| Cambiar grosor | Control deslizante "Grosor" |
| Borrador | Botón "Borrador" (otra vez para apagarlo) |
| Deshacer el último trazo | Ctrl+Z o botón "Deshacer" |
| Borrar todo | Botón "Limpiar todo" |

## Qué vas a practicar

En este proyecto vas a dibujar en un `Canvas`, el lienzo de tkinter. Cada
línea que creas con `create_line()` queda como un objeto con su propio
número, y con ese número la puedes borrar después.

Los trazos salen de tres eventos del mouse. Al presionar el botón
(`<Button-1>`) se guarda el punto de inicio; mientras lo mueves con el
botón presionado (`<B1-Motion>`) se dibuja una línea corta del punto
anterior al actual; y al soltarlo (`<ButtonRelease-1>`) todas esas líneas se
guardan juntas como un trazo. Deshacer es sacar el último trazo de la lista
y borrar sus líneas. El borrador no borra nada: es un pincel del color del
fondo.

Símbolos y sintaxis nuevos: `Canvas` con `create_line()` y `delete()`, los
eventos `<Button-1>`, `<B1-Motion>` y `<ButtonRelease-1>` con `evento.x` y
`evento.y`, el atajo `<Control-z>` y el control deslizante `Scale` con su
opción `from_`.
