# Task 2: NumPy Arrays and Numerical Computation

**Program files:** `code/Task_02_numpy_arrays.py` (original program) and `code/Task_02_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
A weather station records 24 hourly temperatures. We store them in one NumPy array, calculate the daily mean, minimum and maximum, and convert every value from Celsius to Fahrenheit.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: 24 hourly temperatures in °C, ranging from 17.5 to 29.4.
- Operations: `np.mean()`, `np.min()` and `np.max()` reduce the whole array to one number each. The conversion F = 1.8C + 32 is applied to all 24 values in one vectorized expression, with no loop.

## 3. Original output
```
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

![Original output graph](images/task_02_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The daily mean is 23.12 °C. The minimum is 17.50 °C (at 03:00) and the maximum is 29.40 °C (at 12:00).
- The graph shows the usual daily cycle: the temperature falls overnight to its lowest point at 03:00, climbs through the morning, peaks around midday and then cools again in the evening. The dashed line is the mean, and the curve is above it from about 07:00 to 18:00.
- The first Fahrenheit readings (65.3, 64.4, 64.04, ...) are just the Celsius readings stretched by 1.8 and shifted by 32, so the shape of the data does not change.

## 5. Changing a parameter (Requirement C)
- What I changed: I added 5 °C to the afternoon readings from 10:00 to 16:00 (seven values) to simulate a hot afternoon.
- New output:

```
Original: mean=23.12 C, min=17.50 C, max=29.40 C
Hot afternoon (+5 C, 10:00-16:00): mean=24.58 C, min=17.50 C, max=34.40 C
First six Fahrenheit readings (unchanged hours): [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

![Graph after the change](images/task_02_changed.png)

- What changed and why:
  - The mean rose from 23.12 °C to 24.58 °C. This is exactly what we expect: seven of the 24 readings went up by 5 °C, so the mean rises by 5 × 7 / 24 ≈ 1.46 °C.
  - The maximum rose from 29.40 °C to 34.40 °C, a full 5 °C, because the hottest reading is inside the changed period.
  - The minimum stayed at 17.50 °C and the first six Fahrenheit values did not change, because those early-morning readings were not touched.
  - This shows that each statistic responds differently to the same change in the data.

## 6. Modified real-world case (Requirement E)
- Scenario: An IoT water-tank level sensor sends one reading every hour. We use NumPy to summarise the day and to convert the level into litres.
- Assumptions:
  - The tank has a constant cross-section of 0.5 m², so 1 cm of water depth equals 5 litres.
  - The sensor readings are accurate and there are no missing values.
  - The tank is topped up by a pump, and a refill alert is set at 45 cm.
  - The 24 readings are illustrative values, not real measurements.
- New input data: 24 hourly water levels in cm, from 92 cm at midnight, falling during the day to 38 cm at 17:00, then rising back to 95 cm after a refill.
- New output:

```
Mean level: 70.79 cm (354 litres)
Lowest level: 38.0 cm (190 litres) at hour 17
Highest level: 95.0 cm at hour 20
Hours below the 45 cm alert level: 3 (hours [15, 16, 17])
```

![Modified case graph](images/task_02_modified.png)

- Interpretation:
  - The average level is 70.79 cm, which is about 354 litres.
  - The level falls steadily through the day as water is used. It drops below the 45 cm alert level for three hours (15:00, 16:00 and 17:00) and reaches its lowest point of 38 cm (190 litres) at 17:00.
  - The sharp rise between 18:00 and 20:00 shows the refill, after which the level stays near 92–95 cm.
  - Limitation: hourly readings could miss a short dip between two readings, and the 5 litres per cm only holds for a tank with straight vertical sides.

## 7. Conclusion
NumPy arrays let one expression act on every reading at once, so statistics and unit conversions need no loops. Changing part of the data changed the mean, maximum and minimum by different amounts, which can be predicted by reasoning about which readings were altered. The results are only as good as the sensor readings put into the array.
