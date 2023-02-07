
from Engine.Light import *


class CameraLight(Light):
    def __init__(self, rendering_programs,
                 attached_camera,
                 light_index=0,
                 init_position=pygame.Vector3(0, 0, 0),
                 color=pygame.Vector3(1, 1, 1)):
        super().__init__(rendering_programs=rendering_programs,
                         light_index=light_index,
                         init_position=init_position,
                         color=color)
        self.attached_camera = attached_camera
        self.name = 'CameraLight'

    def activate_cam_light(self):
        self.color = pygame.Vector3(1, 1, 1)

    def deactivate_cam_light(self):
        self.color = pygame.Vector3(0, 0, 0)

    def update(self):
        super().update()
        self.translation = self.attached_camera.view_mat
