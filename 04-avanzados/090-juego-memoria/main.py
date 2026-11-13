"""Proyecto 090: Juego de memoria.

Dieciséis cartas boca abajo esconden ocho parejas de figuras. Volteas dos
a la vez: si son iguales se quedan descubiertas y si no, se vuelven a
tapar. Gana encontrando todas las parejas.
"""

import math
import random
from enum import Enum

import pygame

COLUMNAS = 4
FILAS = 4
ANCHO_CARTA = 120
ALTO_CARTA = 120
SEPARACION = 16
ALTO_BARRA = 60
ANCHO = COLUMNAS * ANCHO_CARTA + (COLUMNAS + 1) * SEPARACION
ALTO = FILAS * ALTO_CARTA + (FILAS + 1) * SEPARACION + ALTO_BARRA
FPS = 60
ESPERA_MILISEGUNDOS = 800
FONDO = (33, 33, 48)
REVERSO = (63, 81, 181)
REVERSO_DETALLE = (92, 107, 192)
CARA = (245, 245, 245)
ENCONTRADA = (200, 230, 201)
BLANCO = (240, 240, 240)
OSCURECER = (0, 0, 0, 170)
# Cada pareja es una figura con su color
FIGURAS = [
    ("circulo", (229, 57, 53)), ("cuadro", (30, 136, 229)),
    ("triangulo", (67, 160, 71)), ("rombo", (251, 140, 0)),
    ("cruz", (142, 36, 170)), ("anillo", (0, 172, 193)),
    ("estrella", (253, 216, 53)), ("hexagono", (109, 76, 65)),
]


class Estado(Enum):
    """Estados del juego."""

    ELIGIENDO = "eligiendo"
    ESPERANDO = "esperando"
    VICTORIA = "victoria"


def puntos_de_poligono(centro: tuple, radio: float, lados: int,
                       giro: float) -> list:
    """Devuelve los vértices de un polígono regular."""
    puntos = []
    for i in range(lados):
        angulo = math.radians(giro + i * 360 / lados)
        x = centro[0] + radio * math.cos(angulo)
        y = centro[1] + radio * math.sin(angulo)
        puntos.append((x, y))
    return puntos


def puntos_de_estrella(centro: tuple, radio: float) -> list:
    """Devuelve los diez vértices de una estrella de cinco picos."""
    puntos = []
    for i in range(10):
        # Los vértices alternan entre la punta y el hueco entre puntas
        if i % 2 == 0:
            distancia = radio
        else:
            distancia = radio * 0.45
        angulo = math.radians(-90 + i * 36)
        puntos.append((centro[0] + distancia * math.cos(angulo),
                       centro[1] + distancia * math.sin(angulo)))
    return puntos


class Carta:
    """Carta con una figura que puede estar tapada o descubierta."""

    def __init__(self, figura: str, color: tuple):
        self.figura = figura
        self.color = color
        self.rect = pygame.Rect(0, 0, ANCHO_CARTA, ALTO_CARTA)
        self.descubierta = False
        self.encontrada = False

    def es_pareja_de(self, otra) -> bool:
        """Devuelve True si las dos cartas tienen la misma figura."""
        return self.figura == otra.figura

    def dibujar(self, pantalla: pygame.Surface):
        """Dibuja el reverso o la cara con su figura."""
        if not self.descubierta:
            pygame.draw.rect(pantalla, REVERSO, self.rect, border_radius=12)
            pygame.draw.rect(pantalla, REVERSO_DETALLE,
                             self.rect.inflate(-24, -24), 4,
                             border_radius=8)
            return
        if self.encontrada:
            fondo = ENCONTRADA
        else:
            fondo = CARA
        pygame.draw.rect(pantalla, fondo, self.rect, border_radius=12)
        self.dibujar_figura(pantalla)

    def dibujar_figura(self, pantalla: pygame.Surface):
        """Dibuja la figura de la carta en su centro."""
        centro = self.rect.center
        radio = 34
        color = self.color
        if self.figura == "circulo":
            pygame.draw.circle(pantalla, color, centro, radio)
        elif self.figura == "cuadro":
            cuadro = pygame.Rect(0, 0, radio * 2 - 8, radio * 2 - 8)
            cuadro.center = centro
            pygame.draw.rect(pantalla, color, cuadro)
        elif self.figura == "triangulo":
            puntos = puntos_de_poligono(centro, radio + 4, 3, -90)
            pygame.draw.polygon(pantalla, color, puntos)
        elif self.figura == "rombo":
            puntos = puntos_de_poligono(centro, radio + 2, 4, -90)
            pygame.draw.polygon(pantalla, color, puntos)
        elif self.figura == "cruz":
            horizontal = pygame.Rect(0, 0, radio * 2, 20)
            vertical = pygame.Rect(0, 0, 20, radio * 2)
            horizontal.center = centro
            vertical.center = centro
            pygame.draw.rect(pantalla, color, horizontal)
            pygame.draw.rect(pantalla, color, vertical)
        elif self.figura == "anillo":
            pygame.draw.circle(pantalla, color, centro, radio, 12)
        elif self.figura == "estrella":
            puntos = puntos_de_estrella(centro, radio + 4)
            pygame.draw.polygon(pantalla, color, puntos)
        else:
            puntos = puntos_de_poligono(centro, radio, 6, 0)
            pygame.draw.polygon(pantalla, color, puntos)


class Juego:
    """Tablero de memoria con contador de movimientos y tiempo."""

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Juego de memoria")
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 34)
        self.fuente_grande = pygame.font.Font(None, 72)
        self.ejecutando = True
        self.reiniciar()

    def reiniciar(self):
        """Baraja las cartas y empieza una partida nueva."""
        self.cartas = []
        for figura, color in FIGURAS:
            self.cartas.append(Carta(figura, color))
            self.cartas.append(Carta(figura, color))
        # random.shuffle() revuelve la lista en su lugar: cambia el orden
        # de sus elementos al azar y no devuelve una lista nueva
        random.shuffle(self.cartas)
        for indice, carta in enumerate(self.cartas):
            fila = indice // COLUMNAS
            columna = indice % COLUMNAS
            x = SEPARACION + columna * (ANCHO_CARTA + SEPARACION)
            y = ALTO_BARRA + SEPARACION + fila * (ALTO_CARTA + SEPARACION)
            carta.rect.topleft = (x, y)

        self.elegidas = []
        self.movimientos = 0
        self.parejas = 0
        # get_ticks() devuelve los milisegundos que pasaron desde
        # pygame.init(). Restando dos lecturas se sabe cuánto tiempo pasó.
        self.inicio = pygame.time.get_ticks()
        self.tiempo_final = 0
        self.tapar_en = 0
        self.estado = Estado.ELIGIENDO

    def manejar_eventos(self):
        """Atiende los clics sobre las cartas y el reinicio."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.ejecutando = False
                elif evento.key == pygame.K_SPACE:
                    if self.estado == Estado.VICTORIA:
                        self.reiniciar()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # button dice qué botón se pulsó: 1 es el izquierdo
                if evento.button == 1 and self.estado == Estado.ELIGIENDO:
                    self.voltear_en(evento.pos)

    def voltear_en(self, posicion: tuple):
        """Descubre la carta que está bajo el mouse, si se puede."""
        for carta in self.cartas:
            # collidepoint() dice si un punto está dentro del rectángulo
            if carta.rect.collidepoint(posicion) and not carta.descubierta:
                carta.descubierta = True
                self.elegidas.append(carta)
                if len(self.elegidas) == 2:
                    self.comparar()
                return

    def comparar(self):
        """Revisa la pareja elegida o programa cuándo taparla."""
        self.movimientos = self.movimientos + 1
        primera, segunda = self.elegidas
        if primera.es_pareja_de(segunda):
            primera.encontrada = True
            segunda.encontrada = True
            self.elegidas = []
            self.parejas = self.parejas + 1
            if self.parejas == len(FIGURAS):
                self.tiempo_final = self.segundos_jugados()
                self.estado = Estado.VICTORIA
        else:
            # En lugar de detener el programa con sleep, se anota en qué
            # momento hay que tapar las cartas. El ciclo de juego sigue
            # dibujando y, cuando llega ese momento, actualizar() las tapa.
            self.tapar_en = pygame.time.get_ticks() + ESPERA_MILISEGUNDOS
            self.estado = Estado.ESPERANDO

    def actualizar(self):
        """Tapa la pareja equivocada cuando se cumple la espera."""
        if self.estado != Estado.ESPERANDO:
            return
        if pygame.time.get_ticks() >= self.tapar_en:
            for carta in self.elegidas:
                carta.descubierta = False
            self.elegidas = []
            self.estado = Estado.ELIGIENDO

    def segundos_jugados(self) -> int:
        """Devuelve los segundos desde el inicio de la partida."""
        if self.estado == Estado.VICTORIA:
            return self.tiempo_final
        return (pygame.time.get_ticks() - self.inicio) // 1000

    def escribir(self, texto: str, fuente: pygame.font.Font, centro: tuple):
        """Dibuja un texto blanco centrado."""
        superficie = fuente.render(texto, True, BLANCO)
        self.pantalla.blit(superficie, superficie.get_rect(center=centro))

    def dibujar(self):
        """Dibuja la barra de información y las cartas."""
        self.pantalla.fill(FONDO)
        segundos = self.segundos_jugados()
        # :02d escribe el número con dos dígitos, con un 0 a la izquierda
        # si hace falta: 7 se ve como 07
        reloj = f"{segundos // 60}:{segundos % 60:02d}"
        self.escribir(f"Movimientos: {self.movimientos}", self.fuente,
                      (ANCHO // 4 + 10, ALTO_BARRA // 2))
        self.escribir(f"Tiempo: {reloj}", self.fuente,
                      (ANCHO * 3 // 4, ALTO_BARRA // 2))
        for carta in self.cartas:
            carta.dibujar(self.pantalla)

        if self.estado == Estado.VICTORIA:
            capa = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            capa.fill(OSCURECER)
            self.pantalla.blit(capa, (0, 0))
            self.escribir("Ganaste", self.fuente_grande,
                          (ANCHO // 2, ALTO // 2 - 50))
            resumen = f"{self.movimientos} movimientos en {reloj}"
            self.escribir(resumen, self.fuente, (ANCHO // 2, ALTO // 2 + 10))
            self.escribir("Espacio para jugar otra vez", self.fuente,
                          (ANCHO // 2, ALTO // 2 + 55))
        pygame.display.flip()

    def ejecutar(self):
        """Ciclo de juego: eventos, actualizar y dibujar."""
        while self.ejecutando:
            self.reloj.tick(FPS)
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
        pygame.quit()


def main():
    """Crea el juego y lo ejecuta."""
    Juego().ejecutar()


if __name__ == "__main__":
    main()
