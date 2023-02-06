
import pygame
from OpenGL.GL import *
from Engine.Transformations import *


class Light:
    def __init__(self, rendering_programs, light_index, init_position=pygame.Vector3(1, 1, 1), color=pygame.Vector3(1, 1, 1)):
        self.rendering_programs = rendering_programs
        self.light_index = light_index
        self.init_position = init_position
        self.color = color
        self.translation = identity_mat()
        self.translation = translate(self.translation, self.init_position[0], self.init_position[1], self.init_position[2])
        self.light_color_uniform_locations = []
        self.light_translation_uniform_locations = []
        for program in self.rendering_programs:
            if program.does_support_light:
                self.light_color_uniform_locations.append(glGetUniformLocation(program.rendering_program,
                                                                               "lightData[" + str(self.light_index) + "].color"))
                self.light_translation_uniform_locations.append(glGetUniformLocation(program.rendering_program,
                                                                                     "lightData[" + str(self.light_index) + "].translation"))
            else:
                self.light_translation_uniform_locations.append(0)
                self.light_color_uniform_locations.append(0)
        self.name = ''
        self.is_selected_object = False

    def translate(self, x, y, z):
        self.translation = translate(self.translation, x, y, z)

    def update(self):
        for i in range(len(self.rendering_programs)):
            if self.rendering_programs[i].does_support_light:
                glUseProgram(self.rendering_programs[i].rendering_program)
                glUniform3f(self.light_color_uniform_locations[i], self.color[0], self.color[1], self.color[2])
                glUniformMatrix4fv(self.light_translation_uniform_locations[i], 1, GL_TRUE, self.translation)
