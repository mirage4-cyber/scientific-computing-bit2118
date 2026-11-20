# Task 7 – Gaussian Elimination and LU Decomposition

## 1. Mathematical Concept

The program factors a coefficient matrix once using LU decomposition and reuses the factors to solve several systems with different measurement vectors. It also compares a result with a direct NumPy solution.

## 2. Inputs and Mathematical Operation

Inputs are a square coefficient matrix and several right-hand-side measurement vectors. LU factorization expresses the matrix as lower and upper triangular factors, which are then used for forward and backward solution steps.

## 3. Output and Interpretation

Each solution vector contains the unknown values corresponding to one measurement set. Small residual norms indicate that the solutions satisfy the original systems.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change one measurement vector while keeping the coefficient matrix fixed. The solution for that measurement set changes, but the LU factorization can be reused.

## 5. Modified Real-World Case

**Application:** Repeated engineering measurement calculations.

Engineering simulations often solve many systems with the same physical coefficients but updated measurements, making reusable LU factors useful.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_07_gaussian_elimination_lu.py`
