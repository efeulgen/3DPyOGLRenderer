import pygame

from Engine.PrimitiveMeshes.Cube import *
from Engine.PrimitiveMeshes.Cylinder import *
from Engine.PrimitiveMeshes.Sphere import *
from Engine.PrimitiveMeshes.Torus import *
from Engine.Light import *


class InputManager:
    def __init__(self, mesh_list, light_list, rendering_programs):
        self.mesh_list = mesh_list
        self.light_list = light_list
        self.rendering_programs = rendering_programs
        self.active_object = None
        self.user_input = ''

    def get_user_input(self):
        self.user_input = input("Enter input: ")
        # **********************************************************************************
        # ******************** create mesh *************************************************
        # cube *****************************************************************************
        if self.user_input == 'cube':
            if len(self.mesh_list) > 0:
                for mesh in self.mesh_list:
                    mesh.is_selected_object = False
            self.active_object = Cube(self.rendering_programs[1])
            self.active_object.name = 'Cube'
            self.mesh_list.append(self.active_object)
            num_of_cube = 0
            for mesh in self.mesh_list:
                if mesh.name[:4] == "Cube":
                    num_of_cube += 1
            if num_of_cube < 10:
                self.active_object.name = f'Cube_0{num_of_cube}'
            else:
                self.active_object.name = f'Cube_{num_of_cube}'
            print("Cube created.")
        # cylinder ********************************************************************
        elif self.user_input == "cylinder":
            if len(self.mesh_list) > 0:
                for mesh in self.mesh_list:
                    mesh.is_selected_object = False
            self.active_object = Cylinder(self.rendering_programs[1])
            self.active_object.name = 'Cylinder'
            self.mesh_list.append(self.active_object)
            num_of_cylinder = 0
            for mesh in self.mesh_list:
                if mesh.name[:8] == "Cylinder":
                    num_of_cylinder += 1
            if num_of_cylinder < 10:
                self.active_object.name = f'Cylinder_0{num_of_cylinder}'
            else:
                self.active_object.name = f'Cylinder_{num_of_cylinder}'
            print("Cylinder created.")
        # sphere **********************************************************************
        elif self.user_input == "sphere":
            if len(self.mesh_list) > 0:
                for mesh in self.mesh_list:
                    mesh.is_selected_object = False
            self.active_object = Sphere(self.rendering_programs[1])
            self.active_object.name = 'Sphere'
            self.mesh_list.append(self.active_object)
            num_of_sphere = 0
            for mesh in self.mesh_list:
                if mesh.name[:6] == "Sphere":
                    num_of_sphere += 1
            if num_of_sphere < 10:
                self.active_object.name = f'Sphere_0{num_of_sphere}'
            else:
                self.active_object.name = f'Sphere_{num_of_sphere}'
            print("Sphere created.")
        # torus ***********************************************************************
        elif self.user_input == "torus":
            if len(self.mesh_list) > 0:
                for mesh in self.mesh_list:
                    mesh.is_selected_object = False
            self.active_object = Torus(self.rendering_programs[1])
            self.active_object.name = 'Torus'
            self.mesh_list.append(self.active_object)
            num_of_torus = 0
            for mesh in self.mesh_list:
                if mesh.name[:5] == "Torus":
                    num_of_torus += 1
            if num_of_torus < 10:
                self.active_object.name = f'Torus_0{num_of_torus}'
            else:
                self.active_object.name = f'Torus_{num_of_torus}'
            print("Torus created")
        # light ***********************************************************************
        elif self.user_input == "light":
            new_light = Light(self.rendering_programs, len(self.light_list),
                              init_position=pygame.Vector3(0, 5, 0),
                              color=pygame.Vector3(1, 1, 1))
            new_light.name = f'Light_0{len(self.light_list) + 1}'
            self.light_list.append(new_light)
            print("Light created.")
        # ****************************************************************************
        # ******************** selection *********************************************
        elif self.user_input[:6] == "select":
            mesh_found = False
            light_found = False
            for mesh in self.mesh_list:
                mesh.is_selected_object = False
                if mesh.name == self.user_input[7:]:
                    mesh_found = True
                    mesh.is_selected_object = True
                    self.active_object = mesh
                    print("Mesh selected.")
            if not mesh_found:
                for light in self.light_list:
                    light.is_selected_object = False
                    if light.name == self.user_input[7:]:
                        light_found = True
                        light.is_selected_object = True
                        self.active_object = light
                        print("Light selected.")
                if not light_found:
                    self.active_object.is_selected_object = True
                    print("Mesh or light not found")
        elif self.user_input == "print name":
            if self.active_object is not None:
                print(self.active_object.name)
            else:
                print("Active object not found")
        elif self.user_input == "print mesh list":
            for mesh in self.mesh_list:
                print(mesh.name)
        elif self.user_input == "print light list":
            for light in self.light_list:
                print(light.name)
        # ****************************************************************************
        # ******************** transformation ****************************************
        elif self.user_input[:9] == "translate":
            x, y, z = [float(value) for value in self.user_input[10:].split()]
            if self.active_object in self.mesh_list:
                self.active_object.translate_mesh(x, y, z)
            else:
                self.active_object.translate(x, y, z)
        elif self.user_input[:6] == "rotate":
            angle, axis_x, axis_y, axis_z = [float(value) for value in self.user_input[7:].split()]
            self.active_object.rotate_mesh(angle, pygame.Vector3(axis_x, axis_y, axis_z))
        elif self.user_input[:5] == "scale":
            sx, sy, sz = [float(value) for value in self.user_input[6:].split()]
            self.active_object.scale_mesh(sx, sy, sz)
        elif self.user_input == "print model matrix":
            print(self.active_object.translation)
        elif self.user_input == "clear model matrix":
            self.active_object.clear_transformations()
        # ****************************************************************************
        else:
            print("Invalid input.")
