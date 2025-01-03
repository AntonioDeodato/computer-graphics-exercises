import glfw
from OpenGL.GL import *

point1 = [-0.5,-0.5]
point2 = [-0.5,0.5]
point3 = [0,0]
point4 = [0.5, 0.5]
point5 = [0.5,-0.5]


def init():
    glClearColor(1,1,1,1)
    glLineWidth(5)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_STRIP)
    glColor3f(1,0,0)
    glVertex2fv(point1)
    glColor3f(1,1,0)
    glVertex2fv(point2)
    glColor3f(1,0,1)
    glVertex2fv(point3)
    glColor3f(0,0,0)
    glVertex2fv(point4)
    glColor3f(1,0,0)
    glVertex2fv(point5)

    glEnd()

def main():
    glfw.init()
    janela = glfw.create_window(500, 500, 'inter', None, None)
    glfw.make_context_current(janela)
    init()
    while not glfw.window_should_close(janela):
        glfw.poll_events()
        render()
        glfw.swap_buffers(janela)
    glfw.terminate()    


if __name__ == '__main__':
    main()