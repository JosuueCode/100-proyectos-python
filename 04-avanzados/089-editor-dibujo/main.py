"""Proyecto 089: Editor de dibujo.

Un lienzo para dibujar a mano alzada con el mouse. Tiene paleta de
colores, grosor de pincel, borrador, limpiar todo y deshacer con Ctrl+Z.
"""

import tkinter as tk

ANCHO_LIENZO = 800
ALTO_LIENZO = 520
COLOR_FONDO = "white"
GROSOR_INICIAL = 6
GROSOR_MINIMO = 1
GROSOR_MAXIMO = 40
PALETA = [
    "black", "#e53935", "#fb8c00", "#fdd835", "#43a047",
    "#1e88e5", "#8e24aa", "#6d4c41", "#ec407a", "#90a4ae",
]


class App:
    """Ventana con la barra de herramientas y el lienzo."""

    def __init__(self, ventana: tk.Tk):
        self.ventana = ventana
        self.ventana.title("Editor de dibujo")
        self.color = PALETA[0]
        self.borrador = False
        # Cada trazo es la lista de líneas que se dibujaron desde que se
        # presionó el botón hasta que se soltó. trazos guarda todos, en
        # orden, para poder deshacer el último.
        self.trazos = []
        self.trazo_actual = []
        self.ultimo_x = 0
        self.ultimo_y = 0

        self.crear_barra()
        # Canvas es un lienzo donde se dibujan líneas, figuras y texto.
        # Cada figura queda como un objeto con un número propio, así se
        # puede borrar después.
        self.lienzo = tk.Canvas(ventana, width=ANCHO_LIENZO,
                                height=ALTO_LIENZO, bg=COLOR_FONDO,
                                cursor="crosshair")
        self.lienzo.pack(padx=8, pady=(0, 8))

        # Eventos del mouse sobre el lienzo: <Button-1> al presionar el
        # botón izquierdo, <B1-Motion> al moverlo con el botón presionado y
        # <ButtonRelease-1> al soltarlo. tkinter le pasa a la función un
        # objeto evento con la posición en evento.x y evento.y.
        self.lienzo.bind("<Button-1>", self.empezar_trazo)
        self.lienzo.bind("<B1-Motion>", self.dibujar)
        self.lienzo.bind("<ButtonRelease-1>", self.terminar_trazo)
        # Control-z es la combinación Ctrl+Z; la segunda versión cubre el
        # caso de tener activadas las mayúsculas
        self.ventana.bind("<Control-z>", lambda evento: self.deshacer())
        self.ventana.bind("<Control-Z>", lambda evento: self.deshacer())

    def crear_barra(self):
        """Crea los botones de color, el grosor y las herramientas."""
        barra = tk.Frame(self.ventana)
        barra.pack(fill="x", padx=8, pady=8)

        for color in PALETA:
            boton = tk.Button(barra, bg=color, activebackground=color,
                              width=2, relief="raised",
                              command=lambda color=color: self.elegir(color))
            boton.pack(side="left", padx=1)

        # El cuadro muestra el color actual, o el fondo si es el borrador
        self.muestra = tk.Label(barra, text="  ", bg=self.color, width=3,
                                relief="sunken")
        self.muestra.pack(side="left", padx=8)

        # Scale es un control deslizante para elegir un número entre from_
        # y to. Se escribe from_ con guion bajo porque from es una palabra
        # reservada de Python. orient="horizontal" lo pone acostado.
        self.grosor = tk.Scale(barra, from_=GROSOR_MINIMO, to=GROSOR_MAXIMO,
                               orient="horizontal", label="Grosor",
                               length=140)
        # set() le da su valor inicial y get() lo lee al dibujar
        self.grosor.set(GROSOR_INICIAL)
        self.grosor.pack(side="left", padx=8)

        self.boton_borrador = tk.Button(barra, text="Borrador",
                                        command=self.alternar_borrador)
        self.boton_borrador.pack(side="left", padx=2)
        tk.Button(barra, text="Deshacer", command=self.deshacer).pack(
            side="left", padx=2)
        tk.Button(barra, text="Limpiar todo", command=self.limpiar).pack(
            side="left", padx=2)

    def color_del_pincel(self) -> str:
        """Devuelve el color con el que se pinta ahora."""
        # El borrador es un pincel del color del fondo
        if self.borrador:
            return COLOR_FONDO
        return self.color

    def elegir(self, color: str):
        """Cambia el color del pincel y apaga el borrador."""
        self.color = color
        self.borrador = False
        self.actualizar_herramienta()

    def alternar_borrador(self):
        """Enciende o apaga el borrador."""
        self.borrador = not self.borrador
        self.actualizar_herramienta()

    def actualizar_herramienta(self):
        """Muestra el color actual y si el borrador está activo."""
        self.muestra.config(bg=self.color_del_pincel())
        if self.borrador:
            self.boton_borrador.config(relief="sunken")
        else:
            self.boton_borrador.config(relief="raised")

    def empezar_trazo(self, evento: tk.Event):
        """Guarda el punto donde se presionó el botón."""
        self.ultimo_x = evento.x
        self.ultimo_y = evento.y
        self.trazo_actual = []
        # Un clic sin mover también deja un punto
        self.dibujar(evento)

    def dibujar(self, evento: tk.Event):
        """Une el punto anterior con el actual con una línea."""
        # create_line() dibuja una línea entre dos puntos y devuelve su
        # número de objeto. capstyle="round" redondea las puntas para que
        # los segmentos se unan sin huecos.
        linea = self.lienzo.create_line(
            self.ultimo_x, self.ultimo_y, evento.x, evento.y,
            fill=self.color_del_pincel(), width=self.grosor.get(),
            capstyle="round", joinstyle="round",
        )
        self.trazo_actual.append(linea)
        self.ultimo_x = evento.x
        self.ultimo_y = evento.y

    def terminar_trazo(self, evento: tk.Event):
        """Guarda el trazo completo para poder deshacerlo."""
        if len(self.trazo_actual) > 0:
            self.trazos.append(self.trazo_actual)
        self.trazo_actual = []

    def deshacer(self):
        """Borra las líneas del último trazo."""
        if len(self.trazos) == 0:
            return
        for linea in self.trazos.pop():
            # delete() quita del lienzo el objeto con ese número
            self.lienzo.delete(linea)

    def limpiar(self):
        """Borra todo el lienzo y el historial de trazos."""
        # "all" es una etiqueta especial que incluye todos los objetos
        self.lienzo.delete("all")
        self.trazos = []


def main():
    """Abre el editor de dibujo."""
    ventana = tk.Tk()
    App(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
