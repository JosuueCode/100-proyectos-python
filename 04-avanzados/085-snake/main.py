"""Proyecto 085: Snake.

La serpiente avanza por una cuadrícula, crece al comer y acelera poco a
poco. El juego termina si choca con una pared o con su propio cuerpo.
"""

import random
from enum import Enum

import pygame

CELDA = 25
COLUMNAS = 24
FILAS = 22
ALTO_BARRA = 50
ANCHO = CELDA * COLUMNAS
ALTO = CELDA * FILAS + ALTO_BARRA
FPS = 60
INTERVALO_INICIAL = 0.15
INTERVALO_MINIMO = 0.05
ACELERACION = 0.005
ARCHIVO_RECORD = "record.txt"
FONDO = (18, 24, 18)
CUADRICULA = (28, 36, 28)
BARRA = (10, 14, 10)
CABEZA = (129, 199, 132)
CUERPO = (67, 160, 71)
COMIDA = (239, 83, 80)
BLANCO = (235, 235, 235)
OSCURECER = (0, 0, 0, 170)

ARRIBA = (0, -1)
ABAJO = (0, 1)
IZQUIERDA = (-1, 0)
DERECHA = (1, 0)
# Cada tecla se relaciona con la dirección a la que lleva
TECLAS = {
    pygame.K_UP: ARRIBA, pygame.K_w: ARRIBA,
    pygame.K_DOWN: ABAJO, pygame.K_s: ABAJO,
    pygame.K_LEFT: IZQUIERDA, pygame.K_a: IZQUIERDA,
    pygame.K_RIGHT: DERECHA, pygame.K_d: DERECHA,
}


class Estado(Enum):
    """Estados del juego."""

    JUGANDO = "jugando"
    FIN = "fin"


def leer_record() -> int:
    """Devuelve el récord guardado, o 0 si no hay archivo válido."""
    try:
        with open(ARCHIVO_RECORD, "r", encoding="utf-8") as archivo:
            return int(archivo.read().strip())
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0


def guardar_record(puntos: int):
    """Escribe el récord nuevo en el archivo."""
    with open(ARCHIVO_RECORD, "w", encoding="utf-8") as archivo:
        archivo.write(str(puntos))


class Serpiente:
    """Serpiente formada por una lista de celdas (columna, fila)."""

    def __init__(self):
        centro_columna = COLUMNAS // 2
        centro_fila = FILAS // 2
        # El primer elemento de la lista es la cabeza y el último la cola
        self.segmentos = [
            (centro_columna, centro_fila),
            (centro_columna - 1, centro_fila),
            (centro_columna - 2, centro_fila),
        ]
        self.direccion = DERECHA
        self.siguiente_direccion = DERECHA

    def cambiar_direccion(self, nueva: tuple):
        """Guarda la nueva dirección si no es la contraria a la actual."""
        # La dirección contraria tiene los dos valores con el signo
        # cambiado: girar de DERECHA (1, 0) a IZQUIERDA (-1, 0) haría que
        # la cabeza chocara con el cuello. Se compara con la dirección del
        # último paso, no con la última tecla, para que dos teclas rápidas
        # dentro del mismo paso tampoco permitan darse la vuelta.
        contraria = (-self.direccion[0], -self.direccion[1])
        if nueva != contraria:
            self.siguiente_direccion = nueva

    def proxima_cabeza(self) -> tuple:
        """Devuelve la celda a la que se moverá la cabeza."""
        self.direccion = self.siguiente_direccion
        columna, fila = self.segmentos[0]
        return (columna + self.direccion[0], fila + self.direccion[1])

    def avanzar(self, cabeza: tuple, crecer: bool):
        """Agrega la cabeza nueva y quita la cola si no está creciendo."""
        # insert(0, valor) agrega al inicio de la lista. Si no come, se
        # quita el último segmento con pop() y la serpiente mide lo mismo.
        self.segmentos.insert(0, cabeza)
        if not crecer:
            self.segmentos.pop()

    def dibujar(self, pantalla: pygame.Surface):
        """Dibuja cada segmento como un cuadro de la cuadrícula."""
        for indice, segmento in enumerate(self.segmentos):
            if indice == 0:
                color = CABEZA
            else:
                color = CUERPO
            columna, fila = segmento
            rect = rect_de_celda(columna, fila)
            # inflate(-2, -2) encoge el rect 2 píxeles para dejar una
            # separación entre segmentos, y border_radius redondea las
            # esquinas del rectángulo
            pygame.draw.rect(pantalla, color, rect.inflate(-2, -2),
                             border_radius=5)


def rect_de_celda(columna: int, fila: int) -> pygame.Rect:
    """Convierte una celda de la cuadrícula en un rectángulo en píxeles."""
    return pygame.Rect(columna * CELDA, fila * CELDA + ALTO_BARRA,
                       CELDA, CELDA)


class Juego:
    """Partida de Snake con récord guardado en un archivo."""

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Snake")
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 36)
        self.fuente_grande = pygame.font.Font(None, 72)
        self.ejecutando = True
        self.record = leer_record()
        self.reiniciar()

    def reiniciar(self):
        """Prepara una partida nueva."""
        self.serpiente = Serpiente()
        self.puntos = 0
        self.intervalo = INTERVALO_INICIAL
        # La serpiente no se mueve en cada cuadro sino cada cierto tiempo.
        # acumulado suma el tiempo que pasó hasta completar un paso.
        self.acumulado = 0.0
        self.record_nuevo = False
        self.estado = Estado.JUGANDO
        self.colocar_comida()

    def colocar_comida(self):
        """Pone la comida en una celda al azar que no ocupe la serpiente."""
        # Se arma la lista de celdas libres y se elige una de ellas; así la
        # comida nunca aparece encima de la serpiente
        libres = []
        for columna in range(COLUMNAS):
            for fila in range(FILAS):
                if (columna, fila) not in self.serpiente.segmentos:
                    libres.append((columna, fila))
        if len(libres) == 0:
            self.terminar()
            return
        self.comida = random.choice(libres)

    def manejar_eventos(self):
        """Cambia la dirección o reinicia según la tecla."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.ejecutando = False
                elif self.estado == Estado.FIN:
                    if evento.key == pygame.K_SPACE:
                        self.reiniciar()
                elif evento.key in TECLAS:
                    self.serpiente.cambiar_direccion(TECLAS[evento.key])

    def actualizar(self, dt: float):
        """Avanza un paso cada vez que se junta el intervalo."""
        if self.estado != Estado.JUGANDO:
            return
        self.acumulado = self.acumulado + dt
        if self.acumulado >= self.intervalo:
            self.acumulado = self.acumulado - self.intervalo
            self.dar_paso()

    def dar_paso(self):
        """Mueve la serpiente una celda y revisa choques y comida."""
        cabeza = self.serpiente.proxima_cabeza()
        columna, fila = cabeza
        fuera = columna < 0 or columna >= COLUMNAS or fila < 0 or fila >= FILAS
        come = cabeza == self.comida
        # Si no come, la cola se moverá en este paso, así que la cabeza sí
        # puede entrar en la celda donde está ahora la cola
        if come:
            cuerpo = self.serpiente.segmentos
        else:
            cuerpo = self.serpiente.segmentos[:-1]
        if fuera or cabeza in cuerpo:
            self.terminar()
            return

        self.serpiente.avanzar(cabeza, come)
        if come:
            self.puntos = self.puntos + 1
            self.intervalo = max(INTERVALO_MINIMO,
                                 self.intervalo - ACELERACION)
            self.colocar_comida()

    def terminar(self):
        """Pasa al estado FIN y guarda el récord si se superó."""
        self.estado = Estado.FIN
        if self.puntos > self.record:
            self.record = self.puntos
            self.record_nuevo = True
            guardar_record(self.puntos)

    def escribir(self, texto: str, fuente: pygame.font.Font, centro: tuple):
        """Dibuja un texto blanco centrado en el punto indicado."""
        superficie = fuente.render(texto, True, BLANCO)
        self.pantalla.blit(superficie, superficie.get_rect(center=centro))

    def dibujar(self):
        """Dibuja la barra, la cuadrícula, la comida y la serpiente."""
        self.pantalla.fill(FONDO)
        for columna in range(COLUMNAS):
            for fila in range(FILAS):
                if (columna + fila) % 2 == 0:
                    rect = rect_de_celda(columna, fila)
                    pygame.draw.rect(self.pantalla, CUADRICULA, rect)

        pygame.draw.rect(self.pantalla, BARRA, (0, 0, ANCHO, ALTO_BARRA))
        self.escribir(f"Puntos: {self.puntos}", self.fuente, (ANCHO // 4, 25))
        self.escribir(f"Récord: {self.record}", self.fuente,
                      (ANCHO * 3 // 4, 25))

        centro_comida = rect_de_celda(self.comida[0], self.comida[1]).center
        pygame.draw.circle(self.pantalla, COMIDA, centro_comida,
                           CELDA // 2 - 2)
        self.serpiente.dibujar(self.pantalla)

        if self.estado == Estado.FIN:
            # Una capa negra semitransparente oscurece el tablero para que
            # el mensaje se lea bien encima de la serpiente
            capa = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            capa.fill(OSCURECER)
            self.pantalla.blit(capa, (0, 0))
            centro_y = ALTO // 2
            self.escribir("Fin del juego", self.fuente_grande,
                          (ANCHO // 2, centro_y - 40))
            if self.record_nuevo:
                self.escribir("Nuevo récord", self.fuente,
                              (ANCHO // 2, centro_y + 10))
            self.escribir("Espacio para jugar otra vez", self.fuente,
                          (ANCHO // 2, centro_y + 50))
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
