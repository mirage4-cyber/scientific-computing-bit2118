# Task 16: Numerical Integration

**Program files:** `code/Task_16_numerical_integration.py` (original program) and `code/Task_16_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
A smart meter records power at regular intervals. We estimate the total electrical energy used over the 12 hours of readings.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: power readings [0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9] kW taken every 2 hours from t = 0 to t = 12 h.
- Operation: energy is the integral of power over time. The trapezoidal rule adds up trapezoids between readings, and Simpson's rule fits parabolas through groups of points.

## 3. Original output
```
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule: 15.800 kWh
Difference between estimates: 0.100 kWh
```

![Original output graph](images/task_16_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The trapezoidal rule gives 15.700 kWh and Simpson's rule gives 15.800 kWh, a difference of only 0.100 kWh (about 0.6 %).
- By hand, the trapezoidal rule gives 2 × (0.4 + 1.0 + 1.4 + 1.8 + 1.6 + 1.2 + 0.45) = 15.7 kWh.
- The shaded area under the power curve is the energy used. The peak demand is 1.8 kW at 06:00, and the average power over the 12 hours is about 1.3 kW.

## 5. Changing a parameter (Requirement C)
- What I changed: Change 1: I raised the 06:00 reading from 1.8 kW to 2.6 kW. Change 2: I kept only every second reading, so the sampling interval became 4 hours.
- New output:

```
Original: trapezoid = 15.700 kWh, Simpson = 15.800 kWh
Peak reading 1.8 -> 2.6 kW: trapezoid = 17.300 kWh, Simpson = 17.933 kWh
Sampling every 4 h ([0.0, 4.0, 8.0, 12.0]): trapezoid = 15.400 kWh, Simpson = 15.967 kWh
```

![Graph after the change](images/task_16_changed.png)

- What changed and why:
  - With the higher peak the energy rose to 17.300 kWh (trapezoid) and 17.933 kWh (Simpson). The trapezoid rule counts each interior reading with weight 2 h, so the extra 0.8 kW adds 1.6 kWh. Simpson's rule gives that reading a larger weight of 8/3 h, so it adds about 2.13 kWh.
  - With readings only every 4 hours the answers were 15.400 and 15.967 kWh, which differ from the original 15.7 and 15.8. The coarser sampling misses details of the curve, so the estimate depends on how often the readings are taken.
  - The two rules respond differently to the same change, so neither is exactly right when there are few points.

## 6. Modified real-world case (Requirement E)
- Scenario: Distance travelled by a vehicle, found from speed readings taken every 5 seconds for one minute.
- Assumptions:
  - The vehicle starts at rest and speeds up towards 20 m/s (72 km/h), following v(t) = 20·(1 − e^(−t/15)) m/s.
  - The speed readings are rounded to 2 decimals, as a real meter would.
  - The vehicle travels in a straight line. Because the true speed formula is known, the exact distance 20·(60 + 15·e^(−4) − 15) = 905.49 m can be used to check the numerical answers.
- New input data: 13 speed readings at t = 0, 5, 10, ..., 60 s.
- New output:

```
Readings: 13 speeds from t = 0 s to t = 60 s
Distance by trapezoidal rule: 902.72 m (error 2.77 m)
Distance by Simpson's rule: 905.42 m (error 0.08 m)
Exact distance: 905.49 m
Average speed over the minute: 15.09 m/s (54.3 km/h)
```

![Modified case graph](images/task_16_modified.png)

- Interpretation:
  - The trapezoidal rule gives 902.72 m (error 2.77 m) and Simpson's rule gives 905.42 m (error only 0.08 m). The exact distance is 905.49 m.
  - Simpson's rule is much more accurate here because the speed curve is smooth and curved. The trapezoid rule underestimates because straight lines lie below a curve that bends downward.
  - The average speed over the minute is 15.09 m/s, or about 54.3 km/h.
  - Limitation: both rules need evenly spaced readings and they work best for smooth data. Noisy or sudden changes in speed between readings would reduce the accuracy.

## 7. Conclusion
Numerical integration turns measured rates, such as power or speed, into accumulated quantities such as energy or distance. Simpson's rule was more accurate than the trapezoidal rule for smooth data, and both depend on how often the readings are taken. When the exact answer is known, comparing against it shows how accurate each rule really is.
