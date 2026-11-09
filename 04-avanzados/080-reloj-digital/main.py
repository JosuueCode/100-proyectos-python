"""Proyecto 080: Reloj digital.

Una ventana que muestra la hora y la fecha y se actualiza cada segundo. Un
botón cambia entre el formato de 24 y de 12 horas.
"""

import tkinter as tk
from datetime import datetime

MILISEGUNDOS_POR_SEGUNDO = 1000
DIAS = [
    "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo",
]
MESES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
    "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]


def texto_fecha(momento: datetime) -> str:
    """Devuelve la fecha en español, por ejemplo lunes 3 de marzo de 2025."""
    # weekday() devuelve el día de la semana como número: 0 es lunes y 6
    # es domingo. Se usan listas propias porque strftime() escribe los
    # nombres en el idioma del sistema, que puede ser inglés.
    dia_semana = DIAS[momento.weekday()]
    mes = MESES[momento.month - 1]
    return f"{dia_semana} {momento.day} de {mes} de {momento.year}"


def texto_hora(momento: datetime, formato_24: bool) -> str:
    """Devuelve la hora en formato de 24 o de 12 horas."""
    # strftime() da formato a la hora: %H es la hora de 00 a 23, %I de 01
    # a 12, %M los minutos y %S los segundos
    if formato_24:
        return momento.strftime("%H:%M:%S")
    if momento.hour < 12:
        sufijo = "a. m."
    else:
        sufijo = "p. m."
    return f"{momento.strftime('%I:%M:%S')} {sufijo}"


class App:
    """Ventana del reloj."""

    def __init__(self, ventana: tk.Tk):
        self.ventana = ventana
        self.ventana.title("Reloj digital")
        self.ventana.configure(bg="black")
        self.ventana.resizable(False, False)
        self.formato_24 = True

        # Los colores se pueden dar por nombre, como "black", o en
        # hexadecimal: #00e676 indica cuánto rojo, verde y azul lleva
        self.hora = tk.Label(
            ventana, font=("Consolas", 48, "bold"), fg="#00e676", bg="black",
        )
        # Con una tupla, pady da un margen distinto arriba y abajo
        self.hora.pack(padx=30, pady=(25, 5))
        self.fecha = tk.Label(
            ventana, font=("Arial", 16), fg="white", bg="black",
        )
        self.fecha.pack(padx=30)

        self.boton = tk.Button(
            ventana, text="Cambiar a 12 horas", command=self.cambiar_formato,
        )
        self.boton.pack(pady=20)

        self.actualizar()

    def actualizar(self):
        """Muestra la hora actual y programa la siguiente actualización."""
        ahora = datetime.now()
        self.hora.config(text=texto_hora(ahora, self.formato_24))
        self.fecha.config(text=texto_fecha(ahora))
        # after() pide a tkinter que llame a una función dentro de cierto
        # tiempo, en milisegundos, y regresa de inmediato. Aquí actualizar()
        # se vuelve a programar a sí misma, así el reloj avanza cada
        # segundo sin un ciclo while.
        #
        # No se usa time.sleep(1) porque detiene todo el programa durante
        # ese segundo, incluido el mainloop(). Mientras duerme, la ventana
        # no atiende clics ni se redibuja: se congela y el sistema puede
        # decir que no responde. after() deja libre al mainloop() entre
        # una actualización y otra.
        self.ventana.after(MILISEGUNDOS_POR_SEGUNDO, self.actualizar)

    def cambiar_formato(self):
        """Alterna entre 24 y 12 horas y actualiza el texto del botón."""
        self.formato_24 = not self.formato_24
        if self.formato_24:
            self.boton.config(text="Cambiar a 12 horas")
        else:
            self.boton.config(text="Cambiar a 24 horas")
        ahora = datetime.now()
        self.hora.config(text=texto_hora(ahora, self.formato_24))


def main():
    """Abre el reloj."""
    ventana = tk.Tk()
    App(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
