"""Proyecto 084: Pong.

Juego de tenis de mesa para dos jugadores en la misma computadora. Gana
quien llegue primero a cinco puntos.
"""

import math
import random
from enum import Enum

import pygame

ANCHO = 800
ALTO = 600
FPS = 60
ANCHO_PALETA = 14
ALTO_PALETA = 100
MARGEN_PALETA = 30
VELOCIDAD_PALETA = 420
TAMANO_PELOTA = 14
VELOCIDAD_INICIAL = 360
AUMENTO_POR_GOLPE = 25
VELOCIDAD_MAXIMA = 800
ANGULO_MAXIMO = 55
ESPERA_SAQUE = 1.0
PUNTOS_PARA_GANAR = 5
FONDO = (15, 20, 30)
BLANCO = (235, 235, 235)
GRIS = (90, 90, 110)
COLOR_JUGADOR_1 = (66, 165, 245)
COLOR_JUGADOR_2 = (239, 83, 80)


# Una máquina de estados es una forma de organizar un programa que puede
# estar en una sola situación a la vez, como el menú, la partida o la
# pantalla final. Cada estado decide qué eventos atiende, qué actualiza y
# qué dibuja, y el programa pasa de un estado a otro ante ciertos hechos:
# pulsar Espacio, llegar a cinco puntos. Así cada parte queda separada y
# no hay que revisar diez condiciones mezcladas en cada cuadro.
class Estado(Enum):
    """Estados posibles del juego."""

    MENU = "menu"
    JUGANDO = "jugando"
    FIN = "fin"


class Paleta:
    """Paleta vertical que se mueve con dos teclas."""

    def __init__(self, x: int, tecla_arriba: int, tecla_abajo: int,
                 color: tuple):
        self.rect = pygame.Rect(0, 0, ANCHO_PALETA, ALTO_PALETA)
        # // es la división entera: divide y quita los decimales, así
        # 600 // 2 da 300 y 7 // 2 da 3. Sirve para coordenadas, que
        # deben ser números enteros de píxeles.
        self.rect.center = (x, ALTO // 2)
        self.tecla_arriba = tecla_arriba
        self.tecla_abajo = tecla_abajo
        self.color = color
        self.y = float(self.rect.centery)

    def reiniciar(self):
        """Vuelve al centro vertical."""
        self.y = ALTO / 2
        self.rect.centery = round(self.y)

    def actualizar(self, dt: float):
        """Mueve la paleta con sus teclas sin salir de la ventana."""
        teclas = pygame.key.get_pressed()
        direccion = 0
        if teclas[self.tecla_arriba]:
            direccion = direccion - 1
        if teclas[self.tecla_abajo]:
            direccion = direccion + 1
        self.y = self.y + direccion * VELOCIDAD_PALETA * dt
        mitad = ALTO_PALETA / 2
        self.y = max(mitad, min(self.y, ALTO - mitad))
        self.rect.centery = round(self.y)

    def dibujar(self, pantalla: pygame.Surface):
        """Dibuja la paleta."""
        pygame.draw.rect(pantalla, self.color, self.rect)


class Pelota:
    """Pelota cuadrada con posición y velocidad."""

    def __init__(self):
        self.rect = pygame.Rect(0, 0, TAMANO_PELOTA, TAMANO_PELOTA)
        self.posicion = pygame.Vector2(ANCHO / 2, ALTO / 2)
        self.velocidad = pygame.Vector2(0, 0)
        self.espera = 0.0

    def sacar(self, direccion: int):
        """Pone la pelota en el centro y la lanza hacia un lado."""
        self.posicion = pygame.Vector2(ANCHO / 2, ALTO / 2)
        # math.radians() pasa de grados a radianes, la unidad que usan
        # math.cos() y math.sin(). Con un ángulo y una rapidez, el coseno
        # da la parte horizontal de la velocidad y el seno la vertical.
        angulo = math.radians(random.randint(-30, 30))
        self.velocidad = pygame.Vector2(
            direccion * VELOCIDAD_INICIAL * math.cos(angulo),
            VELOCIDAD_INICIAL * math.sin(angulo),
        )
        # Una pausa corta antes de moverse da tiempo a prepararse
        self.espera = ESPERA_SAQUE
        self.rect.center = (round(self.posicion.x), round(self.posicion.y))

    def actualizar(self, dt: float):
        """Mueve la pelota y la hace rebotar arriba y abajo."""
        if self.espera > 0:
            self.espera = self.espera - dt
            return
        self.posicion = self.posicion + self.velocidad * dt
        mitad = TAMANO_PELOTA / 2
        if self.posicion.y < mitad:
            self.posicion.y = mitad
            self.velocidad.y = abs(self.velocidad.y)
        elif self.posicion.y > ALTO - mitad:
            self.posicion.y = ALTO - mitad
            self.velocidad.y = -abs(self.velocidad.y)
        self.rect.center = (round(self.posicion.x), round(self.posicion.y))

    def rebotar_en(self, paleta: Paleta, direccion: int):
        """Sale hacia direccion con un ángulo según dónde tocó la paleta."""
        # distancia va de -1 (borde de arriba) a 1 (borde de abajo): un
        # golpe en el centro sale recto y uno en la orilla sale inclinado
        distancia = (self.posicion.y - paleta.rect.centery) / (ALTO_PALETA / 2)
        distancia = max(-1, min(distancia, 1))
        angulo = math.radians(distancia * ANGULO_MAXIMO)
        rapidez = min(self.velocidad.length() + AUMENTO_POR_GOLPE,
                      VELOCIDAD_MAXIMA)
        self.velocidad = pygame.Vector2(
            direccion * rapidez * math.cos(angulo),
            rapidez * math.sin(angulo),
        )

    def dibujar(self, pantalla: pygame.Surface):
        """Dibuja la pelota."""
        pygame.draw.rect(pantalla, BLANCO, self.rect)


class Juego:
    """Partida de Pong con menú, juego y pantalla final."""

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Pong")
        self.reloj = pygame.time.Clock()
        # font.Font() carga una fuente para escribir texto. None es el
        # valor de Python que significa "nada" o "sin valor"; aquí le dice
        # a pygame que no hay archivo de fuente y use la suya por defecto.
        self.fuente_grande = pygame.font.Font(None, 80)
        self.fuente = pygame.font.Font(None, 36)
        self.ejecutando = True
        self.estado = Estado.MENU
        self.jugador_1 = Paleta(MARGEN_PALETA, pygame.K_w, pygame.K_s,
                                COLOR_JUGADOR_1)
        self.jugador_2 = Paleta(ANCHO - MARGEN_PALETA, pygame.K_UP,
                                pygame.K_DOWN, COLOR_JUGADOR_2)
        self.pelota = Pelota()
        self.puntos_1 = 0
        self.puntos_2 = 0
        self.ganador = ""

    def empezar_partida(self):
        """Reinicia marcador y posiciones y pasa al estado JUGANDO."""
        self.puntos_1 = 0
        self.puntos_2 = 0
        self.jugador_1.reiniciar()
        self.jugador_2.reiniciar()
        self.pelota.sacar(random.choice([-1, 1]))
        self.estado = Estado.JUGANDO

    def manejar_eventos(self):
        """Atiende el cierre y la tecla Espacio según el estado."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.ejecutando = False
                elif evento.key == pygame.K_SPACE:
                    # Espacio hace algo distinto según el estado actual
                    if self.estado == Estado.MENU:
                        self.empezar_partida()
                    elif self.estado == Estado.FIN:
                        self.estado = Estado.MENU

    def actualizar(self, dt: float):
        """Solo hay movimiento mientras se está jugando."""
        if self.estado != Estado.JUGANDO:
            return
        self.jugador_1.actualizar(dt)
        self.jugador_2.actualizar(dt)
        self.pelota.actualizar(dt)
        self.revisar_golpes()
        self.revisar_puntos()

    def revisar_golpes(self):
        """Hace rebotar la pelota si choca con una paleta."""
        # colliderect() devuelve True si dos rectángulos se enciman. Solo
        # se rebota si la pelota va hacia la paleta; si no, al quedar un
        # instante encimada rebotaría de nuevo y se quedaría atorada.
        pelota = self.pelota
        if pelota.rect.colliderect(self.jugador_1.rect):
            if pelota.velocidad.x < 0:
                pelota.rebotar_en(self.jugador_1, 1)
        elif pelota.rect.colliderect(self.jugador_2.rect):
            if pelota.velocidad.x > 0:
                pelota.rebotar_en(self.jugador_2, -1)

    def revisar_puntos(self):
        """Suma un punto si la pelota sale por un lado y revisa el final."""
        if self.pelota.rect.right < 0:
            self.puntos_2 = self.puntos_2 + 1
            self.pelota.sacar(-1)
        elif self.pelota.rect.left > ANCHO:
            self.puntos_1 = self.puntos_1 + 1
            self.pelota.sacar(1)

        if self.puntos_1 == PUNTOS_PARA_GANAR:
            self.ganador = "Jugador 1"
            self.estado = Estado.FIN
        elif self.puntos_2 == PUNTOS_PARA_GANAR:
            self.ganador = "Jugador 2"
            self.estado = Estado.FIN

    def escribir(self, texto: str, fuente: pygame.font.Font, color: tuple,
                 centro: tuple):
        """Dibuja un texto centrado en el punto indicado."""
        # render() convierte el texto en una superficie que se puede
        # copiar con blit(); True suaviza los bordes de las letras
        superficie = fuente.render(texto, True, color)
        rect = superficie.get_rect(center=centro)
        self.pantalla.blit(superficie, rect)

    def dibujar_cancha(self, con_pelota: bool = True):
        """Dibuja la línea central, el marcador, las paletas y la pelota."""
        for y in range(0, ALTO, 30):
            pygame.draw.rect(self.pantalla, GRIS, (ANCHO // 2 - 2, y, 4, 15))
        self.escribir(str(self.puntos_1), self.fuente_grande,
                      COLOR_JUGADOR_1, (ANCHO // 4, 60))
        self.escribir(str(self.puntos_2), self.fuente_grande,
                      COLOR_JUGADOR_2, (ANCHO * 3 // 4, 60))
        self.jugador_1.dibujar(self.pantalla)
        self.jugador_2.dibujar(self.pantalla)
        if con_pelota:
            self.pelota.dibujar(self.pantalla)

    def dibujar(self):
        """Dibuja la pantalla del estado actual."""
        self.pantalla.fill(FONDO)
        centro_x = ANCHO // 2
        if self.estado == Estado.MENU:
            self.escribir("PONG", self.fuente_grande, BLANCO, (centro_x, 200))
            self.escribir("Jugador 1: W y S", self.fuente, COLOR_JUGADOR_1,
                          (centro_x, 300))
            self.escribir("Jugador 2: flechas", self.fuente, COLOR_JUGADOR_2,
                          (centro_x, 340))
            self.escribir("Pulsa Espacio para empezar", self.fuente, BLANCO,
                          (centro_x, 430))
        elif self.estado == Estado.JUGANDO:
            self.dibujar_cancha()
        else:
            self.dibujar_cancha(con_pelota=False)
            self.escribir(f"Gana el {self.ganador}", self.fuente_grande,
                          BLANCO, (centro_x, ALTO // 2))
            self.escribir("Espacio para volver al menú", self.fuente, BLANCO,
                          (centro_x, ALTO // 2 + 70))
        pygame.display.flip()

    def ejecutar(self):
        """Ciclo de juego: eventos, actualizar y dibujar."""
        while self.ejecutando:
            dt = self.reloj.tick(FPS) / 1000
            self.manejar_eventos()
            self.actualizar(dt)
            self.dibujar()
        pygame.quit()


def main():
    """Crea el juego y lo ejecuta."""
    Juego().ejecutar()


if __name__ == "__main__":
    main()
