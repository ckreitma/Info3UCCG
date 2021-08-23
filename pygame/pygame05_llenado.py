import pygame
import time
ancho = 1200
alto = 900
#screen = pygame.display.set_mode((ancho, alto))
#running = True

# while running:
#event = pygame.event.poll()
# if event.type == pygame.QUIT:
#    running = False
#screen.fill((0, 0, 0))
#pygame.draw.aaline(screen, (0, 100, 255), (0, 0), (ancho-1, alto-1))
#pygame.draw.aaline(screen, (50, 180, 40), (ancho-1, 0), (0, alto-1))
# time.sleep(3)
# pygame.display.flip()


def slope_intercept(x0, y0, x1, y1):
    a = (y1 - y0) / (x1 - x0)
    b = y0 - a * x0
    return a, b


def valor_y(punto0, punto1, x):
    """
    Esta función calculará el valor de la y corrspondiente a
    la ecuación de la recta.
    y = mx + b
    m = pendiente
    b = intersección con el eje vertical
    """
    x0, y0 = punto0
    x1, y1 = punto1

    m, b = slope_intercept(x0, y0, x1, y1)

    # Faltan controlar casos extremos. Pendiente infinita.
    return m*x + b


def encontrar_lado(punto0, punto1, punto):
    """ Calcula el lado en el cual se encuentra
    un punto respecto a una recta (segmento)

    Args:
        punto0 (punto): par inicial
        punto1 (punto):  par final
        punto (punto): Punto

    Returns:
        int: 
            -1 Si está a la izquierda
            +1 Si está a la derecha
            0  Si no se intersecan
    """
    x0, y0 = punto0
    x1, y1 = punto1
    x, y = punto
    x_max = max(x0, x1)
    x_min = min(x0, x1)
    y_max = max(y0, y1)
    y_min = min(y0, y1)

    if x < x_min or x > x_max or y < y_min or y > y_max:
        return 0

    y_punto = valor_y(punto0, punto1, x)
    print(f'<{x},{y_punto}>')
    if y < y_punto:
        return 1
    if y > y_punto:
        return -1
    return 0


if __name__ == '__main__':
    punto0 = (2, 1)
    punto1 = (-1, -5)
    x = 4
    punto = (0, 0)
    print(f'Recta en {x}={valor_y(punto0,punto1,x)}')
    print(f'Lado: {punto0},{punto1},{punto} Lado={encontrar_lado(punto0,punto1,punto)}')
