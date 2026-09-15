# Lab 1

This repo contains the code and documents needed to complete Lab 1.

## Important Notes

- If you are running this on your own computer, make sure to also clone `lab-machine-env` and edit the values in `constants.py` to reflect your file paths. The main one is in

- The Quanser "QArmKeyboardNavigator" has a bug, if you run an error message involving following:
    ```
    ee_position, ee_rotation, gamma = self.armMath.forward_kinematics(phi=initialPose)
    ValueError: not enough values to unpack (expected 3, got 2)
    ```
    The bug is that the forward_kinematics function only outputs 2 values. Simple go to the file (...\Quanser\0_libraries\python\hal\products\qarm.py, line 343) and delete `gamma`, then define it as 0 on the line below.