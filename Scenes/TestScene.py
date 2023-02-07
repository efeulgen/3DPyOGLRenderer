import pygame

from Engine.Scene import *
from Engine.Mesh import *
from Engine.RenderingProgram import *
from Engine.Camera import *
from Engine.Light import *
from Engine.CameraLight import *


class TestScene(Scene):
    def __init__(self):
        super().__init__()

    def init(self):
        super().init()
        self.rendering_programs.append(RenderingProgram("Engine/Shaders/DiffuseShader/diffuseShaderVert.txt",
                                                        "Engine/Shaders/DiffuseShader/diffuseShaderFrag.txt"))
        self.camera = Camera(1280, 720, self.rendering_programs)
        self.camera_light = CameraLight(self.rendering_programs, self.camera)
        self.light_list.append(self.camera_light)

        dog = Mesh(self.rendering_programs[1].rendering_program, file_name="Engine/TestMeshes/Dog.obj")
        self.mesh_list.append(dog)

    def update(self):
        super().update()
        self.camera.update()
        for light in self.light_list:
            light.update()
        for mesh in self.mesh_list:
            mesh.draw()


TestScene().main_loop()
