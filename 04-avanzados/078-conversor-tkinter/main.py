"""Proyecto 078: Conversor con interfaz.

Una ventana que convierte temperatura, longitud y peso entre varias
unidades. Los errores se muestran en un cuadro de mensaje.
"""

import tkinter as tk

# ttk (themed tk) tiene versiones de los widgets con el estilo del sistema
# operativo, y algunos que tk no tiene, como Combobox. messagebox abre
# cuadros de diálogo con un mensaje y un botón para cerrarlos.
from tkinter import messagebox, ttk

# Cuántas unidades base vale cada unidad: metros para longitud y
# kilogramos para peso. Para convertir se pasa a la base y luego a la otra.
FACTORES = {
    "Longitud": {
        "metros": 1,
        "kilómetros": 1000,
        "centímetros": 0.01,
        "millas": 1609.344,
        "pies": 0.3048,
        "pulgadas": 0.0254,
    },
    "Peso": {
        "kilogramos": 1,
        "gramos": 0.001,
        "libras": 0.45359237,
        "onzas": 0.028349523125,
    },
}
TEMPERATURAS = ["Celsius", "Fahrenheit", "Kelvin"]
CATEGORIAS = ["Temperatura", "Longitud", "Peso"]
CERO_ABSOLUTO = -273.15


def a_celsius(valor: float, unidad: str) -> float:
    """Pasa una temperatura a grados Celsius."""
    if unidad == "Fahrenheit":
        return (valor - 32) * 5 / 9
    if unidad == "Kelvin":
        return valor + CERO_ABSOLUTO
    return valor


def desde_celsius(valor: float, unidad: str) -> float:
    """Pasa grados Celsius a la unidad indicada."""
    if unidad == "Fahrenheit":
        return valor * 9 / 5 + 32
    if unidad == "Kelvin":
        return valor - CERO_ABSOLUTO
    return valor


def unidades_de(categoria: str) -> list[str]:
    """Devuelve los nombres de las unidades de una categoría."""
    if categoria == "Temperatura":
        return TEMPERATURAS
    # list() de un diccionario devuelve una lista con sus llaves
    return list(FACTORES[categoria])


def formatear(numero: float) -> str:
    """Devuelve el número sin .0 si es entero y con hasta 4 decimales."""
    numero = round(numero, 4)
    if numero.is_integer():
        return str(int(numero))
    return str(numero)


def convertir(
    valor: float, categoria: str, origen: str, destino: str,
) -> float:
    """Convierte el valor. Lanza ValueError si no tiene sentido físico."""
    if categoria == "Temperatura":
        celsius = a_celsius(valor, origen)
        if celsius < CERO_ABSOLUTO:
            raise ValueError("Ninguna temperatura baja del cero absoluto.")
        return desde_celsius(celsius, destino)

    if valor < 0:
        raise ValueError(f"La {categoria.lower()} no puede ser negativa.")
    factores = FACTORES[categoria]
    return valor * factores[origen] / factores[destino]


class App:
    """Conversor con categoría, unidades, valor y resultado."""

    def __init__(self, ventana: tk.Tk):
        self.ventana = ventana
        self.ventana.title("Conversor de unidades")
        self.ventana.resizable(False, False)

        # StringVar es una variable de tkinter que guarda un texto y está
        # conectada a los widgets: si cambia, el widget se actualiza solo,
        # y si el usuario escribe o elige algo, la variable cambia.
        self.categoria = tk.StringVar(value=CATEGORIAS[0])
        self.origen = tk.StringVar()
        self.destino = tk.StringVar()
        self.valor = tk.StringVar()
        self.resultado = tk.StringVar(value="Escribe un valor y convierte.")

        # Frame es un contenedor para agrupar widgets; padding deja margen
        marco = ttk.Frame(ventana, padding=15)
        marco.grid()

        ttk.Label(marco, text="Categoría").grid(row=0, column=0, sticky="w")
        # Combobox es una lista desplegable. state="readonly" impide que
        # el usuario escriba: solo puede elegir una de las opciones.
        # textvariable conecta el widget con la StringVar.
        categorias = ttk.Combobox(
            marco, textvariable=self.categoria, values=CATEGORIAS,
            state="readonly", width=18,
        )
        categorias.grid(row=0, column=1, pady=4)

        ttk.Label(marco, text="Valor").grid(row=1, column=0, sticky="w")
        entrada = ttk.Entry(marco, textvariable=self.valor, width=21)
        entrada.grid(row=1, column=1, pady=4)

        ttk.Label(marco, text="De").grid(row=2, column=0, sticky="w")
        self.lista_origen = ttk.Combobox(
            marco, textvariable=self.origen, state="readonly", width=18,
        )
        self.lista_origen.grid(row=2, column=1, pady=4)

        ttk.Label(marco, text="A").grid(row=3, column=0, sticky="w")
        self.lista_destino = ttk.Combobox(
            marco, textvariable=self.destino, state="readonly", width=18,
        )
        self.lista_destino.grid(row=3, column=1, pady=4)

        boton = ttk.Button(marco, text="Convertir", command=self.convertir)
        boton.grid(row=4, column=0, columnspan=2, pady=10)

        salida = ttk.Label(marco, textvariable=self.resultado)
        salida.grid(row=5, column=0, columnspan=2)

        # trace_add("write", ...) llama a la función cada vez que la
        # variable cambia. tkinter le pasa tres datos sobre la variable
        # que aquí no hacen falta, por eso la lambda los recibe y no los usa.
        self.categoria.trace_add(
            "write", lambda nombre, indice, modo: self.cambiar_unidades(),
        )
        self.cambiar_unidades()

    def cambiar_unidades(self):
        """Llena las listas de unidades según la categoría elegida."""
        unidades = unidades_de(self.categoria.get())
        self.lista_origen.config(values=unidades)
        self.lista_destino.config(values=unidades)
        # set() cambia el valor de la StringVar y el Combobox lo muestra
        self.origen.set(unidades[0])
        self.destino.set(unidades[1])
        self.resultado.set("Escribe un valor y convierte.")

    def convertir(self):
        """Lee el valor, lo convierte y muestra el resultado o el error."""
        texto = self.valor.get().strip().replace(",", ".")
        # float() lanza ValueError con un mensaje en inglés, así que para
        # ese caso se muestra uno propio
        try:
            valor = float(texto)
        except ValueError:
            # showerror() abre un cuadro con ícono de error y espera a que
            # el usuario pulse Aceptar
            mensaje = "Escribe un número, por ejemplo 25 o 3.5."
            messagebox.showerror("Valor no válido", mensaje)
            return

        categoria = self.categoria.get()
        origen = self.origen.get()
        destino = self.destino.get()
        try:
            resultado = convertir(valor, categoria, origen, destino)
        except ValueError as error:
            messagebox.showerror("Conversión imposible", str(error))
            return

        inicio = f"{formatear(valor)} {origen}"
        self.resultado.set(f"{inicio} = {formatear(resultado)} {destino}")


def main():
    """Abre el conversor."""
    ventana = tk.Tk()
    App(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
