from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

rotacion = [30, 0, 0.2, 0]
rotacion_eje = [30, 0.1, 0.2, 0]
window = None


def Cube():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 600/600, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(4, 5, 5, 0, 0, 0, 0, 1, 0)
    glTranslatef(0.0, 0.0, -5)
    print(f'Rotacion:{rotacion}')
    glPushMatrix()
    glRotatef(rotacion_eje[0], rotacion_eje[1], rotacion_eje[2], rotacion_eje[3])
    glBegin(GL_LINES)
    glColor3f(2.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(2.0, 0.0, 0.0)
    glColor3f(0.0, 2.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)
    glColor3f(0.0, 0.0, 2.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 2.0)
    glEnd()
    glPopMatrix()
    glRotatef(rotacion[0], rotacion[1], rotacion[2], rotacion[3])
    glBegin(GL_LINES)
    glColor3f(0.9, 0.9, 0.9)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glVertex3f(2.0, 0.0, 0.0)
    glEnd()
    glFlush()


def keyPressed(*args):
    global rotacion
    global window
    # If escape is pressed, kill everything.
    print(f'{args[0]}')
    if args[0] == b'0x1b':
        print(f'Terminando el programa...')
        glutDestroyWindow(window)

    if args[0] == b'z':
        rotacion[0] += 1
        glutPostRedisplay()

    if args[0] == b'x':
        rotacion[0] -= 1
        glutPostRedisplay()


def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Cubo OpenGL")
    glutDisplayFunc(Cube)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()


main()
