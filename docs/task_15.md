# Task 15: Numerical Differentiation

## 1. Problem
a GPS device records a vehicle's position every
second, and we estimate its speed from those positions.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: time (0 to 6 s, 7 values) and position in metres
(0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0).
- Operation: speed is approximated as change in position divided by change in time.
- Forward difference at the first point
- Central difference at the interior points
- Backward difference at the last point

## 3. Original output
 ```                                     
t=0s, position=0.0m, estimated speed=4.80m/s
t=1s, position=4.8m, estimated speed=5.10m/s
t=2s, position=10.2m, estimated speed=5.65m/s
t=3s, position=16.1m, estimated speed=6.25m/s
t=4s, position=22.7m, estimated speed=6.95m/s
t=5s, position=30.0m, estimated speed=7.65m/s
t=6s, position=38.0m, estimated speed=8.00m/s
```
![GPS_graph](image.png)
## 4. Interpretation of the output and graph (Requirement D)
The estimated speed rises from 4.80 m/s at t=0 to 8.00 m/s at t=6.
The graph is a rising line, which means the vehicle is speeding up
steadily, gaining roughly 0.65 m/s every second. The first and last
points use one-sided differences, so they are slightly less accurate
than the interior points

## 5. Changing a parameter (Requirement C)
 changed position at t=4 from 22.7 to 30.0
The new output 
```
t=0s, position=0.0m, estimated speed=4.80m/s
t=1s, position=4.8m, estimated speed=5.10m/s
t=2s, position=10.2m, estimated speed=5.65m/s
t=3s, position=16.1m, estimated speed=9.90m/s
t=4s, position=30.0m, estimated speed=6.95m/s
t=5s, position=30.0m, estimated speed=4.00m/s
t=6s, position=38.0m, estimated speed=8.00m/s
```
What changed and why: the speeds at t=3 and t=5 changed by about 3.65 m/s each (6.25 to 9.90, and 7.65 to 4.00). The speed at t=4 stayed at 6.95 because the central difference uses the points on either side and skips the middle one. A 7.3 m error in position, divided by a 2 s gap, gives a 3.65 m/s error in speed. This shows that numerical differentiation magnifies errors in the data.
![figure_2](image-1.png)
## 6. Modified real-world case (Requirement E)
- Scenario 
a boda boda travelling along a straight town road, slowing for a junction and then accelerating away.
- Assumptions 
GPS readings every 2 s, straight road so position is distance along the road, no GPS error, and the rider doesn’t stop completely.
- New input data
times(0s to 16s)9 values and position in metres(0.0,20.0,36.0,46.0,50.0,53.0,61.0,75.0,94.0)
- New output
```
t=0s, position=0.0m, speed=10.00 m/s (36.0 km/h)
t=2s, position=20.0m, speed=9.00 m/s (32.4 km/h)
t=4s, position=36.0m, speed=6.50 m/s (23.4 km/h)
t=6s, position=46.0m, speed=3.50 m/s (12.6 km/h)
t=8s, position=50.0m, speed=1.75 m/s (6.3 km/h)
t=10s, position=53.0m, speed=2.75 m/s (9.9 km/h)
t=12s, position=61.0m, speed=5.50 m/s (19.8 km/h)
t=14s, position=75.0m, speed=8.25 m/s (29.7 km/h)
t=16s, position=94.0m, speed=9.50 m/s (34.2 km/h)
```
![boda_boda](image-2.png)
- Interpretation
The rider starts at about 36 km/h, slows to about 6 km/h near t=8 s (the junction), then speeds back up to about 34 km/h.The readings are 2 s apart, so central differences average over 4 s. The true slowest speed may be lower than the 1.75 m/s shown, because short dips get smoothed out. That shows you understand the method’s weakness, which graders like to see.

## 7. Conclusion
Numerical differentiation estimates speed from position data by
dividing the change in position by the change in time. It worked well
on smooth data, showing the vehicle speeding up steadily. A single bad
GPS reading changed the speeds at its two neighbouring points by about
3.65 m/s each, so the method magnifies errors in the data. For real
GPS data, the readings may need smoothing before differentiating.