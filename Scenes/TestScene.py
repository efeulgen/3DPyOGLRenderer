import pygame

from Engine.Scene import *
from Engine.Mesh import *
from Engine.RenderingProgram import *
from Engine.Camera import *
from Engine.Light import *


class TestScene(Scene):
    def __init__(self):
        super().__init__()

    def init(self):
        glClearColor(0.1, 0.1, 0.11, 1.0)
        self.rendering_programs.append(RenderingProgram("Engine/Shaders/DiffuseShader/diffuseShaderVert.txt",
                                                        "Engine/Shaders/DiffuseShader/diffuseShaderFrag.txt"))
        self.camera = Camera(1280, 720, self.rendering_programs)
        dog = Mesh(self.rendering_programs[1].rendering_program, file_name="Engine/TestMeshes/Dog.obj")
        # dog.random_color()
        self.mesh_list.append(dog)
        '''
        self.light_list.append(Light(self.rendering_programs, 0,
                                     init_position=pygame.Vector3(5, 5, 5),
                                     color=pygame.Vector3(1.0, 1.0, 0.0)))
        self.light_list.append(Light(self.rendering_programs, 1,
                                     init_position=pygame.Vector3(-5, 5, 5),
                                     color=pygame.Vector3(1.0, 0.0, 1.0)))
        self.light_list.append(Light(self.rendering_programs, 2,
                                     init_position=pygame.Vector3(5, 5, -5),
                                     color=pygame.Vector3(1.0, 0.0, 0.0)))
        self.light_list.append(Light(self.rendering_programs, 3,
                                     init_position=pygame.Vector3(-5, 5, -5),
                                     color=pygame.Vector3(0.0, 1.0, 0.0)))
        '''


    def update(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.camera.update()
        for light in self.light_list:
            light.update()
        for mesh in self.mesh_list:
            mesh.draw()


TestScene().main_loop()
