
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Engine.Scene import *
from Engine.Mesh import *
from Engine.RenderingProgram import *
from Engine.Transformations import *
from Engine.Camera import *


vertex_shader_source = r'''
#version 330 core
layout(location=0) in vec3 pos;
uniform mat4 model_mat;
uniform mat4 view_mat;
uniform mat4 projection_mat;
void main()
{
    gl_Position = projection_mat * inverse(view_mat) * model_mat * vec4(pos, 1.0);
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


class TestScene(Scene):
    def __init__(self):
        super().__init__()
        self.rendering_programs = [RenderingProgram(vertex_shader_source, fragment_shader_source)]
        self.cube = None
        self.camera = None

    def init(self):
        glClearColor(0.1, 0.1, 0.11, 1.0)

        self.cube = Mesh(self.rendering_programs[0].rendering_program,
                         draw_type=GL_TRIANGLES,
                         file_name="PrimitiveMeshes/cube.obj",
                         init_location=pygame.Vector3(0, 0, 0),
                         init_rotation=Rotation(),
                         init_scale=pygame.Vector3(1, 1, 1))
        self.cube.create_vbo(self.cube.vertices, 0, "vec3")
        self.camera = Camera(1280, 720, self.rendering_programs)

    def update(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.cube.draw()
        self.camera.update()


TestScene().main_loop()
