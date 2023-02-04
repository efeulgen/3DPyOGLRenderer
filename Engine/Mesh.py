
import random

import pygame
from OpenGL.GL import *

from Engine.Transformations import *
from Engine.Utils import *


class Mesh:
    def __init__(self, rendering_program,
                 draw_type=GL_TRIANGLES,
                 file_name="Engine/PrimitiveMeshes/cube.obj",
                 vertex_color=pygame.Vector3(1, 1, 1),
                 init_location=pygame.Vector3(0, 0, 0),
                 init_rotation=Rotation(),
                 init_scale=pygame.Vector3(1, 1, 1)):
        self.rendering_program = rendering_program
        self.draw_type = draw_type
        self.file_name = file_name
        self.vertex_color = vertex_color
        self.vertices = []
        self.vertex_indices = []
        self.normals = []
        self.normal_indices = []
        self.uvs = []
        self.uv_indices = []
        self.vao = glGenVertexArrays(1)
        self.vbo = []
        self.load_obj_file()  # optional
        self.vertex_colors = []
        for i in range(len(self.vertices)):
            self.vertex_colors.append(self.vertex_color)
        self.create_vbo(self.vertex_colors, 3, "vec3")
        self.translation = identity_mat()
        self.translation = rotate_around_axis(self.translation, init_rotation.angle, init_rotation.axis)
        self.translation = translate(self.translation, init_location.x, init_location.y, init_location.z)
        self.translation = scale(self.translation, init_scale.x, init_scale.y, init_scale.z)
        self.model_mat_uniform_location = glGetUniformLocation(self.rendering_program, "model_mat")
        self.mesh_name = ''
        self.is_selected_object = True

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

    def load_uniform(self, data, data_type, uniform_location):
        if data_type == "mat4":
            glUniformMatrix4fv(uniform_location, 1, GL_TRUE, data)

    def load_obj_file(self):
        with open(self.file_name) as fp:
            line = fp.readline()
            while line:
                if line[:2] == "v ":
                    vx, vy, vz, = [float(value) for value in line[2:].split()]
                    self.vertices.append((vx, vy, vz))
                if line[:3] == "vn ":
                    nx, ny, nz = [float(value) for value in line[3:].split()]
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
        self.vertices = format_vertices(self.vertices, self.vertex_indices)
        self.normals = format_vertices(self.normals, self.normal_indices)
        self.uvs = format_vertices(self.uvs, self.uv_indices)
        self.create_vbo(self.vertices, 0, "vec3")
        self.create_vbo(self.normals, 1, "vec3")
        self.create_vbo(self.uvs, 2, "vec2")

    def translate_mesh(self, x, y, z):
        self.translation = translate(self.translation, x, y, z)

    def rotate_mesh(self, angle, axis):
        self.translation = rotate_around_axis(self.translation, angle, axis)

    def uniform_scale_mesh(self, s):
        self.translation = uniform_scale(self.translation, s)

    def draw(self):
        glUseProgram(self.rendering_program)
        self.load_uniform(self.translation, "mat4", self.model_mat_uniform_location)
        glBindVertexArray(self.vao)
        glDrawArrays(self.draw_type, 0, len(self.vertices))
        glBindVertexArray(0)

    def random_color(self):
        self.vertex_colors.clear()
        for i in range(len(self.vertices)):
            self.vertex_colors.append(pygame.Vector3(random.random(), random.random(), random.random()))
        self.create_vbo(self.vertex_colors, 3, "vec3")
