# http://openglsamples.sourceforge.net/teapot_py.html
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'OpenGL Python Teapot'


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400, 400)
    glutCreateWindow(name)

    glClearColor(0., 0., 1., 1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [-20., 2., -2., 1.]
    lightZeroColor = [1.8, 1.0, 0.8, 1.0]  # green tinged
    ambientColor = [1., 1., 1., 1.]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    #glLightfv(GL_LIGHT0, GL_AMBIENT, ambientColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40., 1., 1., 40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, 0, 10,
              0, 0, 0,
              0, 1, 0)
    glPushMatrix()
    glutMainLoop()
    return


def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    color = [1.0, 0., 0., 1.]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
    glRotatef(180, 1, 0, 0)
    glRotatef(-45, 0, 1, 0)
    glutSolidTeapot(-2, 20, -20)

    glPopMatrix()
    glutSwapBuffers()

    return


if __name__ == '__main__':
    main()