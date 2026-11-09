"""Proyecto 079: Lista de tareas con interfaz.

Una ventana para agregar, eliminar y marcar tareas como hechas. Las tareas
se guardan en un archivo al cerrar y se recuperan al volver a abrir.
"""

import tkinter as tk
from dataclasses import dataclass
from tkinter import messagebox

ARCHIVO = "tareas.txt"
MARCA_HECHA = "[x] "
MARCA_PENDIENTE = "[ ] "


@dataclass
class Tarea:
    """Tarea con su título y si ya está hecha."""

    titulo: str
    hecha: bool = False

    def como_texto(self) -> str:
        """Devuelve la tarea con su casilla, como se ve y se guarda."""
        if self.hecha:
            return MARCA_HECHA + self.titulo
        return MARCA_PENDIENTE + self.titulo


def cargar_tareas() -> list[Tarea]:
    """Lee las tareas del archivo. Si todavía no existe, no hay tareas."""
    tareas = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                linea = linea.rstrip("\n")
                # Cada línea empieza con su casilla de 4 caracteres
                hecha = linea.startswith(MARCA_HECHA)
                titulo = linea[4:]
                if titulo != "":
                    tareas.append(Tarea(titulo, hecha))
    except FileNotFoundError:
        return []
    return tareas


def guardar_tareas(tareas: list[Tarea]):
    """Escribe todas las tareas en el archivo, una por línea."""
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            archivo.write(tarea.como_texto() + "\n")


class App:
    """Ventana con la lista de tareas y sus botones."""

    def __init__(self, ventana: tk.Tk):
        self.ventana = ventana
        self.ventana.title("Lista de tareas")
        self.tareas = cargar_tareas()

        marco_entrada = tk.Frame(ventana)
        marco_entrada.pack(padx=10, pady=10, fill="x")
        self.entrada = tk.Entry(marco_entrada, font=("Arial", 12))
        # side="left" acomoda los widgets uno junto a otro y expand=True
        # hace que la caja ocupe el espacio que sobra
        self.entrada.pack(side="left", fill="x", expand=True)
        tk.Button(
            marco_entrada, text="Agregar", command=self.agregar,
        ).pack(side="left", padx=5)

        # bind() conecta un evento con una función. "<Return>" es la tecla
        # Enter: al pulsarla en la caja de texto se agrega la tarea, igual
        # que con el botón. tkinter le pasa a la función un objeto con los
        # datos del evento; la lambda lo recibe y no lo necesita.
        self.entrada.bind("<Return>", lambda evento: self.agregar())

        marco_lista = tk.Frame(ventana)
        marco_lista.pack(padx=10, fill="both", expand=True)
        # Listbox muestra una lista de textos y deja seleccionar uno
        self.lista = tk.Listbox(
            marco_lista, font=("Arial", 12), width=40, height=12,
        )
        self.lista.pack(side="left", fill="both", expand=True)
        # Scrollbar es la barra de desplazamiento. Se conectan en los dos
        # sentidos: la lista avisa a la barra cuánto se ha movido con
        # yscrollcommand, y la barra mueve la lista con yview.
        barra = tk.Scrollbar(marco_lista, command=self.lista.yview)
        barra.pack(side="right", fill="y")
        self.lista.config(yscrollcommand=barra.set)
        # Doble clic sobre una tarea la marca o desmarca
        self.lista.bind("<Double-Button-1>", lambda evento: self.marcar())

        marco_botones = tk.Frame(ventana)
        marco_botones.pack(pady=10)
        tk.Button(
            marco_botones, text="Marcar como hecha", command=self.marcar,
        ).pack(side="left", padx=5)
        tk.Button(
            marco_botones, text="Eliminar", command=self.eliminar,
        ).pack(side="left", padx=5)

        # protocol() cambia lo que pasa al cerrar la ventana con la X:
        # en lugar de cerrarse directo, se llama a cerrar(), que guarda
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar)

        self.mostrar_tareas()
        self.entrada.focus()

    def mostrar_tareas(self):
        """Vuelve a llenar la Listbox con las tareas actuales."""
        # delete(0, tk.END) borra desde el primer elemento hasta el último
        self.lista.delete(0, tk.END)
        for indice, tarea in enumerate(self.tareas):
            self.lista.insert(tk.END, tarea.como_texto())
            # itemconfig() cambia el estilo de un solo elemento
            if tarea.hecha:
                self.lista.itemconfig(indice, fg="gray")

    def indice_seleccionado(self) -> int:
        """Devuelve la posición elegida, o -1 si no hay ninguna."""
        # curselection() devuelve una tupla con las posiciones elegidas
        seleccion = self.lista.curselection()
        if len(seleccion) == 0:
            messagebox.showinfo("Sin selección", "Primero elige una tarea.")
            return -1
        return seleccion[0]

    def agregar(self):
        """Agrega la tarea escrita y limpia la caja de texto."""
        titulo = self.entrada.get().strip()
        if titulo == "":
            return
        self.tareas.append(Tarea(titulo))
        self.entrada.delete(0, tk.END)
        self.mostrar_tareas()

    def marcar(self):
        """Cambia la tarea elegida entre hecha y pendiente."""
        indice = self.indice_seleccionado()
        if indice == -1:
            return
        tarea = self.tareas[indice]
        tarea.hecha = not tarea.hecha
        self.mostrar_tareas()
        self.lista.selection_set(indice)

    def eliminar(self):
        """Borra la tarea elegida."""
        indice = self.indice_seleccionado()
        if indice == -1:
            return
        del self.tareas[indice]
        self.mostrar_tareas()

    def cerrar(self):
        """Guarda las tareas y cierra la ventana."""
        guardar_tareas(self.tareas)
        # destroy() cierra la ventana y termina el mainloop()
        self.ventana.destroy()


def main():
    """Abre la lista de tareas."""
    ventana = tk.Tk()
    App(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
