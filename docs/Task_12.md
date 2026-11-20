# Task 12 – Polynomial and Nonlinear Equation Solving

## 1. Mathematical Concept

The program defines two nonlinear equations representing a circle and a parabola. SciPy's root solver searches for coordinate pairs where both equations are satisfied, using different initial guesses.

## 2. Inputs and Mathematical Operation

The unknowns are x and y. The equations are the circle residual x² + y² - 4 and the parabola residual y - (x² - 1). The solver adjusts the two unknowns until both residuals are close to zero.

## 3. Output and Interpretation

Each converged coordinate pair represents an intersection point of the two curves. Residuals close to zero indicate that the point satisfies both equations.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change one initial guess. The solver may converge to a different intersection point or may require a different number of iterations; the final residuals should still be small for a valid solution.

## 5. Modified Real-World Case

**Application:** Finding the intersection of a circle and a parabola.

Geometric software can solve nonlinear equations to locate intersections between curves or shapes.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_12_polynomial_nonlinear_equations.py`
