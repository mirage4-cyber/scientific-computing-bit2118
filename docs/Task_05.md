# Task 5 – Matrix Algebra and Matrix Operations

## 1. Mathematical Concept

The program stores the corners of a square as coordinate pairs. It creates rotation and scaling matrices, combines the transformations and multiplies the coordinates by the resulting transformation matrix.

## 2. Inputs and Mathematical Operation

Inputs are the square's coordinates, a rotation angle and horizontal and vertical scale factors. Matrix multiplication applies the transformations; the determinant describes the scaling effect on area.

## 3. Output and Interpretation

The transformed coordinates show the new positions of the square's corners after rotation and scaling. The determinant indicates how the transformation changes area, including whether orientation is reversed.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change the rotation angle from 45 degrees to 90 degrees. The shape will rotate further while its dimensions remain determined by the scale factors.

## 5. Modified Real-World Case

**Application:** Transforming 2-D computer graphics coordinates.

Computer graphics systems use matrix transformations to rotate, resize and position objects on a screen.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_05_matrix_algebra.py`
