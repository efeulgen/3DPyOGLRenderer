
from Engine.Scene import *
from OpenGL.GL import *


class TestScene(Scene):
    def __init__(self):
        super().__init__()

    def init(self):
        glClearColor(0.2, 0.2, 0.21, 1.0)

    def update(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


TestScene().main_loop()
