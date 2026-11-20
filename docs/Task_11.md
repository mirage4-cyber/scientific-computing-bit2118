# Task 11 – Root Finding: Newton-Raphson and Secant Methods

## 1. Mathematical Concept

The program defines net present value from a sequence of cash flows and estimates the interest rate at which NPV is zero. Newton-Raphson uses the derivative of NPV, while the secant method estimates the slope from two starting points.

## 2. Inputs and Mathematical Operation

Inputs are the initial investment, later cash inflows and initial rate guesses. The numerical operation is root finding applied to the NPV function.

## 3. Output and Interpretation

The calculated root is the estimated internal rate of return. An NPV close to zero confirms that the rate makes the discounted cash flows balance the initial investment.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change one of the annual cash inflows. The NPV function changes, so the estimated internal rate of return will generally change as well.

## 5. Modified Real-World Case

**Application:** Calculating a project's internal rate of return.

Businesses can use numerical root-finding methods to estimate the return rate that makes a proposed investment's net present value equal to zero.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_11_newton_raphson_secant.py`
