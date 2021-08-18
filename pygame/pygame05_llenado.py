import pygame
import time
ancho = 1200
alto = 900
screen = pygame.display.set_mode((ancho, alto))
running = True

# while running:
event = pygame.event.poll()
if event.type == pygame.QUIT:
    running = False
screen.fill((0, 0, 0))
pygame.draw.aaline(screen, (0, 100, 255), (0, 0), (ancho-1, alto-1))
pygame.draw.aaline(screen, (50, 180, 40), (ancho-1, 0), (0, alto-1))
time.sleep(3)
pygame.display.flip()
