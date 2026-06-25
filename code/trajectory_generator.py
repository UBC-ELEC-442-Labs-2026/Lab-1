import numpy as np
from scipy.interpolate import CubicSpline
import os
import sys
import constants
from pal.products.qarm import QArm
import time


directory_path = os.path.dirname(constants.path_to_interface)

if directory_path not in sys.path:
    sys.path.append(directory_path)

from QArm_functions import QArm_Lab_interface


#! convert to a starting joint value
trajectory_points = [
    # [X, Y, Z, Target Time (seconds)]
    [0.5, 0.4, 0.45, 0.0],
    [0.5, -0.4, 0.45, 6.0]
]

#TODO: Travel from the first to the second waypoint using cublic spline trajectory generation through task space and differential kinematics (expect integration error)

# Use the following helper functions
# QArm_Interface.write_to_arm(joint_positions, gripper)

mode = "-1"
while(int(mode) != 0 and int(mode) != 1):
    mode = input("Enter 1 for real hardware, 0 for simulation: ")

with QArm(hardware=int(mode), readMode=0) as myArm:
    QArm_Interface = QArm_Lab_interface(myArm)
    #QArm_Interface.write_to_arm(joint_positions, gripper)
    time.sleep(4)