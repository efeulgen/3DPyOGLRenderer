import pygame

from Engine.Scene import *
from Engine.Mesh import *
from Engine.RenderingProgram import *
from Engine.Camera import *
from Engine.Light import *
from Engine.CameraLight import *


class SkullScene(Scene):
    def __init__(self):
        super().__init__()

    def init(self):
        super().init()
        wood_mat = RenderingProgram("/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Engine/Shaders/DiffuseShader/diffuseShaderVert.txt",
                                    "/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Engine/Shaders/DiffuseShader/diffuseShaderFrag.txt",
                                    tex_file_name="/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Engine/Textures/Wood.jpg")
        marble_mat = RenderingProgram("/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Engine/Shaders/DiffuseShader/diffuseShaderVert.txt",
                                      "/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Engine/Shaders/DiffuseShader/diffuseShaderFrag.txt",
                                      tex_file_name="/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Engine/Textures/Marble.jpg")
        stone_mat = RenderingProgram("/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Engine/Shaders/DiffuseShader/diffuseShaderVert.txt",
                                     "/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Engine/Shaders/DiffuseShader/diffuseShaderFrag.txt",
                                     tex_file_name="/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Engine/Textures/Stone.jpg")
        default_mat = RenderingProgram("/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Engine/Shaders/DiffuseShader/diffuseShaderVert.txt",
                                       "/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Engine/Shaders/DiffuseShader/diffuseShaderFrag.txt")
        self.rendering_programs.append(wood_mat)  # 1
        self.rendering_programs.append(marble_mat)  # 2
        self.rendering_programs.append(stone_mat)  # 3
        self.rendering_programs.append(default_mat)  # 4
        self.camera = Camera(1280, 720, self.rendering_programs)
        self.camera_light = CameraLight(self.rendering_programs, self.camera)
        self.light_list.append(self.camera_light)

        skull_top = Mesh(self.rendering_programs[2], file_name="/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Scenes/SkullSceneMeshes/meshes/skull_top.obj", is_turntable=False)
        skull_bottom = Mesh(self.rendering_programs[2], file_name="/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Scenes/SkullSceneMeshes/meshes/skull_bottom.obj", is_turntable=False)
        teeth = Mesh(self.rendering_programs[2], file_name="/Users/efeulgen/Documents/GitHub/3DPyOGLRenderer/Scenes/SkullSceneMeshes/meshes/teeth.obj", is_turntable=False)
        self.mesh_list.append(skull_top)
        self.mesh_list.append(skull_bottom)
        self.mesh_list.append(teeth)

    def update(self):
        super().update()
        self.camera.update()
        for light in self.light_list:
            light.update()
        for mesh in self.mesh_list:
            mesh.draw()


SkullScene().main_loop()
