# Task 18 – Numerical Solution of ODEs Using SciPy

## 1. Mathematical Concept

The program defines a system whose state changes over time using an ordinary differential equation and solves it numerically with SciPy's solve_ivp function. It plots the computed solution over the selected time interval.

## 2. Inputs and Mathematical Operation

Inputs include the differential equation, initial condition, time interval and solver settings. solve_ivp advances the solution numerically and returns estimated state values at selected time points.

## 3. Output and Interpretation

The output values describe how the modelled quantity changes over time from its initial condition. The graph helps show whether the quantity increases, decreases, levels off or changes dynamically.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change the initial condition or a model parameter such as the growth, decay or reaction rate. The solution trajectory and its values over time will change.

## 5. Modified Real-World Case

**Application:** Simulating a changing physical or biological system.

SciPy's ODE solvers can simulate systems such as population changes, electrical circuits, chemical reactions and mechanical motion.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_18_scipy_ode.py`
