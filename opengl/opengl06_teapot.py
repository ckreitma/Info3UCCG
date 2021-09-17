# https://codeloop.org/python-opengl-programming-drawing-teapot/
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)  # Apunta a la matriz de proyección
    glLoadIdentity()
    # Matriz de proyección ortogonal
    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glColor3f(0.5, 0.5, 0.5)
    glRotate(10.0, 1, 0.3, 0.0)
    glutWireTeapot(0.5)

    # Eje de coordenadas
    glBegin(GL_LINES)

    # Eje X en rojo
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(2.0, 0.0, 0.0)

    # Eje Y en Verde
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)

    # Eje Z en Azul
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 2.0)
    glEnd()
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
glutCreateWindow("Tetera")
glutDisplayFunc(draw)
glutMainLoop()
