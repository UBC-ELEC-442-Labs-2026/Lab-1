import numpy as np
from differential_kin import differential_kin # using your jacobian generator
from scipy.interpolate import CubicSpline

# A typical cubic spline here would want pass through the inner workspace boundary
trajectory_points = [
    [0.5, 0.0, 0.2, 0.0],
    [-0.5, 0.0, 0.2, 5.0]
]

