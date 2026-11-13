"""Proyecto 086: Breakout.

Rompe todos los ladrillos con la pelota sin dejarla caer. Tienes tres
vidas y cada nivel trae más filas de ladrillos y una pelota más rápida.
"""

import math
from enum import Enum

import pygame

ANCHO = 800
ALTO = 600
FPS = 60
ANCHO_PALETA = 110
ALTO_PALETA = 16
VELOCIDAD_PALETA = 520
TAMANO_PELOTA = 14
VELOCIDAD_PELOTA = 380
AUMENTO_POR_NIVEL = 70
ANGULO_MAXIMO = 60
COLUMNAS_LADRILLOS = 10
FILAS_INICIALES = 4
ANCHO_LADRILLO = 72
ALTO_LADRILLO = 24
SEPARACION = 6
MARGEN_SUPERIOR = 70
VIDAS_INICIALES = 3
NIVEL_FINAL = 3
FONDO = (20, 20, 35)
BLANCO = (235, 235, 235)
COLOR_PALETA = (144, 202, 249)
# Cada fila tiene su color y los puntos que da cada ladrillo
COLORES_FILAS = [
    ((239, 83, 80), 7), ((255, 152, 0), 6), ((255, 235, 59), 5),
    ((102, 187, 106), 4), ((66, 165, 245), 3), ((171, 71, 188), 2),
    ((236, 64, 122), 1),
]


class Estado(Enum):
    """Estados del juego."""

    ESPERANDO = "esperando"
    JUGANDO = "jugando"
    PERDISTE = "perdiste"
    GANASTE = "ganaste"


class Paleta(pygame.sprite.Sprite):
    """Paleta que se mueve a los lados con el teclado."""

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ANCHO_PALETA, ALTO_PALETA),
                                    pygame.SRCALPHA)
        pygame.draw.rect(self.image, COLOR_PALETA, self.image.get_rect(),
                         border_radius=8)
        self.rect = self.image.get_rect(midbottom=(ANCHO // 2, ALTO - 30))
        self.x = float(self.rect.centerx)

    # update() es el nombre que usa pygame para actualizar un sprite: al
    # llamar a grupo.update(dt), el grupo llama a update(dt) de cada uno
    def update(self, dt: float):
        """Mueve la paleta con las flechas o con A y D."""
        teclas = pygame.key.get_pressed()
        direccion = 0
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            direccion = direccion - 1
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            direccion = direccion + 1
        self.x = self.x + direccion * VELOCIDAD_PALETA * dt
        mitad = ANCHO_PALETA / 2
        self.x = max(mitad, min(self.x, ANCHO - mitad))
        self.rect.centerx = round(self.x)


class Pelota(pygame.sprite.Sprite):
    """Pelota que rebota en paredes, paleta y ladrillos."""

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((TAMANO_PELOTA, TAMANO_PELOTA),
                                    pygame.SRCALPHA)
        mitad = TAMANO_PELOTA // 2
        pygame.draw.circle(self.image, BLANCO, (mitad, mitad), mitad)
        self.rect = self.image.get_rect()
        self.posicion = pygame.Vector2(0, 0)
        self.velocidad = pygame.Vector2(0, 0)
        self.rapidez = VELOCIDAD_PELOTA

    def colocar_sobre(self, paleta: Paleta):
        """Deja la pelota quieta encima de la paleta."""
        self.posicion = pygame.Vector2(paleta.rect.centerx,
                                       paleta.rect.top - TAMANO_PELOTA)
        self.velocidad = pygame.Vector2(0, 0)
        self.sincronizar()

    def lanzar(self):
        """Lanza la pelota hacia arriba con una pequeña inclinación."""
        self.velocidad = pygame.Vector2(0.4, -1).normalize() * self.rapidez

    def sincronizar(self):
        """Pone el rect en la posición exacta redondeada."""
        self.rect.center = (round(self.posicion.x), round(self.posicion.y))

    def update(self, dt: float):
        """Mueve la pelota y la hace rebotar en las paredes."""
        self.posicion = self.posicion + self.velocidad * dt
        mitad = TAMANO_PELOTA / 2
        if self.posicion.x < mitad:
            self.posicion.x = mitad
            self.velocidad.x = abs(self.velocidad.x)
        elif self.posicion.x > ANCHO - mitad:
            self.posicion.x = ANCHO - mitad
            self.velocidad.x = -abs(self.velocidad.x)
        if self.posicion.y < mitad:
            self.posicion.y = mitad
            self.velocidad.y = abs(self.velocidad.y)
        self.sincronizar()

    def rebotar_en_paleta(self, paleta: Paleta):
        """Sale hacia arriba con un ángulo según dónde tocó la paleta."""
        distancia = (self.posicion.x - paleta.rect.centerx)
        distancia = distancia / (ANCHO_PALETA / 2)
        distancia = max(-1, min(distancia, 1))
        angulo = math.radians(distancia * ANGULO_MAXIMO)
        # Aquí el seno da la parte horizontal porque el ángulo se mide
        # desde la vertical: un golpe en el centro sale derecho hacia arriba
        self.velocidad = pygame.Vector2(
            self.rapidez * math.sin(angulo),
            -self.rapidez * math.cos(angulo),
        )
        self.posicion.y = paleta.rect.top - TAMANO_PELOTA / 2
        self.sincronizar()

    def rebotar_en_ladrillo(self, ladrillo: pygame.sprite.Sprite):
        """Rebota según el lado del ladrillo que golpeó."""
        # Se mide cuánto se enciman la pelota y el ladrillo en cada eje.
        # Si se enciman poco a lo ancho, la pelota entró por un costado y
        # se invierte la velocidad horizontal; si se enciman poco a lo
        # alto, entró por arriba o por abajo y se invierte la vertical.
        encima_x = min(self.rect.right - ladrillo.rect.left,
                       ladrillo.rect.right - self.rect.left)
        encima_y = min(self.rect.bottom - ladrillo.rect.top,
                       ladrillo.rect.bottom - self.rect.top)
        if encima_x < encima_y:
            if self.rect.centerx < ladrillo.rect.centerx:
                self.velocidad.x = -abs(self.velocidad.x)
            else:
                self.velocidad.x = abs(self.velocidad.x)
        else:
            if self.rect.centery < ladrillo.rect.centery:
                self.velocidad.y = -abs(self.velocidad.y)
            else:
                self.velocidad.y = abs(self.velocidad.y)


class Ladrillo(pygame.sprite.Sprite):
    """Ladrillo que desaparece al recibir un golpe."""

    def __init__(self, x: int, y: int, color: tuple, puntos: int):
        super().__init__()
        self.image = pygame.Surface((ANCHO_LADRILLO, ALTO_LADRILLO))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.puntos = puntos


class Juego:
    """Partida con niveles, vidas y puntaje."""

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Breakout")
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 34)
        self.fuente_grande = pygame.font.Font(None, 72)
        self.ejecutando = True
        self.paleta = Paleta()
        self.pelota = Pelota()
        # Un grupo de sprites es una colección que actualiza, dibuja y
        # revisa choques de todos sus sprites a la vez. kill() saca un
        # sprite de todos los grupos donde esté.
        self.ladrillos = pygame.sprite.Group()
        self.moviles = pygame.sprite.Group(self.paleta, self.pelota)
        self.reiniciar_partida()

    def reiniciar_partida(self):
        """Empieza desde el nivel 1 con todas las vidas."""
        self.vidas = VIDAS_INICIALES
        self.puntos = 0
        self.nivel = 1
        self.armar_nivel()

    def armar_nivel(self):
        """Crea la cuadrícula de ladrillos del nivel actual."""
        # empty() vacía el grupo antes de llenarlo otra vez
        self.ladrillos.empty()
        filas = min(FILAS_INICIALES + self.nivel - 1, len(COLORES_FILAS))
        ancho_total = COLUMNAS_LADRILLOS * (ANCHO_LADRILLO + SEPARACION)
        inicio_x = (ANCHO - ancho_total + SEPARACION) // 2
        for fila in range(filas):
            color, puntos = COLORES_FILAS[fila]
            for columna in range(COLUMNAS_LADRILLOS):
                x = inicio_x + columna * (ANCHO_LADRILLO + SEPARACION)
                y = MARGEN_SUPERIOR + fila * (ALTO_LADRILLO + SEPARACION)
                # add() mete el sprite en el grupo
                self.ladrillos.add(Ladrillo(x, y, color, puntos))
        aumento = (self.nivel - 1) * AUMENTO_POR_NIVEL
        self.pelota.rapidez = VELOCIDAD_PELOTA + aumento
        self.preparar_saque()

    def preparar_saque(self):
        """Deja la pelota sobre la paleta hasta que se pulse Espacio."""
        self.pelota.colocar_sobre(self.paleta)
        self.estado = Estado.ESPERANDO

    def manejar_eventos(self):
        """Atiende el cierre y la tecla Espacio según el estado."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.ejecutando = False
                elif evento.key == pygame.K_SPACE:
                    if self.estado == Estado.ESPERANDO:
                        self.pelota.lanzar()
                        self.estado = Estado.JUGANDO
                    elif self.estado != Estado.JUGANDO:
                        self.reiniciar_partida()

    def actualizar(self, dt: float):
        """Mueve todo y revisa choques, vidas y fin de nivel."""
        if self.estado == Estado.ESPERANDO:
            self.paleta.update(dt)
            self.pelota.colocar_sobre(self.paleta)
            return
        if self.estado != Estado.JUGANDO:
            return

        # Una sola llamada actualiza la paleta y la pelota
        self.moviles.update(dt)
        if self.pelota.rect.colliderect(self.paleta.rect):
            if self.pelota.velocidad.y > 0:
                self.pelota.rebotar_en_paleta(self.paleta)
        self.revisar_ladrillos()

        if self.pelota.rect.top > ALTO:
            self.vidas = self.vidas - 1
            if self.vidas == 0:
                self.estado = Estado.PERDISTE
            else:
                self.preparar_saque()

    def revisar_ladrillos(self):
        """Rompe el ladrillo que toque la pelota y revisa si se acabaron."""
        # spritecollide() devuelve la lista de sprites del grupo que
        # chocan con la pelota. Con False no los borra; se borran a mano.
        tocados = pygame.sprite.spritecollide(self.pelota, self.ladrillos,
                                              False)
        if len(tocados) > 0:
            # Si toca dos ladrillos a la vez, rebota solo una vez
            self.pelota.rebotar_en_ladrillo(tocados[0])
            for ladrillo in tocados:
                self.puntos = self.puntos + ladrillo.puntos
                ladrillo.kill()

        if len(self.ladrillos) == 0:
            if self.nivel == NIVEL_FINAL:
                self.estado = Estado.GANASTE
            else:
                self.nivel = self.nivel + 1
                self.armar_nivel()

    def escribir(self, texto: str, fuente: pygame.font.Font, centro: tuple):
        """Dibuja un texto blanco centrado."""
        superficie = fuente.render(texto, True, BLANCO)
        self.pantalla.blit(superficie, superficie.get_rect(center=centro))

    def dibujar(self):
        """Dibuja ladrillos, paleta, pelota y la información."""
        self.pantalla.fill(FONDO)
        # draw() copia la image de cada sprite del grupo en su rect
        self.ladrillos.draw(self.pantalla)
        self.moviles.draw(self.pantalla)

        self.escribir(f"Puntos: {self.puntos}", self.fuente, (110, 30))
        self.escribir(f"Nivel {self.nivel}", self.fuente, (ANCHO // 2, 30))
        self.escribir(f"Vidas: {self.vidas}", self.fuente, (ANCHO - 90, 30))

        centro = (ANCHO // 2, ALTO // 2 + 60)
        if self.estado == Estado.ESPERANDO:
            self.escribir("Espacio para lanzar", self.fuente, centro)
        elif self.estado == Estado.PERDISTE:
            self.escribir("Perdiste", self.fuente_grande, centro)
            self.escribir("Espacio para jugar otra vez", self.fuente,
                          (ANCHO // 2, ALTO // 2 + 120))
        elif self.estado == Estado.GANASTE:
            self.escribir("Ganaste", self.fuente_grande, centro)
            self.escribir("Espacio para jugar otra vez", self.fuente,
                          (ANCHO // 2, ALTO // 2 + 120))
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
