# Task 4 – Floating-Point Arithmetic and Numerical Errors

## 1. Mathematical Concept

The program compares 0.1 + 0.2 with 0.3, calculates absolute and relative error for an approximation of the square root of two, and compares direct and numerically stable expressions.

## 2. Inputs and Mathematical Operation

Inputs include decimal values, the approximation 1.414 and several small x values. Operations include floating-point addition, absolute error, relative error and tolerance-based comparison.

## 3. Output and Interpretation

The exact comparison can be false because decimal fractions may not have exact finite binary representations. A tolerance-based comparison treats sufficiently close values as equal. The error calculations measure the difference between the approximation and the reference value.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change the approximation from 1.414 to 1.4142. The absolute and relative errors will decrease because the approximation is closer to the square root of two.

## 5. Modified Real-World Case

**Application:** Reliable numerical comparisons.

Financial, navigation and engineering software should account for finite precision rather than relying on exact equality for calculated decimal values.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_04_floating_point_errors.py`
