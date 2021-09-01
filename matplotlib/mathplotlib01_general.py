import numpy as np
from numpy import array as a
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Función particular para escalar de forma manual.
# Sin utilizar la técnica de la multiplicación de matrices.


def escalar(punto, factorx, factory):
    return [punto[0]*factorx, punto[1]*factory]

# t_points = np.arange(0, 1, 0.01)  # ................................. Creates an iterable list from 0 to 1.
# points1 = np.array([[0, 0], [0, 8], [5, 10], [9, 7], [4, 3]])  # .... Creates an array of coordinates.


p1 = [1, 1]
p2 = [8, 2]
p3 = [3, 3]
p4 = [1, 1]
triangulo1 = np.array([p1, p2, p3, p4])

factorx = 0.5
factory = 0.5
triangulo2 = np.array([escalar(p1, factorx, factory), escalar(p2, factorx, factory), escalar(p3, factorx, factory), escalar(p4, factorx, factory)])

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
