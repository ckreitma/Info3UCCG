# https://codeloop.org/python-opengl-programming-drawing-teapot/
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)  # Apunta a la matriz de proyección
    glPushMatrix()
    glLoadIdentity()

    gluPerspective(30.0, 1.0, 1.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # Posición del ojo.
    gluLookAt(-2, 3, 0, 0, 0, 0, 0, 1, 0)
    glColor3f(0.5, 0.5, 0.5)
    glutWireTeapot(0.5)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(2.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 2.0)
    glEnd()

    glFlush()
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
glutCreateWindow("Tetera")
glutDisplayFunc(draw)
glutMainLoop()
