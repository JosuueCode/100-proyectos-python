"""Proyecto 076: Primera ventana con tkinter.

Una ventana que pide tu nombre y te saluda al pulsar un botón.
"""

# tkinter es la biblioteca de la biblioteca estándar para crear ventanas.
# import ... as le da un nombre corto al módulo: se escribe tk.Label en
# lugar de tkinter.Label.
import tkinter as tk


# La interfaz se organiza en una clase. Cada elemento de la ventana, como
# una etiqueta o un botón, se llama widget y se guarda como atributo para
# poder usarlo desde los métodos.
class App:
    """Ventana que pide un nombre y muestra un saludo."""

    def __init__(self, ventana: tk.Tk):
        self.ventana = ventana
        self.ventana.title("Primera ventana")
        # geometry() fija el tamaño inicial: ancho x alto en píxeles
        self.ventana.geometry("320x200")

        # Label muestra un texto. El primer argumento es el contenedor
        # donde va el widget, en este caso la ventana.
        self.instruccion = tk.Label(ventana, text="¿Cómo te llamas?")
        # pack() coloca el widget en la ventana, uno debajo de otro. pady
        # deja un espacio vertical en píxeles arriba y abajo.
        self.instruccion.pack(pady=10)

        # Entry es una caja de texto de una línea donde el usuario escribe
        self.entrada = tk.Entry(ventana, width=25)
        self.entrada.pack()

        # Button es un botón. command recibe la función que se llama al
        # pulsarlo; va sin paréntesis porque tkinter la llamará después.
        self.boton = tk.Button(ventana, text="Saludar", command=self.saludar)
        self.boton.pack(pady=10)

        # font recibe una tupla con el nombre de la letra y su tamaño. Una
        # tupla se escribe entre paréntesis y es como una lista que no se
        # puede modificar después de crearla.
        self.saludo = tk.Label(ventana, text="", font=("Arial", 14))
        self.saludo.pack()

    def saludar(self):
        """Lee el nombre escrito y muestra el saludo."""
        # get() devuelve el texto que hay en la caja
        nombre = self.entrada.get().strip()
        # config() cambia una opción de un widget que ya existe
        if nombre == "":
            self.saludo.config(text="Escribe tu nombre primero.")
        else:
            self.saludo.config(text=f"Hola, {nombre}. Qué gusto verte.")


def main():
    """Crea la ventana y espera a que el usuario la use."""
    # Tk() crea la ventana principal del programa
    ventana = tk.Tk()
    App(ventana)
    # Un programa con interfaz gráfica está orientado a eventos: en lugar
    # de ejecutarse de arriba abajo y terminar, espera a que pase algo,
    # como un clic o una tecla, y responde llamando a la función indicada.
    # mainloop() es el ciclo que espera esos eventos y redibuja la ventana.
    # Mientras está activo la ventana sigue abierta; al cerrarla, termina
    # y el programa continúa después de esta línea.
    ventana.mainloop()


if __name__ == "__main__":
    main()
