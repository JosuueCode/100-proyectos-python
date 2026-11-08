"""Proyecto 077: Calculadora con interfaz.

Una calculadora con botones que suma, resta, multiplica y divide. Las
operaciones se resuelven con lógica propia, sin eval().
"""

import tkinter as tk

# Cada lista es una fila de botones, en el orden en que se ven
BOTONES = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
]
OPERADORES = "+-*/"
DIGITOS = "0123456789."


# Una forma corta de hacer una calculadora sería armar un texto como
# "8*3" y pasárselo a eval(), que ejecuta cualquier texto como código de
# Python. Es inseguro: si el texto viene del usuario, puede contener
# instrucciones para borrar archivos o leer datos, y eval() las ejecutaría
# sin preguntar. Por eso aquí cada operación se resuelve a mano.
def calcular(primero: float, operador: str, segundo: float) -> float:
    """Aplica el operador a los dos números."""
    if operador == "+":
        return primero + segundo
    if operador == "-":
        return primero - segundo
    if operador == "*":
        return primero * segundo
    # Dividir entre cero lanza ZeroDivisionError, que atrapa quien llama
    return primero / segundo


def formatear(numero: float) -> str:
    """Devuelve el número sin .0 si es entero y con pocos decimales si no."""
    # is_integer() devuelve True si el float no tiene parte decimal
    if numero.is_integer():
        return str(int(numero))
    return str(round(numero, 8))


class App:
    """Calculadora con pantalla y botones en una cuadrícula."""

    def __init__(self, ventana: tk.Tk):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.resizable(False, False)

        self.primero = 0.0
        self.operador = ""
        # True cuando el siguiente dígito debe empezar un número nuevo
        self.empezar_nuevo = True

        # anchor="e" alinea el texto a la derecha (east, este), como en
        # cualquier calculadora
        self.pantalla = tk.Label(
            ventana, text="0", anchor="e", font=("Arial", 24),
            bg="white", relief="sunken", padx=10,
        )
        # grid() acomoda los widgets en una cuadrícula de filas y columnas.
        # columnspan=4 hace que la pantalla ocupe las cuatro columnas y
        # sticky="we" la estira de izquierda (west) a derecha (east).
        self.pantalla.grid(
            row=0, column=0, columnspan=4, sticky="we", padx=5, pady=5,
        )

        self.crear_botones()

    def crear_botones(self):
        """Crea todos los botones con un ciclo en lugar de uno por uno."""
        for numero_fila, fila in enumerate(BOTONES):
            for numero_columna, texto in enumerate(fila):
                # La lambda llama a presionar() con el texto del botón. El
                # parámetro texto=texto es un valor por defecto: se guarda
                # al crear la lambda. Sin él, todas las lambdas usarían el
                # último valor de la variable texto al terminar el ciclo, y
                # todos los botones escribirían "+".
                boton = tk.Button(
                    self.ventana, text=texto, width=5, height=2,
                    font=("Arial", 14),
                    command=lambda texto=texto: self.presionar(texto),
                )
                # La fila 0 es la pantalla, por eso los botones empiezan en 1
                boton.grid(
                    row=numero_fila + 1, column=numero_columna, padx=2, pady=2,
                )

        igual = tk.Button(
            self.ventana, text="=", height=2, font=("Arial", 14),
            command=self.resolver,
        )
        igual.grid(row=5, column=0, columnspan=4, sticky="we", padx=2, pady=2)

    def texto_pantalla(self) -> str:
        """Devuelve lo que se ve en la pantalla."""
        return self.pantalla.cget("text")

    def mostrar(self, texto: str):
        """Cambia lo que se ve en la pantalla."""
        self.pantalla.config(text=texto)

    def presionar(self, texto: str):
        """Decide qué hacer según el botón pulsado."""
        if texto in DIGITOS:
            self.escribir_digito(texto)
        elif texto in OPERADORES:
            self.elegir_operador(texto)
        elif texto == "C":
            self.limpiar()

    def escribir_digito(self, digito: str):
        """Agrega un dígito o el punto decimal al número en pantalla."""
        if self.empezar_nuevo:
            actual = "0"
            self.empezar_nuevo = False
        else:
            actual = self.texto_pantalla()

        if digito == "." and "." in actual:
            return
        if actual == "0" and digito != ".":
            actual = ""
        self.mostrar(actual + digito)

    def elegir_operador(self, operador: str):
        """Guarda el primer número y el operador elegido."""
        # Si ya había una operación pendiente, se resuelve primero, así
        # 2 + 3 * se convierte en 5 *
        if self.operador != "" and not self.empezar_nuevo:
            self.resolver()
        # Después de un error no hay número con qué seguir operando
        if self.texto_pantalla() == "Error":
            return
        self.primero = float(self.texto_pantalla())
        self.operador = operador
        self.empezar_nuevo = True

    def resolver(self):
        """Calcula el resultado de la operación pendiente."""
        if self.operador == "" or self.texto_pantalla() == "Error":
            return
        segundo = float(self.texto_pantalla())
        try:
            resultado = calcular(self.primero, self.operador, segundo)
            self.mostrar(formatear(resultado))
        except ZeroDivisionError:
            self.mostrar("Error")
        self.operador = ""
        self.empezar_nuevo = True

    def limpiar(self):
        """Borra la pantalla y la operación pendiente."""
        self.primero = 0.0
        self.operador = ""
        self.empezar_nuevo = True
        self.mostrar("0")


def main():
    """Abre la calculadora."""
    ventana = tk.Tk()
    App(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
