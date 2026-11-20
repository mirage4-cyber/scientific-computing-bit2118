# Task 3 – Mathematical Functions and Vectorization

## 1. Mathematical Concept

The program generates a large array of network latency readings in milliseconds. It converts the values to seconds and squares them using NumPy vectorized expressions, then compares the execution time with a Python loop.

## 2. Inputs and Mathematical Operation

The input is a generated array of one million latency values. The operations are division by 1000, squaring each value and timing the loop and vectorized implementations.

## 3. Output and Interpretation

The first values show the squared latency measurements in seconds squared. The timing comparison demonstrates how vectorized NumPy operations can process large numerical datasets efficiently.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change the number of generated readings or the range of latency values. Increasing the array size generally increases both execution times, while the vectorized approach is expected to remain more efficient for large arrays.

## 5. Modified Real-World Case

**Application:** Processing network latency measurements.

A network monitoring service can process millions of response-time measurements to identify patterns and calculate error-related metrics.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_03_mathematical_functions_vectorization.py`
