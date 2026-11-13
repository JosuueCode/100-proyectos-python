"""Proyecto 082: Pelota que rebota.

Varias pelotas de colores rebotan en los bordes de la ventana. Con un clic
agregas una pelota nueva donde está el mouse.
"""

import random

import pygame

ANCHO = 800
ALTO = 600
FPS = 60
PELOTAS_INICIALES = 6
RADIO_MINIMO = 12
RADIO_MAXIMO = 35
VELOCIDAD_MINIMA = 120
VELOCIDAD_MAXIMA = 360
FONDO = (25, 25, 40)
COLORES = [
    (239, 83, 80), (255, 167, 38), (255, 238, 88), (102, 187, 106),
    (66, 165, 245), (171, 71, 188), (236, 64, 122),
]


def velocidad_al_azar() -> float:
    """Devuelve una velocidad en píxeles por segundo, positiva o negativa."""
    rapidez = random.randint(VELOCIDAD_MINIMA, VELOCIDAD_MAXIMA)
    return random.choice([-1, 1]) * rapidez


class Pelota:
    """Pelota con posición, velocidad, radio y color."""

    def __init__(self, x: float, y: float):
        self.radio = random.randint(RADIO_MINIMO, RADIO_MAXIMO)
        self.color = random.choice(COLORES)
        # Vector2 guarda dos números, x y y, y permite operar con ellos
        # como un solo valor: sumarlos, restarlos o multiplicarlos por un
        # número afecta a las dos coordenadas a la vez.
        self.posicion = pygame.Vector2(x, y)
        # La velocidad está en píxeles por segundo, no por cuadro
        self.velocidad = pygame.Vector2(velocidad_al_azar(),
                                        velocidad_al_azar())

    def actualizar(self, dt: float):
        """Mueve la pelota según el tiempo que pasó y la hace rebotar."""
        # El delta time (dt) es el tiempo en segundos que pasó desde el
        # cuadro anterior. Moverse velocidad * dt hace que la pelota
        # recorra la misma distancia por segundo a 30 o a 144 FPS: si los
        # cuadros son más lentos, dt es mayor y el paso es más largo.
        self.posicion = self.posicion + self.velocidad * dt

        # Al tocar un borde se acomoda dentro de la ventana y se invierte
        # la velocidad en ese eje. abs() da el valor sin signo, así la
        # nueva dirección siempre apunta hacia adentro.
        if self.posicion.x < self.radio:
            self.posicion.x = self.radio
            self.velocidad.x = abs(self.velocidad.x)
        elif self.posicion.x > ANCHO - self.radio:
            self.posicion.x = ANCHO - self.radio
            self.velocidad.x = -abs(self.velocidad.x)

        if self.posicion.y < self.radio:
            self.posicion.y = self.radio
            self.velocidad.y = abs(self.velocidad.y)
        elif self.posicion.y > ALTO - self.radio:
            self.posicion.y = ALTO - self.radio
            self.velocidad.y = -abs(self.velocidad.y)

    def dibujar(self, pantalla: pygame.Surface):
        """Dibuja la pelota en su posición."""
        pygame.draw.circle(pantalla, self.color, self.posicion, self.radio)


class Juego:
    """Ventana con las pelotas y el ciclo de juego."""

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Pelotas que rebotan")
        self.reloj = pygame.time.Clock()
        self.ejecutando = True
        self.pelotas = []
        for _ in range(PELOTAS_INICIALES):
            x = random.randint(RADIO_MAXIMO, ANCHO - RADIO_MAXIMO)
            y = random.randint(RADIO_MAXIMO, ALTO - RADIO_MAXIMO)
            self.pelotas.append(Pelota(x, y))

    def manejar_eventos(self):
        """Cierra la ventana o agrega una pelota con un clic."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            # MOUSEBUTTONDOWN ocurre al pulsar un botón del mouse; pos es
            # la tupla (x, y) donde estaba el puntero
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                self.pelotas.append(Pelota(x, y))

    def actualizar(self, dt: float):
        """Mueve todas las pelotas."""
        for pelota in self.pelotas:
            pelota.actualizar(dt)

    def dibujar(self):
        """Dibuja el fondo y las pelotas."""
        self.pantalla.fill(FONDO)
        for pelota in self.pelotas:
            pelota.dibujar(self.pantalla)
        pygame.display.flip()

    def ejecutar(self):
        """Ciclo de juego: eventos, actualizar y dibujar."""
        while self.ejecutando:
            # tick() devuelve los milisegundos desde la vuelta anterior; al
            # dividir entre 1000 se obtiene el delta time en segundos
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
