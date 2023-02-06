
import pygame
from Engine.Transformations import *
from OpenGL.GL import *


class Light:
    def __init__(self, rendering_programs, light_index, position=pygame.Vector3(1, 1, 1), color=pygame.Vector3(1, 1, 1)):
        self.rendering_programs = rendering_programs
        self.light_index = light_index
        self.position = position
        self.color = color
        self.light_pos_uniform_locations = []
        self.light_color_uniform_locations = []
        for program in self.rendering_programs:
            if program.does_support_light:
                self.light_pos_uniform_locations.append(glGetUniformLocation(program.rendering_program, "lightData[" + str(self.light_index) + "].position"))
                self.light_color_uniform_locations.append(glGetUniformLocation(program.rendering_program, "lightData[" + str(self.light_index) + "].color"))
            else:
                self.light_pos_uniform_locations.append(0)
                self.light_color_uniform_locations.append(0)

    def update(self):
        for i in range(len(self.rendering_programs)):
            if self.rendering_programs[i].does_support_light:
                glUseProgram(self.rendering_programs[i].rendering_program)
                glUniform3f(self.light_pos_uniform_locations[i], self.position[0], self.position[1], self.position[2])
                glUniform3f(self.light_color_uniform_locations[i], self.color[0], self.color[1], self.color[2])
