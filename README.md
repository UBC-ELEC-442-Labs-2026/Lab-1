# Lab 1

This repo contains the code and documents needed to complete Lab 1. Requires `lab-machine-env`.

## Getting Started

Welcome to the first lab!

1. **[Personal Computer Software Installation](personal-software-installation.md)**  
   Install the software and Quanser dependencies required to run the labs on a personal Windows computer. Complete this first if you have not already set up your computer.

2. **[Personal Computer Setup](personal-computer-setup.md)**  
   Set up the Lab 1 repository, VS Code, Python interpreter, Git workflow, and submission process on your personal computer.
   - As of September 24, 2026 there remains a bug in the Quanser Academic Resources downloaded in step 1. You can fix it by reading the [bug fix](bug-fix.md).

3. **Lab Computer Quick Start**  
   Instructions for using the preconfigured computers during the in-person lab.  
   *This guide is still being prepared.*

## Bugs

- The Quanser "QArmKeyboardNavigator" has a bug, if you run an error message involving following:
    ```
    ee_position, ee_rotation, gamma = self.armMath.forward_kinematics(phi=initialPose)
    ValueError: not enough values to unpack (expected 3, got 2)
    ```
    The bug is that the forward_kinematics function only outputs 2 values. Simple go to the file (...\Quanser\0_libraries\python\hal\products\qarm.py, line 343) and delete `gamma`, then define it as 0 on the line below.