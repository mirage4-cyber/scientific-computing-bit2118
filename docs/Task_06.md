# Task 6 – Solution of Systems of Linear Equations

## 1. Mathematical Concept

The program represents the CPU and memory requirements of two server types as a system of simultaneous linear equations. It solves the matrix equation Ax = b using NumPy and checks the solution by multiplying A by the result.

## 2. Inputs and Mathematical Operation

The coefficient matrix contains the CPU and memory use of each server type. The right-hand side contains the observed total CPU and memory usage. The unknown vector gives the number of each server type.

## 3. Output and Interpretation

The solution estimates how many servers of each type account for the observed resource totals. A zero or very small residual indicates that the calculated values satisfy the equations closely.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change the total CPU or memory usage in the right-hand-side vector. The estimated number of servers will change to satisfy the new resource totals, provided the system has a unique solution.

## 5. Modified Real-World Case

**Application:** Estimating active server types from resource usage.

A data centre can use simultaneous equations to estimate resource allocation when different machine types have known resource profiles.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_06_systems_of_linear_equations.py`
