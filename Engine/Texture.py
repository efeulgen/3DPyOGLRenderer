
import pygame.image
from OpenGL.GL import *


class Texture:
    def __init__(self, file_name):
        self.surface = pygame.image.load(file_name)
        self.pixel_data = pygame.image.tostring(self.surface, "RGBA", True)
        self.texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.surface.get_width(), self.surface.get_height(), 0, GL_RGBA,
                     GL_UNSIGNED_BYTE, self.pixel_data)
        glGenerateMipmap(GL_TEXTURE_2D)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
