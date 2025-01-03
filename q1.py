import glfw
from OpenGL.GL import *

point = [0.5, 0.5]
point1 = [-0.5, 0.5]
point2 = [-0.5, -0.5]
point3 = [0.5, -0.5]


def init():
    glClearColor(1,1,1,1)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glPointSize(20)                
    glBegin(GL_POINTS)
    glColor3f(1,0,1)            
    glVertex2fv(point)
    glColor3f(0,1,0)
    glVertex2fv(point1)
    glColor3f(0,0,1)
    glVertex2fv(point2)
    glColor3f(1,0,0)
    glVertex2fv(point3)


    glEnd()

def main ():
    glfw.init() 
    janela = glfw.create_window(500,500,'intro',None,None) #cria uma janela
    glfw.make_context_current(janela)
    init()
    while not glfw.window_should_close(janela):
        glfw.poll_events()
        render()
        glfw.swap_buffers(janela)
    glfw.terminate()

if __name__ == '__main__':
    main()