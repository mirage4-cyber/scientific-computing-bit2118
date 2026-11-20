# Task 20: Random Numbers and Monte Carlo Methods

**Program files:** `code/Task_20_monte_carlo.py` (original program) and `code/Task_20_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
Estimate the probability that a network server becomes overloaded when the incoming demand is uncertain.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: server capacity 1,000; demand that is normally distributed with mean 850 and standard deviation 120; N = 100,000 simulations; random seed 42 so the run is repeatable.
- Operation: generate N random demand values, mark each one where demand > capacity, and estimate the probability as overloaded cases / N. A running estimate is also plotted to show convergence.

## 3. Original output
```
Estimated overload probability: 10.6160%
Number of overload cases: 10616 out of 100000
```

![Original output graph](images/task_20_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The estimated overload probability is 10.6160 %, from 10,616 overloaded cases out of 100,000.
- This means about one scenario in ten exceeds the capacity. The capacity of 1,000 is only 1.25 standard deviations above the mean demand (150/120), which is why it is exceeded fairly often.
- The graph shows the running estimate swinging widely during the first hundred or so simulations, then settling close to 10.6 %.

## 5. Changing a parameter (Requirement C)
- What I changed: Change 1: I changed the number of simulations N from 100 to 1,000,000. Change 2: I raised the standard deviation of demand from 120 to 200.
- New output:

```
Exact overload probability (normal distribution, std 120): 10.5650%
N =       100: estimate = 2.0000%, error = 8.5650%
N =     1,000: estimate = 10.8000%, error = 0.2350%
N =    10,000: estimate = 10.6100%, error = 0.0450%
N =   100,000: estimate = 10.6080%, error = 0.0430%
N = 1,000,000: estimate = 10.5644%, error = 0.0006%
Std = 200, N = 100,000: estimate = 22.6530%, exact = 22.6627%
```

![Graph after the change](images/task_20_changed.png)

- What changed and why:
  - For this normal distribution the exact answer is 10.565 %. With N = 100 the estimate was 2.0 % (very wrong), with N = 1,000 it was 10.8 %, and with N = 1,000,000 it was 10.5644 %, an error of only 0.0006 %.
  - The error shrinks roughly like 1/√N, so each 100 times more simulations gives about 10 times less typical error. Individual runs can still be luckier or unluckier than this average.
  - With a standard deviation of 200, the estimate rose to 22.65 % (the exact value is 22.66 %). Capacity is now only 0.75 standard deviations above the mean, so overloads happen more than twice as often. More variable demand means more risk even when the average demand is the same.

## 6. Modified real-world case (Requirement E)
- Scenario: A matatu trip is made of three random parts. We estimate the chance that a trip takes longer than 45 minutes.
- Assumptions:
  - The three parts are independent: town traffic is normal with mean 15 min and standard deviation 3, the highway part is uniform between 10 and 20 min, and the stops are exponential with mean 8 min.
  - There are no breakdowns or road closures.
  - The distributions are chosen for illustration, not measured, and N = 200,000 simulated trips are used.
- New input data: Simulated trip time = traffic + highway + stops, repeated 200,000 times with seed 42.
- New output:

```
Simulated trips: 200,000
Mean trip time: 37.99 min, standard deviation: 9.02 min
95th percentile trip time: 55.04 min
Probability of taking longer than 45 minutes: 17.523% (standard error about 0.085%)
```

![Modified case graph](images/task_20_modified.png)

- Interpretation:
  - The mean trip time is 37.99 min (the three means add up to 15 + 15 + 8 = 38) with a standard deviation of 9.02 min.
  - The probability of a trip taking longer than 45 minutes is 17.52 % (standard error about 0.09 %), so roughly one trip in six is over the limit. The 95th percentile is 55.04 min, so one trip in twenty takes nearly an hour or more.
  - The histogram is skewed to the right because the exponential stops can occasionally be very long. This shape makes the answer hard to find by a formula but easy by simulation.
  - Limitation: the answer is only as good as the assumed distributions and independence, which should be checked against real trip data.

## 7. Conclusion
Monte Carlo methods estimate probabilities by simulating many random scenarios, and the estimate gets closer to the true value as the number of simulations grows. They are most useful when combining several random effects, where a formula would be difficult. The quality of the result depends on how realistic the assumed distributions are.
