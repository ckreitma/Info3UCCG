# https://pharos.sh/breve-introduccion-a-opengl-en-python-con-pyopengl/

# pip install PyOpenGL PyOpenGL_accelerate

from OpenGL.GL import (
    GL_COLOR_BUFFER_BIT,
    GL_DEPTH_BUFFER_BIT,
    glClear,
)
from OpenGL.GLUT import (
    GLUT_RGBA,
    glutInit,
    glutInitDisplayMode,
    glutInitWindowSize,
    glutInitWindowPosition,
    glutCreateWindow,
    glutDisplayFunc,
    glutIdleFunc,
    glutMainLoop,
)


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Remove everything from screen (i.e. displays all white)


def opengl01():
    glutInit()  # Inicializa lal instancia OpenGL
    glutInitDisplayMode(GLUT_RGBA)  # Eligiendo el modo en el cual se van a colorear los objetos
    glutInitWindowSize(900, 900)   # Set the width and height of your window
    glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
    wind = glutCreateWindow("OpenGL Coding Practice")  # Give your window a title
    glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
    glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times
    glutMainLoop()  # Keeps the window created above displaying/running in a loop


if __name__ == "__main__":
    opengl01()
