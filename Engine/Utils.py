
import numpy as np


def format_vertices(coordinates, triangles):
    all_triangles = []
    for t in range(0, len(triangles), 3):
        all_triangles.append(coordinates[triangles[t]])
        all_triangles.append(coordinates[triangles[t+1]])
        all_triangles.append(coordinates[triangles[t+2]])
    return np.array(all_triangles, np.float32)
