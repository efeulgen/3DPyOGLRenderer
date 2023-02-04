
from Engine.PrimitiveMeshes.Cube import *
from Engine.PrimitiveMeshes.Cylinder import *
from Engine.PrimitiveMeshes.Sphere import *
from Engine.PrimitiveMeshes.Torus import *


class InputManager:
    def __init__(self, mesh_list, rendering_programs):
        self.mesh_list = mesh_list
        self.rendering_programs = rendering_programs
        self.active_mesh = None
        self.user_input = ''

    def get_user_input(self):
        self.user_input = input("Enter input: ")
        if self.user_input == 'cube':
            self.mesh_list.append(Cube(self.rendering_programs[0].rendering_program))
            print("Cube created.")
        elif self.user_input == "cylinder":
            self.mesh_list.append(Cylinder(self.rendering_programs[0].rendering_program))
            print("Cylinder created.")
        elif self.user_input == "sphere":
            self.mesh_list.append(Sphere(self.rendering_programs[0].rendering_program))
            print("Sphere created.")
        elif self.user_input == "torus":
            self.mesh_list.append(Torus(self.rendering_programs[0].rendering_program))
        else:
            print("Invalid input.")
