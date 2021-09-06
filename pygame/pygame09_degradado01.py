import pygame
import time
import numpy as np
ancho = 1200
alto = 900

BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
GRIS = (100, 100, 100)
ROJO = (255, 10, 10)


def rellenar(screen, puntos, color_superior=ROJO, color_inferior=AZUL):
    p = np.array(puntos)
    miny, maxy = p[:, 1].min(), p[:, 1].max()
    for pos_y in range(miny, maxy):
        escanear_linea_winding(screen, puntos, pos_y=pos_y, color_superior=color_superior, color_inferior=color_inferior)


# is_left(): tests if a point is Left|On|Right of an infinite line.

#   Input: three points P0, P1, and P2
#   Return: >0 for P2 left of the line through P0 and P1
#           =0 for P2 on the line
#           <0 for P2 right of the line
#   See: the January 2001 Algorithm "Area of 2D and 3D Triangles and Polygons"

def is_left(P0, P1, P2):
    return (P1[0] - P0[0]) * (P2[1] - P0[1]) - (P2[0] - P0[0]) * (P1[1] - P0[1])


# ===================================================================

# wn_PnPoly(): winding number test for a point in a polygon
#     Input:  P = a point,
#             V[] = vertex points of a polygon
#     Return: wn = the winding number (=0 only if P is outside V[])


def wn_PnPoly(P, V):
    wn = 0   # the winding number counter

    # loop through all edges of the polygon
    for i in range(len(V)-1):     # edge from V[i] to V[i+1]
        if V[i][1] <= P[1]:        # start y <= P[1]
            if V[i+1][1] > P[1]:     # an upward crossing
                if is_left(V[i], V[i+1], P) > 0:  # P left of edge
                    wn += 1           # have a valid up intersect
        else:                      # start y > P[1] (no test needed)
            if V[i+1][1] <= P[1]:    # a downward crossing
                if is_left(V[i], V[i+1], P) < 0:  # P right of edge
                    wn -= 1           # have a valid down intersect
    return wn


def escanear_linea_winding(screen, puntos, pos_y, color_superior=ROJO, color_inferior=BLANCO):
    """Dibuja una línea en el screen a la altura "pos_y"
    Args:
        screen ([type]): [description]
        puntos (lista de puntos): lista de puntos
    """
    # Primero vamos a encontrar el menor y el mayor de las x e y para no barrer toda la pantalla.
    p = np.array(puntos)
    minx, maxx, miny, maxy = p[:, 0].min(), p[:, 0].max(), p[:, 1].min(), p[:, 1].max()
    #print(f'Los puntos extremos son: {minx} {maxx} {miny} {maxy}')

    # Calculamos la proporción de pos_y entre miny, y maxy.
    proporcion = (pos_y - miny) / (maxy-miny)

    # Calculamos el color.
    # En el caso de que la altura no esté en el rango retornamos
    if pos_y < miny or pos_y > maxy:
        return

    # Nos movemos horizontalmente
    for x in range(minx-1, maxx+1):
        wn = wn_PnPoly((x, pos_y), puntos)
        #print(f'wn para ({x},{pos_y})={wn}')
        if (wn % 2) != 0:
            rojo = color_superior[0] + proporcion*(color_inferior[0]-color_superior[0])
            verde = color_superior[1] + proporcion*(color_inferior[1]-color_superior[1])
            azul = color_superior[2] + proporcion*(color_inferior[2]-color_superior[2])
            color = (rojo, verde, azul)
            pygame.draw.aaline(screen, color, (x, pos_y), (x, pos_y))


def escanear_linea_counting(screen, puntos, pos_y, color_fuera=ROJO, color_dentro=BLANCO):
    """Dibuja una línea en el screen a la altura "pos_y"
    Args:
        screen ([type]): [description]
        puntos (lista de puntos): lista de puntos
    """
    # Primero vamos a encontrar el menor y el mayor de las x e y para no barrer toda la pantalla.
    p = np.array(puntos)
    minx, maxx, miny, maxy = p[:, 0].min(), p[:, 0].max(), p[:, 1].min(), p[:, 1].max()
    #print(f'Los puntos extremos son: {minx} {maxx} {miny} {maxy}')

    # En el caso de que la altura no esté en el rango retornamos
    if pos_y < miny or pos_y > maxy:
        return

    # Nos posicionamos a la altura indicada y hacemos un ciclo para las x
    color = color_fuera
    # Nos movemos horizontalmente
    for x in range(minx-1, maxx+1):
        cn = cn_PnPoly((x, pos_y), puntos)
        #print(f'wn para ({x},{pos_y})={wn}')
        if (cn % 2) == 0:
            #print(f'Cruce pares para x={x} pos_y={pos_y} anteriores:{lados_anteriores} lados actuales={lados_actuales}')
            color = color_fuera
        else:
            #print(f'Cruce impares para x={x} pos_y={pos_y} anteriores:{lados_anteriores} lados actuales={lados_actuales}')
            color = color_dentro
        pygame.draw.aaline(screen, color, (x, pos_y), (x, pos_y))


def leer_puntos(archivo='./pygame/poligono1.txt'):
    # Toma el archivo y crea una lista de puntos.
    puntos = []
    datos = open(archivo)
    try:
        for linea in datos:
            x, y = linea.split(',')
            #print(f'linea={linea} {x} {y}')
            puntos.append((int(x), int(y)))
    except:
        print(f'Error al abrir el archivo {archivo}')
    finally:
        datos.close()
    return puntos

# Dibuja los bordes partiendo de una lista de puntos.


def dibujar_bordes(screen, puntos, color=AZUL):
    for i in range(0, len(puntos)-1):
        pygame.draw.aaline(screen, color, puntos[i], puntos[i+1])


def principal():
    screen = pygame.display.set_mode((ancho, alto))
    running = True

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0, 0, 0))
        archivo = './pygame/dino.txt'
        dibujar_bordes(screen, leer_puntos(archivo))
        rellenar(screen, leer_puntos(archivo))
        pygame.display.flip()
        # time.sleep(3)


if __name__ == '__main__':

    # Simulamos un escaneo
    #punto0 = (2, 1)
    #punto1 = (-1, -5)
    #y = -2
    # for x in range(-4, 6):
    #    print(f'Recta en {x}={valor_y(punto0,punto1,x)}')
    #    punto = (int(x), int(y))
    #    print(f'Lado: {punto0},{punto1},{punto} Lado={encontrar_lado(punto0,punto1,punto)}')

    #escanear_linea('hola', leer_puntos(), pos_y=200)
    principal()
