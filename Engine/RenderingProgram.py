
from OpenGL.GL import *
from Engine.Texture import *


class RenderingProgram:
    def __init__(self, vert_src, frag_src, tex_file_name='', does_support_light=True):
        self.vert_src = open(vert_src).read()
        self.frag_src = open(frag_src).read()
        self.tex_file_name = tex_file_name
        self.rendering_program = glCreateProgram()
        self.vertex_shader = self.load_shader(GL_VERTEX_SHADER, self.vert_src)
        self.fragment_shader = self.load_shader(GL_FRAGMENT_SHADER, self.frag_src)
        glAttachShader(self.rendering_program, self.vertex_shader)
        glAttachShader(self.rendering_program, self.fragment_shader)
        glLinkProgram(self.rendering_program)
        self.vertex_shader = None
        self.fragment_shader = None
        self.does_support_light = does_support_light
        # texture
        self.texture = None
        self.tex_uniform_location = -1
        self.texture_unit = -1
        if self.tex_file_name:
            self.texture = Texture(self.tex_file_name)
            self.tex_uniform_location = glGetUniformLocation(self.rendering_program, "tex")
            self.texture_unit = 1

    def load_shader(self, shader_type, shader_src):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, shader_src)
        glCompileShader(shader)
        compile_success = glGetShaderiv(shader, GL_COMPILE_STATUS)
        if not compile_success:
            error_message = glGetShaderInfoLog(shader)
            glDeleteShader(shader)
            error_message = "\n" + error_message.decode("utf-8")
            raise Exception(error_message)
        return shader
