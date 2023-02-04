
import numpy as np
from OpenGL.GL import *
from Engine.RenderingProgram import *


class Axes:
    def __init__(self, rendering_program):
        self.rendering_program = rendering_program
        self.vertices = [[-1000, 0, 0], [1000, 0, 0], [0, -1000, 0], [0, 1000, 0], [0, 0, -1000], [0, 0, 1000]]
        self.vertices = np.array(self.vertices, np.float32)
        self.vertex_colors = [[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]]
        self.vertex_colors = np.array(self.vertex_colors, np.float32)
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = [0, 0]
        self.vbo[0] = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo[0])
        glBufferData(GL_ARRAY_BUFFER, self.vertices.ravel(), GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(0)
        self.vbo[1] = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo[1])
        glBufferData(GL_ARRAY_BUFFER, self.vertex_colors.ravel(), GL_STATIC_DRAW)
        glVertexAttribPointer(1, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(1)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def draw(self):
        glUseProgram(self.rendering_program)
        glBindVertexArray(self.vao)
        glDrawArrays(GL_LINES, 0, len(self.vertices))
        glBindVertexArray(0)
