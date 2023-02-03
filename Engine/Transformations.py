
import numpy as np
from math import *
import pygame


# ************************************************************************************
# ******************** classes *******************************************************

class Rotation:
    def __init__(self, angle=0, axis=pygame.Vector3(0, 1, 0)):
        self.angle = angle
        self.axis = axis


# ************************************************************************************
# ******************** transformation matrices ****************************************


def identity_mat():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]], np.float32)


def translation_mat(x, y, z):
    return np.array([[1, 0, 0, x],
                     [0, 1, 0, y],
                     [0, 0, 1, z],
                     [0, 0, 0, 1]], np.float32)


def rotate_x_mat(angle):
    c = cos(radians(angle))
    s = sin(radians(angle))
    return np.array([[1, 0, 0, 0],
                     [0, c, -s, 0],
                     [0, s, c, 0],
                     [0, 0, 0, 1]], np.float32)


def rotate_y_mat(angle):
    c = cos(radians(angle))
    s = sin(radians(angle))
    return np.array([[c, 0, s, 0],
                     [0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [0, 0, 0, 1]], np.float32)


def rotate_z_mat(angle):
    c = cos(radians(angle))
    s = sin(radians(angle))
    return np.array([[c, -s, 0, 0],
                     [s, c, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]], np.float32)


def rotate_around_axis_mat(angle, axis):
    c = cos(radians(angle))
    s = sin(radians(angle))
    u = axis.normalize()
    return np.array([[c + u.x**2 * (1 - c), u.x * u.y * (1 - c) - u.z * s, u.x * u.z * (1 - c) + u.y * s, 0],
                    [u.y * u.x * (1 - c) + u.z * s, c + u.y**2 * (1 - c), u.y * u.z * (1 - c) - u.x * s, 0],
                    [u.z * u.x * (1 - c) - u.y * s, u.z * u.y * (1 - c) + u.x * s, c + u.z**2 * (1 - c), 0],
                    [0, 0, 0, 1]], np.float32)


def scale_mat(x, y, z):
    return np.array([[x, 0, 0, 0],
                     [0, y, 0, 0],
                     [0, 0, z, 0],
                     [0, 0, 0, 1]], np.float32)


def uniform_scale_mat(s):
    return np.array([[s, 0, 0, 0],
                     [0, s, 0, 0],
                     [0, 0, s, 0],
                     [0, 0, 0, 1]], np.float32)


def perspective_mat(angle_of_view, aspect_ratio, near_plane, far_plane):
    a = radians(angle_of_view)
    d = 1.0 / tan(a/2)
    r = aspect_ratio
    b = (far_plane + near_plane) / (near_plane - far_plane)
    c = far_plane * near_plane / (near_plane - far_plane)
    return np.array([[d/r, 0, 0, 0],
                    [0, d, 0, 0],
                    [0, 0, b, c],
                    [0, 0, -1, 0]], np.float32)


# ************************************************************************************
# ******************** transformation methods ****************************************


def translate(matrix, x, y, z):
    return matrix @ translation_mat(x, y, z)


def rotate(matrix, angle, axis, local=True):
    rot = identity_mat()
    if axis == "X":
        rot = rotate_x_mat(angle)
    elif axis == "Y":
        rot = rotate_y_mat(angle)
    elif axis == "Z":
        rot = rotate_z_mat(angle)
    if local:
        return matrix @ rot
    else:
        return rot @ matrix


def rotate_around_axis(matrix, angle, axis, local=True):
    if local:
        return matrix @ rotate_around_axis_mat(angle, axis)
    else:
        return rotate_around_axis_mat(angle, axis) @ matrix


def scale(matrix, x, y, z):
    return matrix @ scale_mat(x, y, z)


def uniform_scale(matrix, s):
    return matrix @ uniform_scale_mat(s)
