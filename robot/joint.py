from pyrr import Quaternion, Matrix44, Vector3
import numpy as np

class Joint():
    def __init__(self, length, direction, is_fixed, is_base, position, parent):
        self.is_fixed = is_fixed
        self.length = length
        self.direction = direction
        self.position = position # relative if not base
        self.is_base = is_base
        self.parent = parent
        self.rotation = Quaternion()
        print(self.rotation)

    def get_endpoint(self):
        return self.position + self.direction * self.length