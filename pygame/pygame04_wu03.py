"""Script demonstrating drawing of anti-aliased lines using Xiaolin Wu's line
algorithm

usage: python xiaolinwu.py [output-file]

"""
from __future__ import division
import sys

from PIL import Image
import pygame

# Ancho y alto teórico
ancho_teorico = 1000
alto_teorico = 1000

# Ancho y alto real
ancho_real = 100
alto_real = 100

# Relation (ratio) de aspecto entre el real y el teórico
delta_x = int(ancho_teorico/ancho_real)
delta_y = int(alto_teorico/alto_real)

screen = pygame.display.set_mode((ancho_teorico, alto_teorico))
running = True

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRIS = (100, 100, 100)
ROJO = (255, 10, 10)
YELLOW = (255, 255, 0)


# Dividir proporcionalmente a
# la parte decimal de x un "1"
def _fpart(x):
    """ 1.3 ==> 0.3
    """
    return x - int(x)


def _rfpart(x):
    """ 1.3 ==> 0.7
    """
    return 1 - _fpart(x)


def dibujar_grilla(screen):

    # Lineas horizontales
    for pos_y in range(0, alto_teorico, delta_y):
        # print(f'pos_y={pos_y}')
        pygame.draw.aaline(screen, GRIS, (0, pos_y), (ancho_teorico, pos_y))

    # Lineas verticales
    for pos_x in range(0, ancho_teorico, delta_x):
        # print(f'pos_y={pos_y}')
        pygame.draw.aaline(screen, GRIS, (pos_x, 0), (pos_x, alto_teorico))


def putpixel(screen, xy, color, alpha=1):
    """Paints color over the background at the point xy in img.

    Use alpha for blending. alpha=1 means a completely opaque foreground.

    """
    x, y = xy
    if x < 0 or x > ancho_real or y < 0 or y > alto_real:
        print(f'Punto incorrecto <{x},{y}>')
        return
    pixel_real = (x*delta_x, y*delta_y, delta_x, delta_y)
    # print(f'Pixel real={pixel_real}')
    # Rectángulo (<origen>,<ancho>,<alto>)
    c = tuple(map(lambda bg, fg: int(round(alpha * fg + (1-alpha) * bg)),
                  BLACK, color))
    pygame.draw.rect(screen, c, pixel_real)
    # c = tuple(map(lambda bg, fg: int(round(alpha * fg + (1-alpha) * bg)),
    #              img.getpixel(xy), color))
    #print(f'color={color} alpha={alpha} c={c}')
    #img.putpixel(xy, c)


def draw_line(screen, x0, y0, x1, y1, color):
    """Draws an anti-aliased line in img from p1 to p2 with the given color."""
    p1 = (x0, y0)
    p2 = (x1, y1)
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x2-x1, y2-y1
    steep = abs(dx) < abs(dy)

    def p(px, py):
        # Seleccionar el primer o segundo par dependiendo de true/false de steep.
        return ((px, py), (py, px))[steep]

    if steep:
        x1, y1, x2, y2, dx, dy = y1, x1, y2, x2, dy, dx
    if x2 < x1:
        x1, x2, y1, y2 = x2, x1, y2, y1

    # Podemos asumir que los puntos son esquina superior izquierda y esquina inferior derecha
    grad = dy/dx
    intery = y1 + _rfpart(x1) * grad

    # Dibujar los puntos extremos
    def draw_endpoint(pt):
        x, y = pt
        xend = round(x)
        yend = y + grad * (xend - x)
        xgap = _rfpart(x + 0.5)
        px, py = int(xend), int(yend)
        putpixel(screen, p(px, py), color, _rfpart(yend) * xgap)
        putpixel(screen, p(px, py+1), color, _fpart(yend) * xgap)
        return px

    xstart = draw_endpoint(p(*p1)) + 1
    xend = draw_endpoint(p(*p2))

    for x in range(xstart, xend):
        y = int(intery)
        #print(f'p({x},{y})={p(x,y)} alpha={_rfpart(intery)}')
        putpixel(screen, p(x, y), color, _rfpart(intery))
        putpixel(screen, p(x, y+1), color, _fpart(intery))
        print(
            f'intery={intery} rfpart={_rfpart(intery)} fpart={_fpart(intery)}')
        intery += grad


if __name__ == '__main__':
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        screen.fill(BLACK)
        dibujar_grilla(screen)
        # Prueba de pixel con transparencias
        putpixel(screen, (4, 7), YELLOW)
        putpixel(screen, (5, 8), YELLOW, alpha=0.6)

        draw_line(screen, 12, 20, 50, 25, GRIS)
        pygame.display.flip()

        #draw_line(screen, (10, 10), (30, 80), WHITE)
