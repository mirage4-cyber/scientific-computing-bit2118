# Task 14: Curve Fitting and Approximation

**Program files:** `code/Task_14_curve_fitting.py` (original program) and `code/Task_14_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
Server response time is measured at different user loads. We estimate a mathematical relationship between load and response time.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: concurrent users [50, 100, 150, 200, 250, 300, 350] and response times [82, 95, 115, 145, 185, 238, 305] ms.
- Operation: `curve_fit` finds the parameters of the quadratic y = ax² + bx + c that minimise the sum of squared residuals Σ(y − ŷ)². The RMSE measures the typical size of the misfit.

## 3. Original output
```
Fitted model: y = 0.002167x^2 + -0.1345x + 85.00
RMSE: 1.55 ms
Predicted response at 400 users: 377.86 ms
```

![Original output graph](images/task_14_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The fitted model is y = 0.002167x² − 0.1345x + 85.00, and the RMSE is 1.55 ms, so on average the curve is within about 1.5 ms of each measurement.
- The positive x² term means that the delay grows faster and faster as more users arrive, which is what the graph shows.
- The model predicts about 378 ms at 400 users. That is outside the measured range (50 to 350 users), so it is an extrapolation and less reliable than the values inside the range.

## 5. Changing a parameter (Requirement C)
- What I changed: I changed the model: a straight line, the original quadratic and a cubic were all fitted to the same data.
- New output:

```
Linear: RMSE = 18.83 ms, prediction at 400 users = 312.86 ms
Quadratic (original): RMSE = 1.55 ms, prediction at 400 users = 377.86 ms
Cubic: RMSE = 0.14 ms, prediction at 400 users = 387.86 ms
```

![Graph after the change](images/task_14_changed.png)

- What changed and why:
  - The straight line fits badly (RMSE 18.83 ms), because the data curve upward and a line cannot follow that.
  - The quadratic gives an RMSE of 1.55 ms and the cubic 0.14 ms. A model with more parameters always fits at least as well, but it may start to follow measurement noise instead of the real trend.
  - The three models predict 312.86, 377.86 and 387.86 ms at 400 users. A difference of 75 ms between models shows that extrapolating beyond the data is uncertain and depends strongly on the model chosen.

## 6. Modified real-world case (Requirement E)
- Scenario: Growth of the monthly active users of a mobile app, modelled with an exponential growth curve.
- Assumptions:
  - Seven months of data: 120, 150, 190, 240, 300, 380 and 480 users in months 1 to 7 (invented for illustration).
  - Growth is proportional to the current number of users, so users = a·e^(b·month).
  - We compare it with a straight-line fit and predict months 10 and 12.
- New input data: months = 1 to 7 and users = [120, 150, 190, 240, 300, 380, 480]. Starting guess for the fit: a = 100, b = 0.2.
- New output:

```
Fitted model: users = 94.62 * exp(0.2318 * month)
Monthly growth rate: 26.09%
RMSE exponential = 0.78, RMSE straight line = 23.72
Prediction month 10: exponential = 961, straight line = 619
Prediction month 12: exponential = 1528, straight line = 737
```

![Modified case graph](images/task_14_modified.png)

- Interpretation:
  - The fitted model is users = 94.62·e^(0.2318·month), which is a growth of about 26.09 % per month.
  - The exponential fit has an RMSE of 0.78 users, against 23.72 for the straight line, so the growth is clearly exponential rather than linear.
  - The predictions differ a lot: 961 users in month 10 and 1,528 in month 12 from the exponential model, against 619 and 737 from the straight line.
  - Limitation: exponential growth cannot continue forever (the market gets saturated), so predictions far beyond the data are unreliable. The model must be chosen to suit the process.

## 7. Conclusion
Curve fitting chooses the parameters of a model so that it follows the data as closely as possible, and the RMSE tells how good the fit is. The choice of model matters more than the fitting itself, since a wrong model fits badly and different models can give very different predictions outside the data. A better fit on the data does not guarantee a better prediction.
