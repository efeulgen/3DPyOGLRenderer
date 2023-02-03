
import numpy as np
import pygame
from OpenGL.GL import *

from Engine.Transformations import *


class Mesh:
    def __init__(self, rendering_program, draw_type=GL_TRIANGLES, file_name="PrimitiveMeshes/cube.obj",
                 init_location=pygame.Vector3(0, 0, 0),
                 init_rotation=Rotation(),
                 init_scale=pygame.Vector3(1, 1, 1)):
        self.rendering_program = rendering_program
        self.draw_type = draw_type
        self.file_name = file_name
        self.vertices = []
        self.vertex_indices = []
        self.normals = []
        self.normal_indices = []
        self.uvs = []
        self.uv_indices = []
        self.vao = glGenVertexArrays(1)
        self.vbo = []
        self.load_obj_file()
        self.translation = identity_mat()
        self.translation = translate(self.translation, init_location.x, init_location.y, init_location.z)
        self.translation = rotate_around_axis(self.translation, init_rotation.angle, init_rotation.axis)
        self.translation = scale(self.translation, init_scale.x, init_scale.y, init_scale.z)

    def create_vbo(self, graphics_data, layout_location, data_type):
        data = np.array(graphics_data, np.float32)
        self.vbo.append(0)
        glBindVertexArray(self.vao)
        self.vbo[-1] = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo[-1])
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)
        if data_type == "vec3":
            glVertexAttribPointer(layout_location, 3, GL_FLOAT, False, 0, None)
        elif data_type == "vec2":
            glVertexAttribPointer(layout_location, 2, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(layout_location)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def create_uniform(self, data, data_type):
        pass

    def load_obj_file(self):
        with open(self.file_name) as fp:
            line = fp.readline()
            while line:
                if line[:2] == "v ":
                    vx, vy, vz, = [float(value) for value in line[2:].split()]
                    self.vertices.append((vx, vy, vz))
                if line[:3] == "vn ":
                    nx, ny, nz = [float(value) for value in line[2:].split()]
                    self.normals.append((nx, ny, nz))
                if line[:3] == "vt ":
                    u, v = [float(value) for value in line[3:].split()]
                    self.uvs.append((u, v))
                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in line[2:].split()]
                    self.vertex_indices.append([int(value) for value in t1.split("/")][0] - 1)
                    self.vertex_indices.append([int(value) for value in t2.split("/")][0] - 1)
                    self.vertex_indices.append([int(value) for value in t3.split("/")][0] - 1)
                    self.uv_indices.append([int(value) for value in t1.split("/")][1] - 1)
                    self.uv_indices.append([int(value) for value in t2.split("/")][1] - 1)
                    self.uv_indices.append([int(value) for value in t3.split("/")][1] - 1)
                    self.normal_indices.append([int(value) for value in t1.split("/")][2] - 1)
                    self.normal_indices.append([int(value) for value in t2.split("/")][2] - 1)
                    self.normal_indices.append([int(value) for value in t3.split("/")][2] - 1)
                line = fp.readline()

    def draw(self):
        glBindVertexArray(self.vao)
        glUseProgram(self.rendering_program)
        glDrawArrays(self.draw_type, 0, len(self.vertices))
        glBindVertexArray(0)
