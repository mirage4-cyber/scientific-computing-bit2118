# Task 3: Mathematical Functions and Vectorization

**Program files:** `code/Task_03_vectorization.py` (original program) and `code/Task_03_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
A network-monitoring system has one million latency measurements in milliseconds. Each one must be converted to seconds and squared for an error calculation. We compare a Python loop with a vectorized NumPy expression.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: 1,000,000 random latencies between 5 and 250 ms (generated with seed 42 so the run is repeatable).
- Operation: `seconds = latency_ms / 1000` and `squared = seconds ** 2`. The loop version does this one value at a time, while the vectorized version does it on the whole array in one expression. `timeit` measures how long each takes.

## 3. Original output
```
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.1173 s
Vectorized time: 0.0022 s
Approximate speed-up: 53.3x
```

![Original output graph](images/task_03_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The squared latencies are small numbers in s² (for example 0.0379 for the first reading), because latencies in seconds are fractions.
- The vectorized version gave the same answers much faster. The speed-up line in the output shows it was tens of times quicker than the loop, and often more than a hundred times in repeated runs. The exact figure changes from computer to computer and from run to run.
- The bar chart uses a log scale so that both bars can be seen. The loop bar is far taller than the vectorized one.
- The reason is that NumPy runs the repeated arithmetic in compiled code, while the Python loop has to interpret every step.

## 5. Changing a parameter (Requirement C)
- What I changed: I changed the number of readings N to 10,000, 100,000 and 1,000,000 and measured both versions each time.
- New output:

```
N=   10,000: loop=0.00100 s, vectorized=0.000008 s, speed-up=125.0x
N=  100,000: loop=0.01064 s, vectorized=0.000069 s, speed-up=154.4x
N=1,000,000: loop=0.11507 s, vectorized=0.001112 s, speed-up=103.5x
```

![Graph after the change](images/task_03_changed.png)

- What changed and why:
  - The loop time grows roughly in proportion to N: about ten times more data takes about ten times longer.
  - The vectorized time also grows with N but stays far lower at every size, so vectorization wins by a large factor each time.
  - The speed-up ratio is not identical for each size because very small timings are noisy and depend on the computer's cache and other running programs.
  - Vectorization matters more as the data gets bigger, because the absolute time saved grows with N.

## 6. Modified real-world case (Requirement E)
- Scenario: Soil-moisture sensors send 500,000 readings. A reading is flagged as an outlier when it is more than 3 standard deviations from the mean (|z| > 3). The check is done with a loop and with vectorized NumPy.
- Assumptions:
  - Normal readings follow a normal distribution with mean 35 % and standard deviation 5 %.
  - 50 readings are faulty spikes, each pushed 40 percentage points up or down.
  - The mean and standard deviation are computed from all the readings, including the faults.
  - The data are simulated (seed 42), not measured.
- New input data: 500,000 simulated soil-moisture readings with 50 injected spikes.
- New output:

```
Readings: 500,000, mean=35.01 %, std=5.01 %
Outliers found (|z| > 3): 1336
Loop and vectorized results identical: True
Loop time: 0.0650 s, vectorized time: 0.00102 s, speed-up: 63.9x
```

![Modified case graph](images/task_03_modified.png)

- Interpretation:
  - The loop and vectorized versions found exactly the same outliers (`Loop and vectorized results identical: True`), so vectorizing did not change the answer, only the speed.
  - The vectorized version was again tens of times faster.
  - More outliers were found than the 50 spikes we injected. This is expected: in normal data about 0.27 % of readings are naturally more than 3 standard deviations from the mean, which is about 1,350 of 500,000. So |z| > 3 flags unusual readings, not necessarily faulty ones.
  - Limitation: the spikes also slightly inflate the mean and standard deviation, which is why robust methods (such as the median) are sometimes used.

## 7. Conclusion
Vectorization applies a mathematical operation to a whole array at once and gives the same results as a loop with far less run time, and the advantage holds as the data grows. In the outlier example it also made the code shorter and easier to read. A limitation is that timing results depend on the computer, so the speed-up should be quoted as approximate.
