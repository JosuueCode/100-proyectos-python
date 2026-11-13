"""Proyecto 083: Nave con teclado.

Una nave que se mueve en ocho direcciones con las flechas o con WASD, sin
salir de la pantalla. La tecla C cambia su color.
"""

import random

import pygame

ANCHO = 800
ALTO = 600
FPS = 60
VELOCIDAD_NAVE = 300
CANTIDAD_ESTRELLAS = 120
FONDO = (10, 10, 30)
ESTRELLA = (200, 200, 220)
COLORES_NAVE = [(0, 229, 255), (255, 82, 82), (255, 235, 59), (105, 240, 174)]
LLAMA = (255, 152, 0)


# pygame.sprite.Sprite es la clase base de pygame para los objetos del
# juego que se dibujan y se mueven. Un sprite necesita dos atributos:
# image, la superficie con su dibujo, y rect, el rectángulo que indica
# dónde está y cuánto mide.
class Nave(pygame.sprite.Sprite):
    """Nave del jugador controlada con el teclado."""

    def __init__(self, x: float, y: float):
        super().__init__()
        self.indice_color = 0
        # Surface crea una superficie propia de 50 x 50 donde se dibuja la
        # nave. SRCALPHA la hace transparente, así no se ve un cuadro de
        # fondo alrededor del triángulo.
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.dibujar_imagen()
        # pygame.Rect guarda x, y, ancho y alto, y tiene atributos útiles
        # como center, left, right, top y bottom. get_rect() crea uno del
        # tamaño de la imagen, aquí con el centro en (x, y).
        self.rect = self.image.get_rect(center=(x, y))
        # El Rect solo guarda enteros; la posición exacta se lleva aparte
        # en un Vector2 para que los movimientos pequeños no se pierdan
        self.posicion = pygame.Vector2(x, y)

    def dibujar_imagen(self):
        """Dibuja el triángulo de la nave con el color actual."""
        # (0, 0, 0, 0) es un color totalmente transparente: el cuarto
        # valor es la opacidad
        self.image.fill((0, 0, 0, 0))
        color = COLORES_NAVE[self.indice_color]
        pygame.draw.polygon(self.image, color, [(25, 0), (50, 45), (0, 45)])
        pygame.draw.polygon(self.image, LLAMA, [(17, 45), (33, 45), (25, 50)])

    def cambiar_color(self):
        """Pasa al siguiente color de la lista y vuelve al primero."""
        self.indice_color = (self.indice_color + 1) % len(COLORES_NAVE)
        self.dibujar_imagen()

    def actualizar(self, dt: float, limites: pygame.Rect):
        """Lee las teclas mantenidas y mueve la nave sin salir de límites."""
        # key.get_pressed() devuelve el estado de todas las teclas en este
        # momento: teclas[pygame.K_LEFT] es True mientras se mantiene
        # presionada la flecha izquierda. Sirve para el movimiento
        # continuo, porque se revisa en cada cuadro.
        teclas = pygame.key.get_pressed()
        direccion = pygame.Vector2(0, 0)
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            direccion.x = direccion.x - 1
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            direccion.x = direccion.x + 1
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            direccion.y = direccion.y - 1
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            direccion.y = direccion.y + 1

        # En diagonal la dirección es (1, 1), que mide 1.41 y no 1: la nave
        # iría un 41 % más rápido. normalize() la ajusta para que mida 1
        # sin cambiar hacia dónde apunta. Un vector (0, 0) no se puede
        # normalizar, por eso solo se hace si hay movimiento.
        if direccion.length() > 0:
            direccion = direccion.normalize()
        self.posicion = self.posicion + direccion * VELOCIDAD_NAVE * dt

        # El centro no puede acercarse al borde más de media nave. max() y
        # min() recortan cada coordenada entre su mínimo y su máximo.
        mitad_ancho = self.rect.width / 2
        mitad_alto = self.rect.height / 2
        x_minima = limites.left + mitad_ancho
        x_maxima = limites.right - mitad_ancho
        y_minima = limites.top + mitad_alto
        y_maxima = limites.bottom - mitad_alto
        self.posicion.x = max(x_minima, min(self.posicion.x, x_maxima))
        self.posicion.y = max(y_minima, min(self.posicion.y, y_maxima))
        # El Rect se acomoda en la posición redondeada para dibujarse
        self.rect.center = (round(self.posicion.x), round(self.posicion.y))

    def dibujar(self, pantalla: pygame.Surface):
        """Copia la imagen de la nave en la pantalla."""
        # blit() copia una superficie sobre otra en la posición del rect
        pantalla.blit(self.image, self.rect)


class Juego:
    """Ventana con el fondo de estrellas y la nave."""

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Nave con teclado")
        self.reloj = pygame.time.Clock()
        self.ejecutando = True
        self.nave = Nave(ANCHO / 2, ALTO / 2)
        self.estrellas = []
        for _ in range(CANTIDAD_ESTRELLAS):
            x = random.randint(0, ANCHO)
            y = random.randint(0, ALTO)
            self.estrellas.append((x, y))

    def manejar_eventos(self):
        """Atiende el cierre de la ventana y las teclas de una sola vez."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            # KEYDOWN ocurre una sola vez cuando se pulsa una tecla, aunque
            # se mantenga presionada. Sirve para acciones puntuales, como
            # cambiar de color: con get_pressed() el color cambiaría en
            # cada cuadro mientras la tecla siga abajo.
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_c:
                    self.nave.cambiar_color()
                elif evento.key == pygame.K_ESCAPE:
                    self.ejecutando = False

    def actualizar(self, dt: float):
        """Mueve la nave dentro de los límites de la ventana."""
        self.nave.actualizar(dt, self.pantalla.get_rect())

    def dibujar(self):
        """Dibuja el fondo, las estrellas y la nave."""
        self.pantalla.fill(FONDO)
        for estrella in self.estrellas:
            pygame.draw.circle(self.pantalla, ESTRELLA, estrella, 1)
        self.nave.dibujar(self.pantalla)
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
