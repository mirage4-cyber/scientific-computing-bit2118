# Task 10 – Root Finding: Bisection and Fixed-Point Methods

## 1. Mathematical Concept

The program defines a nonlinear heat-balance function and estimates the temperature at which it becomes zero. It uses SciPy's bisection solver and a fixed-point iteration, then plots the function and its root.

## 2. Inputs and Mathematical Operation

The input is the heat-balance function and a bracketing interval for bisection. Fixed-point iteration uses a rearranged function and an initial temperature estimate. Both methods stop according to a numerical tolerance or iteration limit.

## 3. Output and Interpretation

The root represents the estimated equilibrium temperature where the model's heat balance is zero. The graph's intersection with the horizontal axis visually identifies the root.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change the initial temperature used by fixed-point iteration. The sequence of estimates and possibly the number of iterations will change, although a convergent iteration should approach the same fixed point.

## 5. Modified Real-World Case

**Application:** Finding an equilibrium temperature.

A thermal-control application can use root finding to estimate the temperature at which heat gained and heat lost balance.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_10_bisection_fixed_point.py`
