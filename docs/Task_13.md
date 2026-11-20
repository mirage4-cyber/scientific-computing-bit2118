# Task 13 – Interpolation

## 1. Mathematical Concept

The program uses hourly temperature measurements to estimate values at intermediate times. It compares linear interpolation with a cubic spline and plots the measured points and estimated curves.

## 2. Inputs and Mathematical Operation

Inputs are measured hours and temperatures, plus the target time. Linear interpolation connects neighboring observations with straight lines, while cubic spline interpolation uses smooth piecewise cubic polynomials.

## 3. Output and Interpretation

The estimated temperature at 10:30 is a value inferred from surrounding hourly measurements, not a direct sensor reading. The graph shows how the two interpolation methods pass between the known data points.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change one of the measured temperatures. The interpolated values around that time will change, and the shape of the fitted curves may also change.

## 5. Modified Real-World Case

**Application:** Estimating temperatures between hourly sensor readings.

A monitoring system can estimate more frequent temperature readings from sensors that record data only once per hour.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_13_interpolation.py`
