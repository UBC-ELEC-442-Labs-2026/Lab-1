import numpy as np
from differential_kin import differential_kin # using your jacobian generator
from scipy.interpolate import CubicSpline

#! This will probably need to be changed depending on the workspace avaliable
trajectory_points = [
    [-0.2, 0.0, 0.65, 0.0],
    [0.0, 0.7, 0.2, 3.0],
    [0.7, 0.0, 0.2, 6.0],
    [-0.5, -0.25, 0.3, 9.0]
]