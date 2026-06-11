import numpy as np

def differential_kin(phi):
    '''
    Implement a differential kinematics function for the QArm, generates the Jacobian

    Input:
        phi: the joint angles in radians, in order of base, shoulder, elbow, wrist

    Output:
        J: the Jacobian matrix
        J_inv: the inverse or psuedo inverse of the Jacobian
    '''

    # Replace these two definitions
    J = None
    J_inv = None

    return J, J_inv