import glfw
from OpenGL.GL import *

point1 = [0,0.5]
point2 = [-0.5,0]
point3 = [0.5,0.5]
point4 = [-0.5,-0.5]
point5 = [0,-0.5]
point6 = [0.5,0.0]

def init():
    glClearColor(1,1,1,1)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(10)
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex2fv(point1)
    glVertex2fv(point2)
    glVertex2fv(point3)
    glVertex2fv(point4)
    glVertex2fv(point5)
    glVertex2fv(point6)



    glEnd()

def main():
    glfw.init()
    janela = glfw.create_window(500,500, 'intro',None,None)
    glfw.make_context_current(janela)
    init()
    while not glfw.window_should_close(janela):
        glfw.poll_events()
        render()
        glfw.swap_buffers(janela)
    glfw.terminate()

if __name__ == '__main__':
    main()