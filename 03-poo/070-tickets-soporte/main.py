"""Proyecto 070: Sistema de tickets.

Un sistema de soporte técnico que registra tickets, los asigna a agentes y
controla que cada ticket pase por sus estados en un orden permitido.
"""

# enum es el módulo de la biblioteca estándar para crear enumeraciones
from enum import Enum


# Una enumeración es una clase con un grupo fijo de valores con nombre.
# Para crearla se hereda de Enum. Cada estado es un objeto único: no se
# puede escribir mal como un texto suelto ni inventar un estado nuevo.
# Cada uno tiene un .name, como "EN_PROCESO", y un .value, como
# "en proceso".
class Estado(Enum):
    """Estados por los que pasa un ticket."""

    ABIERTO = "abierto"
    EN_PROCESO = "en proceso"
    RESUELTO = "resuelto"
    CERRADO = "cerrado"


# A qué estados se puede pasar desde cada uno. Un ticket resuelto se puede
# reabrir si el problema vuelve, pero uno cerrado ya no cambia.
TRANSICIONES = {
    Estado.ABIERTO: [Estado.EN_PROCESO, Estado.CERRADO],
    Estado.EN_PROCESO: [Estado.RESUELTO, Estado.ABIERTO],
    Estado.RESUELTO: [Estado.CERRADO, Estado.EN_PROCESO],
    Estado.CERRADO: [],
}


class ErrorTickets(Exception):
    """Error base del sistema de tickets."""


class TransicionInvalidaError(ErrorTickets):
    """El ticket no puede pasar del estado actual al pedido."""

    def __init__(self, ticket, nuevo_estado):
        actual = ticket.estado.value
        nuevo = nuevo_estado.value
        mensaje = f"El ticket {ticket.numero} no puede pasar de {actual}"
        super().__init__(f"{mensaje} a {nuevo}.")
        self.ticket = ticket
        self.nuevo_estado = nuevo_estado


class TicketNoEncontradoError(ErrorTickets):
    """No existe un ticket con ese número."""


class Ticket:
    """Reporte de un problema con número, título, estado y agente."""

    def __init__(self, numero, titulo):
        self.numero = numero
        self.titulo = titulo
        self.estado = Estado.ABIERTO
        self.agente = "sin asignar"

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado. Lanza TransicionInvalidaError si no se puede."""
        if nuevo_estado not in TRANSICIONES[self.estado]:
            raise TransicionInvalidaError(self, nuevo_estado)
        self.estado = nuevo_estado

    def __str__(self):
        """Devuelve el número, el título y el agente del ticket."""
        return f"#{self.numero} {self.titulo} ({self.agente})"


class Agente:
    """Persona de soporte que atiende tickets."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.tickets = []


class SistemaTickets:
    """Registra tickets, los asigna y los lista por estado."""

    def __init__(self):
        self.tickets = {}
        self.siguiente_numero = 1

    def crear_ticket(self, titulo):
        """Crea un ticket con el siguiente número y lo devuelve."""
        ticket = Ticket(self.siguiente_numero, titulo)
        self.tickets[ticket.numero] = ticket
        self.siguiente_numero = self.siguiente_numero + 1
        return ticket

    def buscar(self, numero):
        """Devuelve el ticket. Lanza TicketNoEncontradoError si no existe."""
        if numero not in self.tickets:
            raise TicketNoEncontradoError(f"No existe el ticket {numero}.")
        return self.tickets[numero]

    def asignar(self, numero, agente):
        """Asigna el ticket a un agente y lo pasa a en proceso."""
        ticket = self.buscar(numero)
        # Si el ticket está cerrado, cambiar_estado() lanza el error antes
        # de que se asigne
        if ticket.estado != Estado.EN_PROCESO:
            ticket.cambiar_estado(Estado.EN_PROCESO)
        ticket.agente = agente.nombre
        agente.tickets.append(ticket)
        print(f"Ticket {numero} asignado a {agente.nombre}.")

    def cambiar_estado(self, numero, nuevo_estado):
        """Busca el ticket y cambia su estado."""
        ticket = self.buscar(numero)
        ticket.cambiar_estado(nuevo_estado)
        print(f"Ticket {numero} ahora está {nuevo_estado.value}.")

    def listar_por_estado(self):
        """Muestra los tickets agrupados por estado."""
        # Un for sobre la clase Enum recorre sus valores en el orden en que
        # se declararon
        for estado in Estado:
            print(f"{estado.value.capitalize()}:")
            hay_tickets = False
            for ticket in self.tickets.values():
                if ticket.estado == estado:
                    print(f"  {ticket}")
                    hay_tickets = True
            if not hay_tickets:
                print("  Ninguno")


def intentar(accion, numero, dato):
    """Ejecuta una acción del sistema y muestra el error si lo hay."""
    try:
        accion(numero, dato)
    except ErrorTickets as error:
        print(f"Error: {error}")


def main():
    """Registra tickets, los mueve entre estados y los lista."""
    sistema = SistemaTickets()
    sistema.crear_ticket("No enciende la impresora")
    sistema.crear_ticket("Olvidé mi contraseña")
    sistema.crear_ticket("El internet está lento")
    sistema.crear_ticket("Pantalla parpadea")
    sistema.crear_ticket("Instalar programa de diseño")

    marta = Agente("Marta")
    jorge = Agente("Jorge")

    # Un método también se puede pasar como argumento, sin paréntesis:
    # intentar() lo llama después con los datos que recibe
    intentar(sistema.asignar, 1, marta)
    intentar(sistema.asignar, 2, jorge)
    intentar(sistema.asignar, 3, marta)
    intentar(sistema.asignar, 9, jorge)
    print()

    intentar(sistema.cambiar_estado, 2, Estado.RESUELTO)
    intentar(sistema.cambiar_estado, 2, Estado.CERRADO)
    intentar(sistema.cambiar_estado, 1, Estado.RESUELTO)
    intentar(sistema.cambiar_estado, 4, Estado.RESUELTO)
    intentar(sistema.cambiar_estado, 5, Estado.CERRADO)
    intentar(sistema.cambiar_estado, 2, Estado.ABIERTO)
    intentar(sistema.asignar, 5, jorge)
    print()

    sistema.listar_por_estado()
    print()
    print(f"Tickets asignados a Marta: {len(marta.tickets)}")
    print(f"Tickets asignados a Jorge: {len(jorge.tickets)}")


if __name__ == "__main__":
    main()
