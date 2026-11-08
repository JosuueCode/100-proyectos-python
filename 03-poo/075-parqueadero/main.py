"""Proyecto 075: Sistema de parqueadero.

Un estacionamiento con espacios para autos, motos y camionetas. Registra la
entrada con un ticket, calcula el tiempo de estancia y cobra al salir según
la tarifa de cada tipo de vehículo.
"""

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass

# datetime es el módulo de la biblioteca estándar para fechas y horas. La
# clase datetime guarda un momento exacto: año, mes, día, hora y minuto.
from datetime import datetime
from enum import Enum


class TipoEspacio(Enum):
    """Tipos de espacio del estacionamiento."""

    AUTO = "auto"
    MOTO = "moto"
    CAMIONETA = "camioneta"


class ErrorParqueadero(Exception):
    """Error base del estacionamiento."""


class SinEspacioError(ErrorParqueadero):
    """No quedan espacios libres para ese tipo de vehículo."""


class VehiculoNoEncontradoError(ErrorParqueadero):
    """No hay ningún vehículo con esa placa dentro."""


class VehiculoYaDentroError(ErrorParqueadero):
    """El vehículo ya tiene un ticket abierto."""


class Vehiculo(ABC):
    """Vehículo con placa. Cada tipo define su espacio y su tarifa."""

    def __init__(self, placa: str):
        placa = placa.strip().upper()
        if placa == "":
            raise ValueError("La placa no puede estar vacía.")
        self.placa = placa

    @abstractmethod
    def tarifa_por_hora(self) -> float:
        """Devuelve cuánto cuesta cada hora o fracción."""

    def calcular_cobro(self, horas: int) -> float:
        """Devuelve el cobro por las horas de estancia."""
        return horas * self.tarifa_por_hora()

    def __str__(self) -> str:
        """Devuelve el tipo y la placa."""
        return f"{self.tipo.value} {self.placa}"


class Auto(Vehiculo):
    """Auto: ocupa un espacio normal."""

    tipo = TipoEspacio.AUTO

    def tarifa_por_hora(self) -> float:
        """Tarifa de los autos."""
        return 25


class Moto(Vehiculo):
    """Moto: tarifa baja y un tope de cobro por estancia."""

    tipo = TipoEspacio.MOTO
    COBRO_MAXIMO = 60

    def tarifa_por_hora(self) -> float:
        """Tarifa de las motos."""
        return 12

    def calcular_cobro(self, horas: int) -> float:
        """Usa el cálculo general, pero nunca cobra más del tope."""
        return min(super().calcular_cobro(horas), Moto.COBRO_MAXIMO)


class Camioneta(Vehiculo):
    """Camioneta: ocupa un espacio grande y paga más."""

    tipo = TipoEspacio.CAMIONETA

    def tarifa_por_hora(self) -> float:
        """Tarifa de las camionetas."""
        return 40


@dataclass
class Ticket:
    """Comprobante de entrada de un vehículo."""

    folio: int
    vehiculo: Vehiculo
    entrada: datetime

    def mostrar(self):
        """Muestra el folio, el vehículo y la hora de entrada."""
        # strftime() convierte una fecha en texto con el formato indicado:
        # %d es el día, %m el mes, %Y el año, %H la hora y %M los minutos
        hora = self.entrada.strftime("%d/%m/%Y %H:%M")
        print(f"  Ticket {self.folio}: {self.vehiculo}, entró {hora}")


class Parqueadero:
    """Estacionamiento con espacios por tipo y tickets abiertos."""

    def __init__(self, nombre: str, capacidad: dict[TipoEspacio, int]):
        self.nombre = nombre
        self.capacidad = capacidad
        self.tickets: dict[str, Ticket] = {}
        self.siguiente_folio = 1
        self.recaudado: float = 0

    def ocupados(self, tipo: TipoEspacio) -> int:
        """Devuelve cuántos espacios de ese tipo están ocupados."""
        cuenta = 0
        for ticket in self.tickets.values():
            if ticket.vehiculo.tipo == tipo:
                cuenta = cuenta + 1
        return cuenta

    def libres(self, tipo: TipoEspacio) -> int:
        """Devuelve cuántos espacios de ese tipo quedan."""
        return self.capacidad[tipo] - self.ocupados(tipo)

    def registrar_entrada(self, vehiculo: Vehiculo, hora: datetime) -> Ticket:
        """Da un ticket al vehículo. Lanza un error si no puede entrar."""
        if vehiculo.placa in self.tickets:
            raise VehiculoYaDentroError(f"{vehiculo.placa} ya está dentro.")
        if self.libres(vehiculo.tipo) == 0:
            raise SinEspacioError(f"No hay espacio libre para {vehiculo}.")

        ticket = Ticket(self.siguiente_folio, vehiculo, hora)
        self.tickets[vehiculo.placa] = ticket
        self.siguiente_folio = self.siguiente_folio + 1
        ticket.mostrar()
        return ticket

    def registrar_salida(self, placa: str, hora: datetime) -> float:
        """Cierra el ticket, calcula el cobro y lo devuelve."""
        placa = placa.strip().upper()
        if placa not in self.tickets:
            raise VehiculoNoEncontradoError(f"No hay ningún {placa} dentro.")
        ticket = self.tickets[placa]
        if hora < ticket.entrada:
            raise ValueError("La salida no puede ser antes de la entrada.")

        # Restar dos datetime da un timedelta: la duración entre los dos
        # momentos. total_seconds() la devuelve en segundos.
        estancia = hora - ticket.entrada
        minutos = estancia.total_seconds() / 60
        # math.ceil() redondea hacia arriba: 61 minutos cuentan como 2
        # horas, porque se cobra cada hora o fracción. Mínimo se cobra 1.
        horas = max(math.ceil(minutos / 60), 1)
        cobro = ticket.vehiculo.calcular_cobro(horas)

        del self.tickets[placa]
        self.recaudado = self.recaudado + cobro
        tiempo = f"{minutos:.0f} min, se cobran {horas} h"
        print(f"  Sale {ticket.vehiculo}: {tiempo}, ${cobro:.2f}")
        return cobro

    def mostrar_ocupacion(self):
        """Muestra los espacios libres de cada tipo."""
        print(f"Ocupación de {self.nombre}:")
        for tipo in TipoEspacio:
            libres = self.libres(tipo)
            total = self.capacidad[tipo]
            print(f"  {tipo.value:<10} {libres} libres de {total}")


def entrar(parqueadero: Parqueadero, vehiculo: Vehiculo, hora: datetime):
    """Registra una entrada y muestra el error si lo hay."""
    try:
        parqueadero.registrar_entrada(vehiculo, hora)
    except ErrorParqueadero as error:
        print(f"  Error: {error}")


def salir(parqueadero: Parqueadero, placa: str, hora: datetime):
    """Registra una salida y muestra el error si lo hay."""
    try:
        parqueadero.registrar_salida(placa, hora)
    except ErrorParqueadero as error:
        print(f"  Error: {error}")
    except ValueError as error:
        print(f"  Error: {error}")


def a_las(hora: int, minuto: int) -> datetime:
    """Devuelve un datetime de hoy a la hora indicada."""
    # Las horas se fijan a mano para que el ejemplo dé siempre lo mismo.
    # En un sistema real se usaría datetime.now(), la hora del momento.
    hoy = datetime.now()
    return datetime(hoy.year, hoy.month, hoy.day, hora, minuto)


def main():
    """Simula un día del estacionamiento."""
    capacidad = {
        TipoEspacio.AUTO: 2,
        TipoEspacio.MOTO: 2,
        TipoEspacio.CAMIONETA: 1,
    }
    parqueadero = Parqueadero("Estacionamiento Centro", capacidad)

    print("Entradas:")
    entrar(parqueadero, Auto("abc-123"), a_las(8, 0))
    entrar(parqueadero, Moto("mto-45"), a_las(8, 15))
    entrar(parqueadero, Camioneta("cam-900"), a_las(9, 0))
    entrar(parqueadero, Auto("xyz-789"), a_las(9, 30))
    entrar(parqueadero, Camioneta("cam-111"), a_las(9, 40))
    entrar(parqueadero, Auto("abc-123"), a_las(10, 0))
    try:
        Auto("   ")
    except ValueError as error:
        print(f"  Error: {error}")
    print()
    parqueadero.mostrar_ocupacion()
    print()

    print("Salidas:")
    salir(parqueadero, "abc-123", a_las(9, 1))
    salir(parqueadero, "MTO-45", a_las(15, 30))
    salir(parqueadero, "cam-900", a_las(9, 40))
    salir(parqueadero, "zzz-000", a_las(12, 0))
    salir(parqueadero, "xyz-789", a_las(9, 0))
    print()
    parqueadero.mostrar_ocupacion()
    print(f"Total recaudado: ${parqueadero.recaudado:.2f}")


if __name__ == "__main__":
    main()
