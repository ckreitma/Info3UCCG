import numpy as np
from numpy import array as a
import matplotlib.pyplot as plt
from math import sin, cos, pi


# Función particular para escalar de forma manual.
# Sin utilizar la técnica de la multiplicación de matrices.


# t_points = np.arange(0, 1, 0.01)  # ................................. Creates an iterable list from 0 to 1.
# points1 = np.array([[0, 0], [0, 8], [5, 10], [9, 7], [4, 3]])  # .... Creates an array of coordinates.


def tranformar_triangulos():
    # Puntos en coordenadas homogéneas
    p1 = [1, 1, 1]
    p2 = [8, 2, 1]
    p3 = [3, 3, 1]
    p4 = [1, 1, 1]

    triangulo1 = np.array([p1, p2, p3, p4])

    # Matriz de transformación para escalamiento
    factorx = 0.2
    factory = 0.45
    escalar = np.array([[factorx, 0, 0], [0, factory, 0], [0, 0, 1]])

    # Matriz de desplazamiento.
    tx = 2
    ty = -4
    desplazamiento = np.array([[1, 0, 0], [0, 1, 0], [tx, ty, 1]])

    # Rotación origen
    angulo = 0.12
    rotacion = np.array([[cos(angulo), sin(angulo), 0], [-sin(angulo), cos(angulo), 0], [0, 0, 1]])

    # Rotación de angulo (a) respecto a  xc,yc
    a = 0.4
    xc = 3.5
    yc = 2.0

    t0 = np.array([[1, 0, 0], [0, 1, 0], [-xc, -yc, 1]])
    r0 = np.array([[cos(a), sin(a), 0], [-sin(a), cos(a), 0], [0, 0, 1]])
    t1 = np.array([[1, 0, 0], [0, 1, 0], [xc, yc, 1]])

    # Matriz de transformación completa.
    #m = np.matmul(rotacion, np.matmul(desplazamiento, escalar))
    m = np.matmul(t0, np.matmul(r0, t1))
    print(f'Forma de m {m.shape} \n{m}')

    triangulo2 = np.array([np.matmul(p1, m), np.matmul(p2, m), np.matmul(p3, m), np.matmul(p4, m)])

    plt.figure()
    # plt.plot(
    #    points1[:, 0],  # x-coordinates.
    #    points1[:, 1],  # y-coordinates.
    #    'ro:'           # Styling (red, circles, dotted).
    # )

    plt.plot(triangulo1[:, 0], triangulo1[:, 1], 'bo-')
    plt.plot(triangulo2[:, 0], triangulo2[:, 1], 'ro-')
    #plt.plot((1, 2), (12, 15), 'bo:')
    plt.grid()
    plt.show()


def multiplicacion():
    punto = np.array([2, 7, 1])
    matriz = np.array([[0.5, 0, 0], [0, 0.2, 0], [0, 0, 1]])

    print(f'Forma de matriz {matriz.shape} \n{matriz}')

    resultado = np.matmul(punto, matriz)
    print(f'Forma de resultado {resultado.shape} \n{resultado}')


if __name__ == '__main__':
    tranformar_triangulos()
