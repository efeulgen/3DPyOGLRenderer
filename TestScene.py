
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Engine.Scene import *
from Engine.Mesh import *


vertex_shader_source = r'''
#version 330 core
layout(location=0) in vec3 pos;
void main()
{
    gl_Position = vec4(pos, 1.0);
}
'''

fragment_shader_source = r'''
#version 330 core
out vec4 frag_color;
void main()
{
    frag_color = vec4(1.0, 1.0, 1.0, 1.0);
}
'''


def create_shader(shader_source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, shader_source)
    glCompileShader(shader)
    return shader


def create_rendering_program(vert_src, frag_src):
    vertex_shader = create_shader(vert_src, GL_VERTEX_SHADER)
    fragment_shader = create_shader(frag_src, GL_FRAGMENT_SHADER)
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)
    return program


class TestScene(Scene):
    def __init__(self):
        super().__init__()
        self.rendering_program = None
        self.cube = None

    def init(self):
        glClearColor(0.2, 0.2, 0.21, 1.0)
        vertex_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertex_shader, vertex_shader_source)
        glCompileShader(vertex_shader)
        fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment_shader, fragment_shader_source)
        glCompileShader(fragment_shader)
        self.rendering_program = glCreateProgram()
        glAttachShader(self.rendering_program, vertex_shader)
        glAttachShader(self.rendering_program, fragment_shader)
        glLinkProgram(self.rendering_program)
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

        self.cube = Mesh(self.rendering_program)
        self.cube.create_vbo(self.cube.vertices, 0, "vec3")

    def update(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.cube.draw()


TestScene().main_loop()
