# Task 19 – Numerical Optimization

## 1. Mathematical Concept

The program defines an objective function representing a cost or performance measure and uses a numerical optimizer to find parameter values that minimize or maximize it, subject to any specified bounds or constraints.

## 2. Inputs and Mathematical Operation

Inputs are the objective function, initial parameter estimates and optimization settings. The algorithm repeatedly evaluates candidate values and searches for a point with a better objective value.

## 3. Output and Interpretation

The result gives the parameter values found by the optimizer and the corresponding objective-function value. A successful status indicates that the solver met its convergence conditions; it does not automatically prove a global optimum.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change an input bound, starting guess or cost coefficient. The optimizer may find a different solution because the feasible region or objective function has changed.

## 5. Modified Real-World Case

**Application:** Reducing operating cost under constraints.

A cloud service provider can use optimization to allocate computing resources while balancing operating cost and service requirements.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_19_numerical_optimization.py`
