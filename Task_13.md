# Task 13: Interpolation

**Program files:** `code/Task_13_interpolation.py` (original program) and `code/Task_13_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
A sensor records the temperature every hour, but an application needs estimates every 10 minutes. We build interpolation functions from the hourly data and evaluate them at the in-between times.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: hourly times 8:00 to 14:00 and temperatures [18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0] °C; the target time 10:30; and evaluation times every 1/6 hour.
- Operation: `interp1d(kind="linear")` joins neighbouring points with straight lines, and `CubicSpline` joins them with smooth cubic curves.

## 3. Original output
```
Linear estimate at 10:30: 23.25 C
Cubic estimate at 10:30: 23.36 C
```

![Original output graph](images/task_13_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- At 10:30 the linear estimate is 23.25 °C, which is the average of 22.5 and 24.0, and the cubic estimate is 23.36 °C.
- The cubic value is slightly higher because the spline follows the trend of the data: the temperature is rising more slowly later in the day, so the curve bends.
- The graph shows the linear estimate as straight segments with corners at each reading, and the cubic spline as one smooth curve through the same points.
- Both curves pass exactly through the measured points. They only differ in between.

## 5. Changing a parameter (Requirement C)
- What I changed: I replaced the 10:00 reading (22.5 °C) with a wrong value of 28.0 °C, as if the sensor had made an error.
- New output:

```
Original: at 09:30 linear=21.25, cubic=21.32; at 10:30 linear=23.25, cubic=23.36; cubic maximum between readings=25.50 C
10:00 reading = 28.0: at 09:30 linear=24.00, cubic=25.07; at 10:30 linear=26.00, cubic=26.55; cubic maximum between readings=28.04 C
```

![Graph after the change](images/task_13_changed.png)

- What changed and why:
  - The linear estimates changed only in the two hours next to the bad point: 09:30 went from 21.25 to 24.00 and 10:30 from 23.25 to 26.00. Each is just the average of its two neighbours.
  - The cubic estimates changed by slightly larger amounts at 09:30 (21.32 to 25.07) and 10:30 (23.36 to 26.55), and the spline curve also bulges above the bad point, reaching 28.04 °C between readings against 25.50 °C before.
  - A spline is built from all the points together, so an error in one reading can distort the curve over a wider region, and it can overshoot the data.
  - Linear interpolation limits the damage to the neighbouring intervals and never overshoots.

## 6. Modified real-world case (Requirement E)
- Scenario: Calibrating a fuel-gauge sensor. The sensor gives a voltage, and a calibration table converts it to litres. Readings between the table values must be interpolated.
- Assumptions:
  - The table is accurate: 0.5 V = 0 L, 1.0 V = 4 L, 1.5 V = 9 L, 2.0 V = 16 L, 3.0 V = 31 L, 4.0 V = 43 L and 4.5 V = 48 L.
  - The tank holds 48 L at most, and readings stay between 0.5 V and 4.5 V, so there is no extrapolation.
  - The relationship is smooth but curved because the tank is not a simple box. The table values are invented.
  - We estimate the fuel at 1.2 V, 2.5 V and 3.6 V.
- New input data: Voltages [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 4.5] V and litres [0, 4, 9, 16, 31, 43, 48] L.
- New output:

```
Sensor 1.2 V: linear = 6.00 L, cubic = 5.79 L
Sensor 2.5 V: linear = 23.50 L, cubic = 23.67 L
Sensor 3.6 V: linear = 38.20 L, cubic = 38.59 L
Largest difference between the two methods over the table range: 0.42 L
```

![Modified case graph](images/task_13_modified.png)

- Interpretation:
  - At 1.2 V the estimates are 6.00 L (linear) and 5.79 L (cubic). At 2.5 V they are 23.50 L and 23.67 L, and at 3.6 V they are 38.20 L and 38.59 L.
  - The two methods never differ by more than 0.42 L over the whole table, which is under 1 % of the 48 L tank, so either would be acceptable for a fuel gauge.
  - The cubic spline follows the curved relationship better when the calibration is smooth, while linear interpolation is simpler and cannot overshoot.
  - Limitation: neither method can be trusted outside 0.5 V to 4.5 V, and both are only as accurate as the calibration table.

## 7. Conclusion
Interpolation estimates values between known measurements. Linear interpolation is simple and safe, while a cubic spline gives a smooth curve that fits well when the data are smooth. A wrong data point has a bigger and wider effect on the spline than on the linear estimate, so data should be checked before interpolating.
