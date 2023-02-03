
from OpenGL.GL import *


class RenderingProgram:
    def __init__(self, vert_src, frag_src):
        self.vert_src = vert_src
        self.frag_src = frag_src
        self.rendering_program = glCreateProgram()
        self.vertex_shader = self.load_shader(GL_VERTEX_SHADER, vert_src)
        self.fragment_shader = self.load_shader(GL_FRAGMENT_SHADER, frag_src)
        glAttachShader(self.rendering_program, self.vertex_shader)
        glAttachShader(self.rendering_program, self.fragment_shader)
        glLinkProgram(self.rendering_program)
        self.vertex_shader = None
        self.fragment_shader = None

    def load_shader(self, shader_type, shader_src):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, shader_src)
        glCompileShader(shader)
        return shader
