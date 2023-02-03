import pygame
import numpy as np
from OpenGL.GL import *
from math import *
from Engine.Transformations import *


class Camera:
    def __init__(self, width, height, rendering_programs):
        self.screen_width = width
        self.screen_height = height
        self.last_mouse = pygame.math.Vector2(0, 0)
        self.mouse_sensitivity_x = 0.1
        self.mouse_sensitivity_y = 0.1
        self.key_sensitivity = 0.05
        self.view_mat = identity_mat()
        self.projection_mat = perspective_mat(60, self.screen_width/self.screen_height, 0.01, 10000.0)
        self.rendering_programs = rendering_programs
        self.projection_mat_uniform_locations = []
        self.view_mat_uniform_locations = []
        for program in self.rendering_programs:
            self.projection_mat_uniform_locations.append(glGetUniformLocation(program.rendering_program, "projection_mat"))
            self.view_mat_uniform_locations.append(glGetUniformLocation(program.rendering_program, "view_mat"))

    def rotate(self, yaw, pitch):
        forward = pygame.Vector3(self.view_mat[0, 2], self.view_mat[1, 2], self.view_mat[2, 2])
        up = pygame.Vector3(0, 1, 0)
        angle = forward.angle_to(up)
        self.view_mat = rotate(self.view_mat, yaw, "Y", False)
        if angle < 170.0 and pitch > 0 or angle > 30.0 and pitch < 0:
            self.view_mat = rotate(self.view_mat, pitch, "X", True)

    def update(self):
        if pygame.mouse.get_visible():
            return
        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)
        pygame.mouse.set_pos(self.screen_width / 2, self.screen_height / 2)
        self.last_mouse = pygame.mouse.get_pos()
        self.rotate(mouse_change.x * self.mouse_sensitivity_x, mouse_change.y * self.mouse_sensitivity_y)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.view_mat = translate(self.view_mat, 0, 0, self.key_sensitivity)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.view_mat = translate(self.view_mat, 0, 0, -self.key_sensitivity)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.view_mat = translate(self.view_mat, self.key_sensitivity, 0, 0)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.view_mat = translate(self.view_mat, -self.key_sensitivity, 0, 0)
        if keys[pygame.K_e]:
            self.view_mat = translate(self.view_mat, 0, self.key_sensitivity, 0)
        if keys[pygame.K_q]:
            self.view_mat = translate(self.view_mat, 0, -self.key_sensitivity, 0)

        for i in range(len(self.rendering_programs)):
            glUseProgram(self.rendering_programs[i].rendering_program)
            glUniformMatrix4fv(self.view_mat_uniform_locations[i], 1, GL_TRUE, self.view_mat)
            glUniformMatrix4fv(self.projection_mat_uniform_locations[i], 1, GL_TRUE, self.projection_mat)
