from pyrr import Quaternion, Matrix44, Vector3
import numpy as np

from robot.joint import Joint

# joint lengths
# all in mm
j1_l = 128
j2_l = 124
j3_l = 126

# important motor lengths
m1_l = 77
m2_l = 24

J0 = Joint(77, Vector3([0, 1, 0]), True, True, Vector3([0, 0, 0]), None)
J1 = Joint(128, Vector3([0, 1, 0]), False, False, Vector3([0, 0, 0]), J0)