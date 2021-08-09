"""for i = 0 to numberOfLines:
   	angle1 = i * (2*pi/numberOfLines)
   	angle2 = (i+1) * (2*pi/numberOfLines)
	x1 = x + r1*cos(angle1)
	y1 = y + r2*sin(angle1)
	x2 = x + r1*cos(angle2)
	y2 = y + r2*sin(angle2)
	Draw Line from (x1,y1) to (x2,y2)
    """

import pygame
from math import sin, cos, pi
from time import sleep
ancho = 1000
alto = 1000
screen = pygame.display.set_mode((ancho, alto))
running = True

centro = {
    'x': ancho/2,
    'y': alto/2
}

r1 = 200
r2 = 450

cantidad_rectas = 32
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    screen.fill((0, 0, 0))
    for i in range(0, cantidad_rectas):
        # Calculamos los cuatro puntos para la siguiente recta.
        angulo1 = i * (2*pi/cantidad_rectas)
        angulo2 = (i+1) * (2*pi/cantidad_rectas)
        #print(f'Ángulos: <{i},{angulo1},{angulo2}')
        x1 = centro['x'] + r1*cos(angulo1)
        y1 = centro['y'] + r2*sin(angulo1)
        x2 = centro['x'] + r1*cos(angulo2)
        y2 = centro['y'] + r2*sin(angulo2)
        # print(f'Puntos=<{i},{x1},{y1},{x2},{y2}')
        pygame.draw.line(screen, (0, 100, 255), (x1, y1), (x2, y2))
    pygame.display.flip()
