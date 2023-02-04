
from Engine.Mesh import *


class Torus(Mesh):
    def __init__(self, rendering_program,
                 draw_type=GL_TRIANGLES,
                 file_name="Engine/PrimitiveMeshes/torus.obj",
                 vertex_color=pygame.Vector3(1, 1, 1),
                 init_location=pygame.Vector3(0, 0, 0),
                 init_rotation=Rotation(),
                 init_scale=pygame.Vector3(1, 1, 1)):
        super().__init__(rendering_program=rendering_program,
                         draw_type=draw_type,
                         file_name=file_name,
                         vertex_color=vertex_color,
                         init_location=init_location,
                         init_rotation=init_rotation,
                         init_scale=init_scale)
