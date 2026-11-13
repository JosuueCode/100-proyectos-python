"""Proyecto 087: Cohete en la cueva.

Un cohete cae por la gravedad y sube con cada impulso de su motor. Hay que
cruzar los huecos entre las rocas de la cueva sin tocar nada.
"""

import random
from enum import Enum

import pygame

ANCHO = 480
ALTO = 640
FPS = 60
GRAVEDAD = 1500
IMPULSO = -480
VELOCIDAD_MAXIMA_CAIDA = 700
VELOCIDAD_CUEVA = 180
ANCHO_ROCA = 80
SEPARACION_ROCAS = 260
HUECO_INICIAL = 200
HUECO_MINIMO = 140
REDUCCION_HUECO = 4
ALTO_TECHO = 30
MARGEN_HUECO = 70
COHETE_X = 120
FONDO = (22, 18, 30)
ROCA = (93, 64, 55)
ROCA_OSCURA = (62, 39, 35)
TECHO = (55, 40, 40)
CUERPO_COHETE = (224, 224, 224)
VENTANILLA = (79, 195, 247)
FUEGO = (255, 112, 67)
BLANCO = (240, 240, 240)
OSCURECER = (0, 0, 0, 150)


class Estado(Enum):
    """Estados del juego."""

    LISTO = "listo"
    VOLANDO = "volando"
    CHOQUE = "choque"


class Cohete:
    """Cohete que cae por la gravedad y sube con impulsos."""

    def __init__(self):
        self.y = ALTO / 2
        self.velocidad_y = 0.0
        self.tiempo_fuego = 0.0
        # La caja de choque es un poco más chica que el dibujo para que
        # rozar una roca con la punta no se sienta injusto
        self.rect = pygame.Rect(0, 0, 34, 22)
        self.rect.center = (COHETE_X, round(self.y))

    def impulsar(self):
        """Enciende el motor un instante y lanza el cohete hacia arriba."""
        # El impulso cambia la velocidad de golpe, sin importar cuál
        # tenía: así cada pulsación da el mismo salto, aunque el cohete
        # viniera cayendo rápido
        self.velocidad_y = IMPULSO
        self.tiempo_fuego = 0.12

    def actualizar(self, dt: float):
        """Aplica la gravedad y mueve el cohete."""
        # La gravedad es una aceleración: no mueve al cohete directamente,
        # sino que aumenta su velocidad hacia abajo en cada cuadro. Por
        # eso la caída empieza lenta y se vuelve cada vez más rápida.
        self.velocidad_y = self.velocidad_y + GRAVEDAD * dt
        self.velocidad_y = min(self.velocidad_y, VELOCIDAD_MAXIMA_CAIDA)
        self.y = self.y + self.velocidad_y * dt
        self.tiempo_fuego = max(0, self.tiempo_fuego - dt)
        self.rect.center = (COHETE_X, round(self.y))

    def dibujar(self, pantalla: pygame.Surface):
        """Dibuja el cohete inclinado según su velocidad."""
        # El cohete mira hacia arriba al subir y hacia abajo al caer.
        # rotate() gira un Vector2 los grados indicados alrededor de
        # (0, 0), así que los puntos se definen respecto al centro.
        angulo = max(-25, min(self.velocidad_y / 10, 50))
        centro = pygame.Vector2(COHETE_X, self.y)
        cuerpo = [(26, 0), (8, -11), (-20, -11), (-20, 11), (8, 11)]
        aletas = [(-12, -11), (-24, -20), (-20, -11)]
        aletas_abajo = [(-12, 11), (-24, 20), (-20, 11)]
        llama = [(-20, -7), (-38, 0), (-20, 7)]
        if self.tiempo_fuego > 0:
            self.dibujar_figura(pantalla, llama, centro, angulo, FUEGO)
        self.dibujar_figura(pantalla, aletas, centro, angulo, FUEGO)
        self.dibujar_figura(pantalla, aletas_abajo, centro, angulo, FUEGO)
        self.dibujar_figura(pantalla, cuerpo, centro, angulo, CUERPO_COHETE)
        ventanilla = centro + pygame.Vector2(4, 0).rotate(angulo)
        pygame.draw.circle(pantalla, VENTANILLA, ventanilla, 5)

    def dibujar_figura(self, pantalla: pygame.Surface, puntos: list,
                       centro: pygame.Vector2, angulo: float, color: tuple):
        """Gira los puntos, los mueve al centro y dibuja el polígono."""
        girados = []
        for punto in puntos:
            girados.append(centro + pygame.Vector2(punto).rotate(angulo))
        pygame.draw.polygon(pantalla, color, girados)


class ParDeRocas:
    """Roca del techo y roca del piso con un hueco entre ellas."""

    def __init__(self, x: float, alto_hueco: int):
        self.x = x
        minimo = ALTO_TECHO + MARGEN_HUECO
        maximo = ALTO - ALTO_TECHO - MARGEN_HUECO - alto_hueco
        self.hueco_y = random.randint(minimo, maximo)
        self.alto_hueco = alto_hueco
        self.pasada = False
        # Cada roca lleva unas manchas al azar para que no se vean iguales.
        # Se guardan como (x, y, radio) relativos a la esquina de la roca.
        self.manchas = []
        for roca in self.rects():
            lista = []
            for _ in range(4):
                x = random.randint(15, ANCHO_ROCA - 15)
                y = random.randint(10, max(11, roca.height - 30))
                lista.append((x, y, random.randint(5, 11)))
            self.manchas.append(lista)

    def actualizar(self, dt: float):
        """Avanza hacia la izquierda con la cueva."""
        self.x = self.x - VELOCIDAD_CUEVA * dt

    def rects(self) -> list[pygame.Rect]:
        """Devuelve el rectángulo de arriba y el de abajo."""
        arriba = pygame.Rect(round(self.x), 0, ANCHO_ROCA, self.hueco_y)
        inicio_abajo = self.hueco_y + self.alto_hueco
        abajo = pygame.Rect(round(self.x), inicio_abajo, ANCHO_ROCA,
                            ALTO - inicio_abajo)
        return [arriba, abajo]

    def choca_con(self, rect: pygame.Rect) -> bool:
        """Devuelve True si el rect toca alguna de las dos rocas."""
        for roca in self.rects():
            if roca.colliderect(rect):
                return True
        return False

    def dibujar(self, pantalla: pygame.Surface):
        """Dibuja las dos rocas con su borde y sus manchas."""
        arriba, abajo = self.rects()
        for indice, roca in enumerate([arriba, abajo]):
            pygame.draw.rect(pantalla, ROCA_OSCURA, roca, border_radius=10)
            pygame.draw.rect(pantalla, ROCA, roca.inflate(-12, -12),
                             border_radius=8)
            for x, y, radio in self.manchas[indice]:
                centro = (roca.left + x, roca.top + y)
                pygame.draw.circle(pantalla, ROCA_OSCURA, centro, radio)


class Juego:
    """Partida del cohete en la cueva."""

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Cohete en la cueva")
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 34)
        self.fuente_grande = pygame.font.Font(None, 80)
        self.ejecutando = True
        self.mejor = 0
        self.reiniciar()

    def reiniciar(self):
        """Prepara una partida nueva, con el cohete esperando."""
        self.cohete = Cohete()
        self.rocas = [ParDeRocas(ANCHO + 60, HUECO_INICIAL)]
        self.puntos = 0
        self.estado = Estado.LISTO

    def alto_hueco_actual(self) -> int:
        """El hueco se cierra un poco con cada punto, hasta un mínimo."""
        alto = HUECO_INICIAL - self.puntos * REDUCCION_HUECO
        return max(HUECO_MINIMO, alto)

    def manejar_eventos(self):
        """Espacio impulsa el cohete o reinicia tras un choque."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.ejecutando = False
                elif evento.key in (pygame.K_SPACE, pygame.K_UP):
                    self.pulsar()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                self.pulsar()

    def pulsar(self):
        """Responde a la tecla de acción según el estado."""
        if self.estado == Estado.CHOQUE:
            self.reiniciar()
        else:
            self.estado = Estado.VOLANDO
            self.cohete.impulsar()

    def actualizar(self, dt: float):
        """Mueve cohete y rocas, cuenta puntos y revisa choques."""
        if self.estado != Estado.VOLANDO:
            return
        self.cohete.actualizar(dt)
        for par in self.rocas:
            par.actualizar(dt)

        # Las rocas que ya salieron por la izquierda se quitan, y cuando
        # la última avanzó lo suficiente se crea otra a la derecha
        if self.rocas[0].x < -ANCHO_ROCA:
            self.rocas.pop(0)
        if self.rocas[-1].x < ANCHO - SEPARACION_ROCAS:
            nueva_x = self.rocas[-1].x + SEPARACION_ROCAS
            self.rocas.append(ParDeRocas(nueva_x, self.alto_hueco_actual()))

        for par in self.rocas:
            # Se gana el punto cuando la roca queda atrás del cohete
            if not par.pasada and par.x + ANCHO_ROCA < COHETE_X:
                par.pasada = True
                self.puntos = self.puntos + 1
            if par.choca_con(self.cohete.rect):
                self.chocar()

        rect = self.cohete.rect
        if rect.top < ALTO_TECHO or rect.bottom > ALTO - ALTO_TECHO:
            self.chocar()

    def chocar(self):
        """Termina la partida y guarda el mejor puntaje de la sesión."""
        self.estado = Estado.CHOQUE
        self.mejor = max(self.mejor, self.puntos)

    def dibujar_techo_y_piso(self):
        """Dibuja el techo y el piso de la cueva con picos que avanzan."""
        pygame.draw.rect(self.pantalla, TECHO, (0, 0, ANCHO, ALTO_TECHO))
        pygame.draw.rect(self.pantalla, TECHO,
                         (0, ALTO - ALTO_TECHO, ANCHO, ALTO_TECHO))
        # El desplazamiento usa la posición de la primera roca para que
        # los picos avancen al mismo paso que la cueva
        desplazamiento = round(self.rocas[0].x) % 40
        for x in range(desplazamiento - 40, ANCHO + 40, 40):
            techo = [(x, 0), (x + 40, 0), (x + 20, ALTO_TECHO)]
            piso = [(x, ALTO), (x + 40, ALTO), (x + 20, ALTO - ALTO_TECHO)]
            pygame.draw.polygon(self.pantalla, ROCA, techo)
            pygame.draw.polygon(self.pantalla, ROCA, piso)

    def escribir(self, texto: str, fuente: pygame.font.Font, centro: tuple):
        """Dibuja un texto blanco centrado."""
        superficie = fuente.render(texto, True, BLANCO)
        self.pantalla.blit(superficie, superficie.get_rect(center=centro))

    def dibujar(self):
        """Dibuja la cueva, las rocas, el cohete y los textos."""
        self.pantalla.fill(FONDO)
        for par in self.rocas:
            par.dibujar(self.pantalla)
        self.dibujar_techo_y_piso()
        self.cohete.dibujar(self.pantalla)
        self.escribir(str(self.puntos), self.fuente_grande, (ANCHO // 2, 90))

        if self.estado == Estado.LISTO:
            self.escribir("Espacio o clic para encender", self.fuente,
                          (ANCHO // 2, ALTO - 110))
        elif self.estado == Estado.CHOQUE:
            capa = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            capa.fill(OSCURECER)
            self.pantalla.blit(capa, (0, 0))
            self.escribir("Choque", self.fuente_grande,
                          (ANCHO // 2, ALTO // 2 - 40))
            self.escribir(f"Puntos: {self.puntos}   Mejor: {self.mejor}",
                          self.fuente, (ANCHO // 2, ALTO // 2 + 20))
            self.escribir("Espacio para volver a intentar", self.fuente,
                          (ANCHO // 2, ALTO // 2 + 60))
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
