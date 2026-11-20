# Task 19: Numerical Optimization

**Program files:** `code/Task_19_optimization.py` (original program) and `code/Task_19_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
A cloud service wants to choose how many units of two server types to use so that the operating cost is as low as possible while meeting a minimum processing capacity.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: cost per unit A = 12 and B = 18; capacity per unit A = 100 and B = 170; required capacity at least 1,000; both amounts must be zero or more; starting point (5, 3).
- Operation: `scipy.optimize.minimize` (SLSQP method) minimises 12x + 18y subject to 100x + 170y − 1000 ≥ 0. Because whole servers are needed in practice, a loop then tests whole-number combinations.

## 3. Original output
```
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution (cost, A, B, capacity): (108, 0, 6, 1020)
```

![Original output graph](images/task_19_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The optimizer succeeds and chooses 0 units of A and 5.882 units of B, with capacity exactly 1,000 and a minimum cost of 105.88.
- B is cheaper per unit of capacity (18/170 = 0.106 against 12/100 = 0.120), so the optimizer uses only B. The capacity is exactly 1,000 because extra capacity would only cost more money.
- With whole servers, the best answer is 6 units of B (capacity 1,020) at a cost of 108, slightly above the 105.88 optimum.
- The graph shows the feasible region above the capacity line, with the optimum at the corner where the line meets the B axis.

## 5. Changing a parameter (Requirement C)
- What I changed: I raised the cost of one Type B unit from 18 to 22, leaving everything else unchanged.
- New output:

```
Cost of B = 18: A = 0.000, B = 5.882, cost = 105.88; best whole-server answer (cost, A, B) = (108, 0, 6)
Cost of B = 22: A = 10.000, B = 0.000, cost = 120.00; best whole-server answer (cost, A, B) = (120, 10, 0)
```

![Graph after the change](images/task_19_changed.png)

- What changed and why:
  - The optimum jumped from "all B" to "all A": 10 units of A, 0 of B, at a cost of 120. The whole-server answer is also 10 units of A at 120.
  - B is now more expensive per unit of capacity (22/170 = 0.129) than A (0.120). The switch happens when the cost of B passes 12 × 170/100 = 20.4.
  - This shows that a small change in one input can move the optimum to a completely different corner of the feasible region.

## 6. Modified real-world case (Requirement E)
- Scenario: A farmer buys two fertiliser bags to meet nutrient needs at the lowest cost. This problem has two constraints.
- Assumptions:
  - The farm needs at least 60 kg of nitrogen and at least 40 kg of phosphorus.
  - Bag A has 12 kg nitrogen and 4 kg phosphorus and costs KES 2,500. Bag B has 6 kg nitrogen and 10 kg phosphorus and costs KES 3,200.
  - For the optimization, bags may be fractions. We then check whole bags by testing combinations.
  - The prices and contents are invented for illustration, and only these two nutrients matter.
- New input data: Minimise 2.5a + 3.2b (thousands of KES) subject to 12a + 6b ≥ 60 and 4a + 10b ≥ 40, with a, b ≥ 0. Starting point (5, 5).
- New output:

```
Optimization success: True
Bags of A: 3.750, bags of B: 2.500
Nitrogen supplied: 60.00 kg, phosphorus supplied: 40.00 kg
Minimum cost: KES 17,375
Best whole-bag answer (cost, A, B): (18900, 5, 2)
```

![Modified case graph](images/task_19_modified.png)

- Interpretation:
  - The optimum is 3.75 bags of A and 2.50 bags of B at a cost of KES 17,375. Both nutrient requirements are met exactly (60 kg and 40 kg).
  - The optimum sits where the two constraint lines cross. Buying only A (10 bags) would cost KES 25,000 and only B (10 bags) KES 32,000, so the mix is much cheaper.
  - With whole bags, the best choice is 5 bags of A and 2 of B at KES 18,900, which is KES 1,525 more than the ideal because bags cannot be split.
  - Limitation: in real life prices change, there are other nutrients, and a farmer may want more than the minimum.

## 7. Conclusion
Optimization finds the cheapest way to meet requirements, and the best answer usually lies where the constraints are exactly met. A small change in a cost can flip the optimum to a different corner of the feasible region. Requiring whole numbers (servers or bags) makes the true answer more expensive than the continuous optimum.
