"""Proyecto 081: Ventana y dibujo con pygame.

Abre una ventana con pygame y dibuja un paisaje con rectángulos, círculos y
líneas. Una nube cruza el cielo para mostrar que la imagen se redibuja en
cada cuadro.
"""

# pygame es una biblioteca externa para hacer juegos: abre ventanas,
# dibuja figuras, lee el teclado y el mouse y controla el tiempo
import pygame

ANCHO = 800
ALTO = 600
FPS = 60
VELOCIDAD_NUBE = 2

# Cada color es una tupla (rojo, verde, azul) con valores de 0 a 255
CIELO = (135, 206, 235)
PASTO = (76, 175, 80)
SOL = (255, 214, 0)
PARED = (230, 180, 120)
TECHO = (178, 34, 34)
PUERTA = (120, 72, 40)
VENTANA = (200, 235, 255)
TRONCO = (110, 70, 40)
COPA = (34, 139, 34)
NUBE = (255, 255, 255)
NEGRO = (0, 0, 0)


class Paisaje:
    """Dibuja el paisaje y mueve la nube."""

    def __init__(self):
        self.nube_x = -150

    def actualizar(self):
        """Mueve la nube a la derecha y la regresa al salir de la ventana."""
        # La nube avanza una cantidad fija de píxeles en cada cuadro. Si el
        # juego corre a menos cuadros por segundo, la nube va más lenta;
        # en el proyecto 082 eso se corrige con el delta time.
        self.nube_x = self.nube_x + VELOCIDAD_NUBE
        if self.nube_x > ANCHO + 150:
            self.nube_x = -150

    def dibujar(self, pantalla: pygame.Surface):
        """Dibuja todas las figuras en la superficie recibida."""
        # fill() pinta toda la superficie de un color: borra el cuadro
        # anterior antes de dibujar el nuevo
        pantalla.fill(CIELO)

        # Las coordenadas empiezan en la esquina superior izquierda: x
        # crece hacia la derecha y y crece hacia abajo.
        # draw.rect(superficie, color, (x, y, ancho, alto)) dibuja un
        # rectángulo relleno
        pygame.draw.rect(pantalla, PASTO, (0, 450, ANCHO, 150))

        # draw.circle(superficie, color, (x, y) del centro, radio)
        pygame.draw.circle(pantalla, SOL, (680, 110), 50)
        # draw.line(superficie, color, inicio, fin, grosor) dibuja una
        # línea. Los rayos del sol son ocho líneas que salen del centro.
        rayos = [
            ((680, 30), (680, 0)), ((680, 190), (680, 220)),
            ((600, 110), (570, 110)), ((760, 110), (790, 110)),
            ((625, 55), (605, 35)), ((735, 55), (755, 35)),
            ((625, 165), (605, 185)), ((735, 165), (755, 185)),
        ]
        for inicio, fin in rayos:
            pygame.draw.line(pantalla, SOL, inicio, fin, 4)

        self.dibujar_casa(pantalla)
        self.dibujar_arbol(pantalla)
        self.dibujar_nube(pantalla)

    def dibujar_casa(self, pantalla: pygame.Surface):
        """Dibuja la casa con pared, techo, puerta y ventana."""
        pygame.draw.rect(pantalla, PARED, (150, 300, 250, 170))
        # draw.polygon() une una lista de puntos y rellena la figura; con
        # tres puntos forma el triángulo del techo
        techo = [(130, 300), (275, 190), (420, 300)]
        pygame.draw.polygon(pantalla, TECHO, techo)
        pygame.draw.rect(pantalla, PUERTA, (245, 370, 60, 100))
        pygame.draw.rect(pantalla, VENTANA, (175, 330, 50, 50))
        # Con un grosor al final, draw.rect() dibuja solo el borde
        pygame.draw.rect(pantalla, NEGRO, (175, 330, 50, 50), 3)
        pygame.draw.line(pantalla, NEGRO, (200, 330), (200, 380), 3)
        pygame.draw.line(pantalla, NEGRO, (175, 355), (225, 355), 3)

    def dibujar_arbol(self, pantalla: pygame.Surface):
        """Dibuja un árbol con tronco y tres círculos de copa."""
        pygame.draw.rect(pantalla, TRONCO, (540, 330, 30, 130))
        pygame.draw.circle(pantalla, COPA, (555, 300), 60)
        pygame.draw.circle(pantalla, COPA, (510, 340), 40)
        pygame.draw.circle(pantalla, COPA, (600, 340), 40)

    def dibujar_nube(self, pantalla: pygame.Surface):
        """Dibuja la nube con tres círculos en su posición actual."""
        x = self.nube_x
        pygame.draw.circle(pantalla, NUBE, (x, 100), 35)
        pygame.draw.circle(pantalla, NUBE, (x + 40, 85), 45)
        pygame.draw.circle(pantalla, NUBE, (x + 85, 100), 35)


class Juego:
    """Abre la ventana y ejecuta el ciclo de juego."""

    def __init__(self):
        # init() prepara todos los módulos de pygame antes de usarlos
        pygame.init()
        # set_mode() abre la ventana con el tamaño (ancho, alto) y
        # devuelve la superficie donde se dibuja
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Ventana y dibujo con pygame")
        # Clock lleva la cuenta del tiempo entre cuadros
        self.reloj = pygame.time.Clock()
        self.paisaje = Paisaje()
        self.ejecutando = True

    def manejar_eventos(self):
        """Revisa lo que hizo el usuario desde el cuadro anterior."""
        # event.get() devuelve la lista de eventos pendientes: teclas,
        # clics, cerrar la ventana. Si no se leen, la ventana se congela.
        for evento in pygame.event.get():
            # pygame.QUIT es el evento de cerrar la ventana con la X
            if evento.type == pygame.QUIT:
                self.ejecutando = False

    def actualizar(self):
        """Cambia el estado del juego para el siguiente cuadro."""
        self.paisaje.actualizar()

    def dibujar(self):
        """Dibuja el cuadro y lo muestra en la ventana."""
        self.paisaje.dibujar(self.pantalla)
        # Todo se dibuja primero en memoria; flip() muestra el cuadro
        # terminado de una vez, así no se ven figuras a medio dibujar
        pygame.display.flip()

    def ejecutar(self):
        """Repite el ciclo de juego hasta que se cierra la ventana."""
        # El ciclo de juego es el corazón de cualquier juego: se repite
        # muchas veces por segundo y en cada vuelta lee los eventos,
        # actualiza lo que se mueve y dibuja un cuadro nuevo. Cada vuelta
        # produce un cuadro (frame) de la animación.
        while self.ejecutando:
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            # tick(FPS) espera lo necesario para no pasar de FPS cuadros
            # por segundo. Sin límite, el ciclo correría tan rápido como
            # pueda la computadora: usaría todo el procesador y la nube
            # iría a una velocidad distinta en cada equipo.
            self.reloj.tick(FPS)
        # quit() cierra pygame y libera la ventana
        pygame.quit()


def main():
    """Crea el juego y lo ejecuta."""
    Juego().ejecutar()


if __name__ == "__main__":
    main()
