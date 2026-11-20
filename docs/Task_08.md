# Task 8 – Iterative Methods for Linear Systems

## 1. Mathematical Concept

The program models temperatures at interior points between two fixed-temperature boundaries. It solves the system using Jacobi and Gauss-Seidel iteration, compares the results with a direct solution and plots the convergence history.

## 2. Inputs and Mathematical Operation

Inputs are the coefficient matrix, boundary influence vector, initial estimate, tolerance and maximum iteration count. Each method repeatedly updates the unknown temperatures until the maximum change is below the tolerance or the iteration limit is reached.

## 3. Output and Interpretation

The calculated values estimate the steady-state temperatures along the grid. The convergence graph shows how the maximum change decreases as iterations proceed. Faster reduction indicates faster convergence.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change the tolerance from 1e-8 to 1e-5. The method will usually stop earlier because a less precise solution is accepted.

## 5. Modified Real-World Case

**Application:** Steady-state temperature distribution.

The same iterative approach can estimate steady-state temperatures in a larger heat-transfer grid where direct factorization may be expensive.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_08_iterative_methods.py`
