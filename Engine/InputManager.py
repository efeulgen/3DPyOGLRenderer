
from Engine.PrimitiveMeshes.Cube import *
from Engine.PrimitiveMeshes.Cylinder import *
from Engine.PrimitiveMeshes.Sphere import *
from Engine.PrimitiveMeshes.Torus import *


class InputManager:
    def __init__(self, mesh_list, rendering_programs):
        self.mesh_list = mesh_list
        self.rendering_programs = rendering_programs
        self.active_object = None
        self.user_input = ''

    def get_user_input(self):
        self.user_input = input("Enter input: ")
        # *************************************************************************
        # ******************** create mesh ****************************************
        # cube ********************************************************************
        if self.user_input == 'cube':
            if len(self.mesh_list) > 0:
                for mesh in self.mesh_list:
                    mesh.is_selected_object = False
            self.active_object = Cube(self.rendering_programs[1].rendering_program)
            self.active_object.mesh_name = 'Cube'
            self.mesh_list.append(self.active_object)
            num_of_cube = 0
            for mesh in self.mesh_list:
                if mesh.mesh_name[:4] == "Cube":
                    num_of_cube += 1
            if num_of_cube < 10:
                self.active_object.mesh_name = f'Cube_0{num_of_cube}'
            else:
                self.active_object.mesh_name = f'Cube_{num_of_cube}'
            print("Cube created.")
        # cylinder ********************************************************************
        elif self.user_input == "cylinder":
            if len(self.mesh_list) > 0:
                for mesh in self.mesh_list:
                    mesh.is_selected_object = False
            self.active_object = Cylinder(self.rendering_programs[1].rendering_program)
            self.active_object.mesh_name = 'Cylinder'
            self.mesh_list.append(self.active_object)
            num_of_cylinder = 0
            for mesh in self.mesh_list:
                if mesh.mesh_name[:8] == "Cylinder":
                    num_of_cylinder += 1
            if num_of_cylinder < 10:
                self.active_object.mesh_name = f'Cylinder_0{num_of_cylinder}'
            else:
                self.active_object.mesh_name = f'Cylinder_{num_of_cylinder}'
            print("Cylinder created.")
        # sphere ********************************************************************
        elif self.user_input == "sphere":
            if len(self.mesh_list) > 0:
                for mesh in self.mesh_list:
                    mesh.is_selected_object = False
            self.active_object = Sphere(self.rendering_programs[1].rendering_program)
            self.active_object.mesh_name = 'Sphere'
            self.mesh_list.append(self.active_object)
            num_of_sphere = 0
            for mesh in self.mesh_list:
                if mesh.mesh_name[:6] == "Sphere":
                    num_of_sphere += 1
            if num_of_sphere < 10:
                self.active_object.mesh_name = f'Sphere_0{num_of_sphere}'
            else:
                self.active_object.mesh_name = f'Sphere_{num_of_sphere}'
            print("Sphere created.")
        # torus ********************************************************************
        elif self.user_input == "torus":
            if len(self.mesh_list) > 0:
                for mesh in self.mesh_list:
                    mesh.is_selected_object = False
            self.active_object = Torus(self.rendering_programs[1].rendering_program)
            self.active_object.mesh_name = 'Torus'
            self.mesh_list.append(self.active_object)
            num_of_torus = 0
            for mesh in self.mesh_list:
                if mesh.mesh_name[:5] == "Torus":
                    num_of_torus += 1
            if num_of_torus < 10:
                self.active_object.mesh_name = f'Torus_0{num_of_torus}'
            else:
                self.active_object.mesh_name = f'Torus_{num_of_torus}'
            print("Torus created")
        # ****************************************************************************
        # ******************** selection *********************************************
        elif self.user_input[:6] == "select":
            for mesh in self.mesh_list:
                mesh.is_selected_object = False
                if mesh.mesh_name == self.user_input[7:]:
                    mesh.is_selected_object = True
                    self.active_object = mesh
        elif self.user_input == "print name":
            print(self.active_object.mesh_name)
        # ****************************************************************************
        # ******************** transformation ****************************************
        elif self.user_input[:9] == "translate":
            x, y, z = [float(value) for value in self.user_input[10:].split()]
            self.active_object.translate_mesh(x, y, z)
        elif self.user_input[:6] == "rotate":
            pass
        elif self.user_input[:5] == "scale":
            pass
        else:
            print("Invalid input.")
