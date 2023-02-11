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
        wood_mat = RenderingProgram("Engine/Shaders/DiffuseShader/diffuseShaderVert.txt",
                                    "Engine/Shaders/DiffuseShader/diffuseShaderFrag.txt",
                                    tex_file_name="Engine/Textures/Wood.jpg")
        marble_mat = RenderingProgram("Engine/Shaders/DiffuseShader/diffuseShaderVert.txt",
                                      "Engine/Shaders/DiffuseShader/diffuseShaderFrag.txt",
                                      tex_file_name="Engine/Textures/Marble.jpg")
        stone_mat = RenderingProgram("Engine/Shaders/DiffuseShader/diffuseShaderVert.txt",
                                     "Engine/Shaders/DiffuseShader/diffuseShaderFrag.txt",
                                     tex_file_name="Engine/Textures/Stone.jpg")
        default_mat = RenderingProgram("Engine/Shaders/DiffuseShader/diffuseShaderVert.txt",
                                       "Engine/Shaders/DiffuseShader/diffuseShaderFrag.txt")
        self.rendering_programs.append(wood_mat)  # 1
        self.rendering_programs.append(marble_mat)  # 2
        self.rendering_programs.append(stone_mat)  # 3
        self.rendering_programs.append(default_mat)  # 4
        self.camera = Camera(1280, 720, self.rendering_programs)
        self.camera_light = CameraLight(self.rendering_programs, self.camera)
        self.light_list.append(self.camera_light)

        dog = Mesh(self.rendering_programs[3], file_name="Engine/TestMeshes/Dog.obj", is_turntable=False)
        self.input_manager.active_object = dog
        self.mesh_list.append(dog)

    def update(self):
        super().update()
        self.camera.update()
        for light in self.light_list:
            light.update()
        for mesh in self.mesh_list:
            mesh.draw()


TestScene().main_loop()
