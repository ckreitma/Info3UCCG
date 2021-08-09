# https://lorenzod8n.wordpress.com/category/pygame-tutorial/
# Dibujo de Ventana Principal
import pygame

screen = pygame.display.set_mode((1200, 900))
running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
