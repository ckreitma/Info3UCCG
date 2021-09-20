from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

vertices = (
    1, 1, 1,
    1, 1, -1,
    1, -1, -1,
    1, -1, 1,
    -1, 1, 1,
    -1, 1, -1,
    -1, -1, -1,
    -1, -1, 1
)

colors = (
    1, 1, 1,
    1, 0, 0,
    1, 1, 0,
    0, 1, 0,
    0, 0, 1,
    1, 0, 1,
    0, 0, 0,
    0, 1, 1,
)

faces = (
    0, 1, 2, 3,
    0, 3, 7, 4,
    0, 4, 5, 1,
    6, 2, 1, 5,
    6, 5, 4, 7,
    6, 7, 3, 2
)


rotacion = [0, 0, 1, 0]
rotacion_eje = [0, 0, 1, 0]
window = None


def ejes():
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


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Remove everything from screen (i.e. displays all white)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 600/600, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)
    #glTranslatef(0.0, 0.0, -5)
    ejes()
    cubo()
    glFlush()


def cubo():
    print(f'Cubo con rotacion={rotacion}')
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glColorPointer(3, GL_FLOAT, 0, colors)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glRotatef(rotacion[0], rotacion[1], rotacion[2], rotacion[3])
    glDrawElements(GL_QUADS, 24, GL_UNSIGNED_INT, faces)
    glPopMatrix()


def keyPressed(*args):
    global rotacion
    global window
    # If escape is pressed, kill everything.
    print(f'{args[0]}')
    if args[0] == b'0x1b':
        print(f'Terminando el programa...')
        glutDestroyWindow(window)

    if args[0] == b'+':
        rotacion[0] += 1
        glutPostRedisplay()

    if args[0] == b'-':
        rotacion[0] -= 1
        glutPostRedisplay()

    if args[0] == b'x':
        rotacion = [0, 1, 0, 0]
        glutPostRedisplay()

    if args[0] == b'y':
        rotacion = [0, 0, 1, 0]
        glutPostRedisplay()

    if args[0] == b'z':
        rotacion = [0, 0, 0, 1]
        glutPostRedisplay()


def main():
    global window
    glutInit(sys.argv)
    #glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Cubo Indexed Face Sets")
    glutDisplayFunc(draw)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()


main()
