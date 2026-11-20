# Task 16 – Numerical Integration

## 1. Mathematical Concept

The program uses power readings collected at regular time intervals to estimate the total electrical energy consumed. It applies the trapezoidal rule and Simpson's rule and compares the estimates.

## 2. Inputs and Mathematical Operation

Inputs are time values in hours and corresponding power values in kilowatts. Numerical integration approximates the area under the power-time curve; the resulting unit is kilowatt-hours.

## 3. Output and Interpretation

The integral estimates accumulated energy over the recorded period. A difference between the two methods reflects how their approximations represent the changing power curve.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change one or more power readings. The estimated total energy will change because the area under the power-time curve has changed.

## 5. Modified Real-World Case

**Application:** Estimating daily electrical energy consumption.

A smart meter can estimate household energy consumption by integrating power measurements collected throughout the day.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_16_numerical_integration.py`
