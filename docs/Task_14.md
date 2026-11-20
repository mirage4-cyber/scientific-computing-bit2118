# Task 14 – Curve Fitting and Approximation

## 1. Mathematical Concept

The program fits a mathematical model to measured server response times at different user loads using least-squares curve fitting. It compares the fitted model with the observed data and examines the fitted parameters.

## 2. Inputs and Mathematical Operation

Inputs are the measured user loads and response times, together with a selected model function. The fitting operation estimates model parameters by minimizing the sum of squared differences between observations and predictions.

## 3. Output and Interpretation

The fitted curve summarizes the relationship between user load and response time. Residuals represent the differences between measured values and model predictions; smaller residuals generally indicate a closer fit.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change one observed response-time value or add another measurement. The fitted parameters and curve may shift to reflect the changed dataset.

## 5. Modified Real-World Case

**Application:** Modelling server response time under increasing load.

System administrators can fit performance curves to load-test results and use them to estimate how response time may change as more users access a service.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_14_curve_fitting.py`
