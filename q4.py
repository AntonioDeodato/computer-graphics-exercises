import glfw
from OpenGL.GL import *

point1 = [0,0.5]
point2 = [0.1,0.1]
point3 = [0.5,0]
point4 = [0.1,-0.1]
point5 = [0,-0.5]
point6 = [-0.1,-0.1]
point7 = [-0.5,0]
point8 = [-0.1,0.1]



def init():
    glClearColor(1,1,1,1)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)
    glColor3b(1,1,0)
    glVertex2fv(point1)
    glColor3b(1,1,0)
    glVertex2fv(point2)
    glColor3b(1,1,0)
    glVertex2fv(point3)
    glColor3b(1,1,0)
    glVertex2fv(point4)
    glColor3b(1,1,0)
    glVertex2fv(point5)
    glColor3b(1,1,0)
    glVertex2fv(point6)
    glColor3b(1,1,0)
    glVertex2fv(point7)
    glColor3b(1,1,0)
    glVertex2fv(point8)

    glEnd()

def main():
    glfw.init()
    janela = glfw.create_window(500,500,'intor',None,None)
    glfw.make_context_current(janela)
    init()
    while not glfw.window_should_close(janela):
        glfw.poll_events()
        render()
        glfw.swap_buffers(janela)
    glfw.terminate

if __name__ == '__main__':
    main()