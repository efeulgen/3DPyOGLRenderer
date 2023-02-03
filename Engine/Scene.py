import os
import pygame
from pygame.locals import *
from OpenGL.GL import *

from Engine.InputManager import *


class Scene:
    def __init__(self, screen_pos_x=100, screen_pos_y=100, screen_width=1280, screen_height=720):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_pos_x, screen_pos_y)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_size = self.screen_width, self.screen_height
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 32)
        self.screen = pygame.display.set_mode(self.screen_size, DOUBLEBUF | OPENGL)
        pygame.display.set_caption("PyOpenGL 3D Renderer")
        self.clock = pygame.time.Clock()
        glEnable(GL_DEPTH_TEST)

        self.rendering_programs = []
        self.mesh_list = []
        self.camera = None
        self.input_manager = InputManager(self.mesh_list, self.rendering_programs)

    def init(self):
        pass

    def update(self):
        pass

    def main_loop(self):
        self.init()
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_TAB:
                        self.input_manager.get_user_input()
                    if event.key == K_SPACE:
                        if pygame.event.get_grab():
                            pygame.event.set_grab(False)
                            pygame.mouse.set_visible(True)
                        else:
                            pygame.event.set_grab(True)
                            pygame.mouse.set_visible(False)
            # *****************************************************************************************************************************
            # *****************************************************************************************************************************
            self.update()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
