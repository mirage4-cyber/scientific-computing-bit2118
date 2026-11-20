# Task 20 – Random Numbers and Monte Carlo Methods

## 1. Mathematical Concept

The program generates random samples and uses repeated trials to estimate a quantity that is difficult to calculate directly. The estimate is compared with a known or theoretical value where appropriate.

## 2. Inputs and Mathematical Operation

Inputs include the number of trials and a random-number generator seed. Monte Carlo estimation uses random sampling, counts outcomes of interest and divides the count by the total number of trials.

## 3. Output and Interpretation

The estimated probability or quantity is an approximation based on the generated sample. With more trials, the estimate will generally become more stable, although random variation remains.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Increase the number of simulations, for example from 10,000 to 100,000. The estimate will usually become more stable and its sampling variability will generally decrease.

## 5. Modified Real-World Case

**Application:** Estimating a probability or uncertain quantity.

Monte Carlo methods can estimate risk, reliability and probabilities in systems where exhaustive calculation is difficult.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_20_random_numbers_monte_carlo.py`
