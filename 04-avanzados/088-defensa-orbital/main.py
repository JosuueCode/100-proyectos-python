"""Proyecto 088: Defensa orbital.

Una torreta protege su planeta de oleadas de drones que bajan en
formación. Cada oleada llega con otra figura y es más rápida.
"""

import random
from enum import Enum

import pygame

ANCHO = 800
ALTO = 640
FPS = 60
ALTURA_PLANETA = 80
VELOCIDAD_TORRETA = 380
ESPERA_ENTRE_DISPAROS = 0.35
VELOCIDAD_DISPARO = 600
VELOCIDAD_DISPARO_DRON = 260
VELOCIDAD_FORMACION = 50
AUMENTO_POR_OLEADA = 15
BAJADA_FORMACION = 22
PROBABILIDAD_DISPARO = 0.5
TAMANO_DRON = 34
SEPARACION_DRON = 50
VIDAS_INICIALES = 3
TIEMPO_INVULNERABLE = 1.5
PAUSA_ENTRE_OLEADAS = 2.0
FONDO = (8, 10, 28)
ESTRELLA = (90, 100, 140)
PLANETA = (38, 110, 90)
PLANETA_BORDE = (60, 160, 120)
TORRETA = (176, 190, 197)
CANON = (255, 213, 79)
DISPARO = (255, 241, 118)
DISPARO_DRON = (255, 82, 82)
BLANCO = (240, 240, 240)
OSCURECER = (0, 0, 0, 150)
# Color y puntos de los drones según su fila, de arriba hacia abajo
TIPOS_DRON = [((186, 104, 200), 30), ((79, 195, 247), 20),
              ((129, 199, 132), 10)]
# Cada figura es una lista de filas; una X marca dónde va un dron
FORMACIONES = [
    ["XXXXXXXXX", "XXXXXXXXX", "XXXXXXXXX", "XXXXXXXXX"],
    ["X.......X", ".X.....X.", "..X...X..", "...XXX...", "....X...."],
    ["....X....", "...XXX...", "..XXXXX..", ".XXXXXXX.", "..XXXXX..",
     "...XXX...", "....X...."],
]


class Estado(Enum):
    """Estados del juego."""

    ANUNCIO = "anuncio"
    JUGANDO = "jugando"
    FIN = "fin"


class Disparo(pygame.sprite.Sprite):
    """Proyectil vertical, del jugador o de un dron."""

    def __init__(self, x: int, y: int, velocidad: float, color: tuple):
        super().__init__()
        self.image = pygame.Surface((4, 14))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.y = float(y)
        self.velocidad = velocidad

    def update(self, dt: float):
        """Avanza y se elimina al salir de la pantalla."""
        self.y = self.y + self.velocidad * dt
        self.rect.centery = round(self.y)
        if self.rect.bottom < 0 or self.rect.top > ALTO:
            self.kill()


class Torreta(pygame.sprite.Sprite):
    """Torreta del jugador que se mueve a los lados y dispara."""

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((56, 36), pygame.SRCALPHA)
        pygame.draw.rect(self.image, CANON, (24, 0, 8, 18))
        # draw.ellipse() dibuja un óvalo que llena el rectángulo indicado
        pygame.draw.ellipse(self.image, TORRETA, (0, 12, 56, 24))
        self.rect = self.image.get_rect(
            midbottom=(ANCHO // 2, ALTO - ALTURA_PLANETA + 4),
        )
        self.x = float(self.rect.centerx)
        self.espera = 0.0
        self.invulnerable = 0.0

    def update(self, dt: float):
        """Mueve la torreta y descuenta los tiempos de espera."""
        teclas = pygame.key.get_pressed()
        direccion = 0
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            direccion = direccion - 1
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            direccion = direccion + 1
        self.x = self.x + direccion * VELOCIDAD_TORRETA * dt
        mitad = self.rect.width / 2
        self.x = max(mitad, min(self.x, ANCHO - mitad))
        self.rect.centerx = round(self.x)
        self.espera = max(0, self.espera - dt)
        self.invulnerable = max(0, self.invulnerable - dt)

    def puede_disparar(self) -> bool:
        """Devuelve True si ya pasó el tiempo de espera."""
        return self.espera == 0

    def disparar(self) -> Disparo:
        """Crea un disparo y reinicia el tiempo de espera."""
        # El tiempo de espera (cooldown) evita que al mantener Espacio
        # salga un disparo en cada cuadro, 60 por segundo
        self.espera = ESPERA_ENTRE_DISPAROS
        return Disparo(self.rect.centerx, self.rect.top, -VELOCIDAD_DISPARO,
                       DISPARO)

    def visible(self) -> bool:
        """Parpadea mientras es invulnerable."""
        if self.invulnerable == 0:
            return True
        return int(self.invulnerable * 10) % 2 == 0


class Dron(pygame.sprite.Sprite):
    """Dron enemigo con forma de rombo."""

    def __init__(self, x: float, y: float, color: tuple, puntos: int):
        super().__init__()
        self.image = pygame.Surface((TAMANO_DRON, TAMANO_DRON),
                                    pygame.SRCALPHA)
        mitad = TAMANO_DRON // 2
        rombo = [(mitad, 0), (TAMANO_DRON, mitad), (mitad, TAMANO_DRON),
                 (0, mitad)]
        pygame.draw.polygon(self.image, color, rombo)
        pygame.draw.circle(self.image, FONDO, (mitad, mitad), 6)
        self.rect = self.image.get_rect(center=(round(x), round(y)))
        self.posicion = pygame.Vector2(x, y)
        self.puntos = puntos

    def mover(self, dx: float, dy: float):
        """Desplaza el dron y acomoda su rect."""
        self.posicion = self.posicion + pygame.Vector2(dx, dy)
        self.rect.center = (round(self.posicion.x), round(self.posicion.y))


class Juego:
    """Partida con oleadas, vidas y puntaje."""

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Defensa orbital")
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 34)
        self.fuente_grande = pygame.font.Font(None, 76)
        self.ejecutando = True
        self.estrellas = []
        for _ in range(90):
            x = random.randint(0, ANCHO)
            y = random.randint(0, ALTO - ALTURA_PLANETA)
            self.estrellas.append((x, y))
        self.reiniciar_partida()

    def reiniciar_partida(self):
        """Empieza en la oleada 1 con todas las vidas."""
        self.torreta = Torreta()
        # GroupSingle es un grupo que guarda un solo sprite
        self.grupo_torreta = pygame.sprite.GroupSingle(self.torreta)
        self.drones = pygame.sprite.Group()
        self.disparos = pygame.sprite.Group()
        self.disparos_drones = pygame.sprite.Group()
        self.vidas = VIDAS_INICIALES
        self.puntos = 0
        self.oleada = 0
        self.siguiente_oleada()

    def siguiente_oleada(self):
        """Arma la formación de la oleada siguiente y la anuncia."""
        self.oleada = self.oleada + 1
        self.drones.empty()
        self.disparos.empty()
        self.disparos_drones.empty()
        # Las figuras se repiten en orden: oleada 1, 2, 3, 1, 2, 3...
        figura = FORMACIONES[(self.oleada - 1) % len(FORMACIONES)]
        ancho_figura = (len(figura[0]) - 1) * SEPARACION_DRON
        inicio_x = (ANCHO - ancho_figura) / 2
        for numero_fila, fila in enumerate(figura):
            tipo = min(numero_fila * len(TIPOS_DRON) // len(figura),
                       len(TIPOS_DRON) - 1)
            color, puntos = TIPOS_DRON[tipo]
            for numero_columna, marca in enumerate(fila):
                if marca == "X":
                    x = inicio_x + numero_columna * SEPARACION_DRON
                    y = 80 + numero_fila * SEPARACION_DRON * 0.8
                    self.drones.add(Dron(x, y, color, puntos))
        self.direccion = 1
        aumento = (self.oleada - 1) * AUMENTO_POR_OLEADA
        self.velocidad_formacion = VELOCIDAD_FORMACION + aumento
        self.tiempo_anuncio = PAUSA_ENTRE_OLEADAS
        self.estado = Estado.ANUNCIO

    def manejar_eventos(self):
        """Atiende el cierre y el reinicio."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.ejecutando = False
                elif evento.key == pygame.K_SPACE:
                    if self.estado == Estado.FIN:
                        self.reiniciar_partida()

    def actualizar(self, dt: float):
        """Avanza el anuncio o la partida según el estado."""
        if self.estado == Estado.ANUNCIO:
            self.torreta.update(dt)
            self.tiempo_anuncio = self.tiempo_anuncio - dt
            if self.tiempo_anuncio <= 0:
                self.estado = Estado.JUGANDO
            return
        if self.estado != Estado.JUGANDO:
            return

        self.grupo_torreta.update(dt)
        # Disparar se revisa con get_pressed() para poder mantener Espacio;
        # el tiempo de espera decide cada cuánto sale un disparo
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE] and self.torreta.puede_disparar():
            self.disparos.add(self.torreta.disparar())

        self.mover_formacion(dt)
        self.disparar_drones(dt)
        self.disparos.update(dt)
        self.disparos_drones.update(dt)
        self.revisar_choques()

    def mover_formacion(self, dt: float):
        """Mueve la formación a un lado y la baja al llegar al borde."""
        dx = self.direccion * self.velocidad_formacion * dt
        for dron in self.drones:
            dron.mover(dx, 0)
        toca_borde = False
        for dron in self.drones:
            if dron.rect.right >= ANCHO - 10 or dron.rect.left <= 10:
                toca_borde = True
        # Al tocar un borde, toda la formación cambia de sentido y baja un
        # escalón: así avanza poco a poco hacia el planeta
        if toca_borde:
            self.direccion = -self.direccion
            for dron in self.drones:
                dron.mover(-dx, BAJADA_FORMACION)

    def disparar_drones(self, dt: float):
        """De vez en cuando, un dron al azar dispara hacia abajo."""
        # La probabilidad está dada por segundo: multiplicarla por dt la
        # reparte entre los cuadros. random.random() da un número entre 0
        # y 1, así que es menor que la probabilidad esa fracción de veces.
        probabilidad = (PROBABILIDAD_DISPARO + self.oleada * 0.1) * dt
        if len(self.drones) > 0 and random.random() < probabilidad:
            # sprites() devuelve la lista de sprites del grupo
            dron = random.choice(self.drones.sprites())
            disparo = Disparo(dron.rect.centerx, dron.rect.bottom,
                              VELOCIDAD_DISPARO_DRON, DISPARO_DRON)
            self.disparos_drones.add(disparo)

    def revisar_choques(self):
        """Revisa disparos contra drones y contra la torreta."""
        # groupcollide() compara dos grupos y devuelve un diccionario: cada
        # disparo que chocó es una llave y su valor es la lista de drones
        # que tocó. Los dos True borran de sus grupos lo que chocó.
        choques = pygame.sprite.groupcollide(self.disparos, self.drones,
                                             True, True)
        for drones_tocados in choques.values():
            for dron in drones_tocados:
                self.puntos = self.puntos + dron.puntos

        # Aquí el tercer valor es True para borrar el disparo enemigo, y el
        # cuarto es False para que la torreta no desaparezca del grupo
        golpes = pygame.sprite.groupcollide(self.disparos_drones,
                                            self.grupo_torreta, True, False)
        if len(golpes) > 0 and self.torreta.invulnerable == 0:
            self.perder_vida()

        for dron in self.drones:
            if dron.rect.bottom >= ALTO - ALTURA_PLANETA:
                self.vidas = 0
                self.estado = Estado.FIN
                return

        if len(self.drones) == 0:
            self.siguiente_oleada()

    def perder_vida(self):
        """Resta una vida y da un momento de invulnerabilidad."""
        self.vidas = self.vidas - 1
        self.torreta.invulnerable = TIEMPO_INVULNERABLE
        if self.vidas == 0:
            self.estado = Estado.FIN

    def escribir(self, texto: str, fuente: pygame.font.Font, centro: tuple):
        """Dibuja un texto blanco centrado."""
        superficie = fuente.render(texto, True, BLANCO)
        self.pantalla.blit(superficie, superficie.get_rect(center=centro))

    def dibujar(self):
        """Dibuja estrellas, planeta, sprites y la información."""
        self.pantalla.fill(FONDO)
        for estrella in self.estrellas:
            pygame.draw.circle(self.pantalla, ESTRELLA, estrella, 1)
        # El planeta es un círculo enorme del que solo se ve la parte de
        # arriba, como si fuera el horizonte
        centro_planeta = (ANCHO // 2, ALTO + 900)
        radio = 900 + ALTURA_PLANETA - 20
        pygame.draw.circle(self.pantalla, PLANETA_BORDE, centro_planeta,
                           radio + 4)
        pygame.draw.circle(self.pantalla, PLANETA, centro_planeta, radio)

        self.drones.draw(self.pantalla)
        self.disparos.draw(self.pantalla)
        self.disparos_drones.draw(self.pantalla)
        if self.torreta.visible():
            self.grupo_torreta.draw(self.pantalla)

        self.escribir(f"Puntos: {self.puntos}", self.fuente, (100, 25))
        self.escribir(f"Oleada {self.oleada}", self.fuente, (ANCHO // 2, 25))
        self.escribir(f"Vidas: {self.vidas}", self.fuente, (ANCHO - 80, 25))

        if self.estado == Estado.ANUNCIO:
            self.escribir(f"Oleada {self.oleada}", self.fuente_grande,
                          (ANCHO // 2, ALTO // 2))
        elif self.estado == Estado.FIN:
            capa = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            capa.fill(OSCURECER)
            self.pantalla.blit(capa, (0, 0))
            self.escribir("El planeta cayó", self.fuente_grande,
                          (ANCHO // 2, ALTO // 2 - 30))
            self.escribir(f"Puntos: {self.puntos}", self.fuente,
                          (ANCHO // 2, ALTO // 2 + 30))
            self.escribir("Espacio para jugar otra vez", self.fuente,
                          (ANCHO // 2, ALTO // 2 + 70))
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
