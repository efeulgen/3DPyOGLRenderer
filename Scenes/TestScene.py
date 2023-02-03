
from Engine.Scene import *
from Engine.Mesh import *
from Engine.RenderingProgram import *
from Engine.Camera import *


class TestScene(Scene):
    def __init__(self):
        super().__init__()

    def init(self):
        glClearColor(0.1, 0.1, 0.11, 1.0)
        self.rendering_programs.append(RenderingProgram("Shaders/DiffuseShader/diffuseShaderVert.txt",
                                                        "Shaders/DiffuseShader/diffuseShaderFrag.txt"))
        self.camera = Camera(1280, 720, self.rendering_programs)
        dog = Mesh(self.rendering_programs[0].rendering_program,
                   file_name="PrimitiveMeshes/Dog.obj")
        dog.random_color()
        self.mesh_list.append(dog)

    def update(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.camera.update()
        for mesh in self.mesh_list:
            mesh.draw()


TestScene().main_loop()
