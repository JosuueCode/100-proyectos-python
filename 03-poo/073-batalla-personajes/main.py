"""Proyecto 073: Batalla de personajes.

Un guerrero, un mago y un arquero se enfrentan en combates por turnos. Cada
uno ataca con daño aleatorio y cada tres turnos usa su habilidad especial.
"""

import random
from abc import ABC, abstractmethod

TURNOS_PARA_HABILIDAD = 3


class Personaje(ABC):
    """Personaje con vida protegida, ataque normal y habilidad especial."""

    def __init__(self, nombre, vida_maxima, ataque_minimo, ataque_maximo):
        if vida_maxima <= 0:
            raise ValueError("La vida máxima debe ser mayor que cero.")
        if ataque_minimo > ataque_maximo:
            raise ValueError("El ataque mínimo no puede superar al máximo.")
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.ataque_minimo = ataque_minimo
        self.ataque_maximo = ataque_maximo
        self.turnos = 0
        self.__vida = vida_maxima

    @property
    def vida(self):
        """Devuelve la vida actual."""
        return self.__vida

    # @vida.setter define qué pasa al asignar personaje.vida = valor. En
    # el proyecto 052 la propiedad era de solo lectura; con un setter se
    # puede asignar, pero el valor pasa antes por este método. Aquí se
    # recorta para que la vida nunca baje de 0 ni pase del máximo.
    @vida.setter
    def vida(self, valor):
        if valor < 0:
            valor = 0
        if valor > self.vida_maxima:
            valor = self.vida_maxima
        self.__vida = valor

    def esta_vivo(self):
        """Devuelve True si le queda vida."""
        return self.vida > 0

    def recibir_dano(self, cantidad):
        """Resta vida. El setter impide que quede negativa."""
        self.vida = self.vida - cantidad

    def atacar(self, objetivo):
        """Ataque normal con daño aleatorio entre el mínimo y el máximo."""
        dano = random.randint(self.ataque_minimo, self.ataque_maximo)
        print(f"  {self.nombre} ataca a {objetivo.nombre}: {dano} de daño")
        objetivo.recibir_dano(dano)

    @abstractmethod
    def habilidad_especial(self, objetivo):
        """Cada tipo de personaje define su propia habilidad."""

    def tomar_turno(self, objetivo):
        """Usa la habilidad cada cierto número de turnos y si no, ataca."""
        self.turnos = self.turnos + 1
        if self.turnos % TURNOS_PARA_HABILIDAD == 0:
            self.habilidad_especial(objetivo)
        else:
            self.atacar(objetivo)

    def descansar(self):
        """Recupera toda la vida y reinicia el conteo de turnos."""
        self.vida = self.vida_maxima
        self.turnos = 0

    def estado(self):
        """Devuelve el nombre con su vida actual y máxima."""
        return f"{self.nombre} {self.vida}/{self.vida_maxima}"


class Guerrero(Personaje):
    """Mucha vida y golpes fuertes."""

    def __init__(self, nombre):
        super().__init__(nombre, 112, 9, 15)

    def habilidad_especial(self, objetivo):
        """Golpe furioso: el doble de un ataque normal."""
        dano = random.randint(self.ataque_minimo, self.ataque_maximo) * 2
        print(f"  {self.nombre} usa Golpe furioso: {dano} de daño")
        objetivo.recibir_dano(dano)


class Mago(Personaje):
    """Poca vida, pero puede curarse."""

    def __init__(self, nombre):
        super().__init__(nombre, 90, 9, 20)

    def habilidad_especial(self, objetivo):
        """Curación: recupera vida sin pasar del máximo."""
        antes = self.vida
        self.vida = self.vida + 30
        recuperada = self.vida - antes
        print(f"  {self.nombre} usa Curación: recupera {recuperada} de vida")


class Arquero(Personaje):
    """Vida media y varios disparos a la vez."""

    def __init__(self, nombre):
        super().__init__(nombre, 100, 9, 16)

    def habilidad_especial(self, objetivo):
        """Lluvia de flechas: tres flechas de daño pequeño."""
        total = 0
        for _ in range(3):
            total = total + random.randint(6, 11)
        print(f"  {self.nombre} usa Lluvia de flechas: {total} de daño")
        objetivo.recibir_dano(total)


def combate(primero, segundo):
    """Alterna turnos hasta que uno se queda sin vida. Devuelve al ganador."""
    print(f"Combate: {primero.nombre} contra {segundo.nombre}")
    atacante = primero
    defensor = segundo
    ronda = 1
    while primero.esta_vivo() and segundo.esta_vivo():
        print(f"Ronda {ronda}")
        atacante.tomar_turno(defensor)
        print(f"  {primero.estado()} | {segundo.estado()}")
        # Se intercambian los papeles para el siguiente turno
        atacante, defensor = defensor, atacante
        ronda = ronda + 1

    # Quien atacó al final es ahora el defensor, porque ya se cambiaron
    ganador = defensor
    print(f"Gana {ganador.nombre} con {ganador.vida} de vida.")
    return ganador


def main():
    """Organiza dos combates: el ganador del primero pelea el segundo."""
    guerrero = Guerrero("Brenda la guerrera")
    mago = Mago("Merlín el mago")
    arquero = Arquero("Tomás el arquero")

    ganador = combate(guerrero, mago)
    print()
    # El ganador descansa antes de la final para pelear en igualdad
    ganador.descansar()
    campeon = combate(arquero, ganador)
    print()
    print(f"Campeón del torneo: {campeon.nombre}")


if __name__ == "__main__":
    main()
