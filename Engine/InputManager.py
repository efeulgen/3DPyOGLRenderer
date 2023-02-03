
from Engine.Mesh import *


class InputManager:
    def __init__(self, mesh_list, rendering_programs):
        self.mesh_list = mesh_list
        self.rendering_programs = rendering_programs
        self.active_mesh = None
        self.user_input = ''

    def get_user_input(self):
        self.user_input = input("Enter input: ")
        if self.user_input == 'cube':
            self.mesh_list.append(Mesh(self.rendering_programs[0].rendering_program, file_name="PrimitiveMeshes/cube.obj"))
        else:
            print("invalid input")
