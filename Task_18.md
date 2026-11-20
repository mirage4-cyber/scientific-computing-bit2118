# Task 18: Numerical Solution of ODEs Using SciPy

**Program files:** `code/Task_18_scipy_ode.py` (original program) and `code/Task_18_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
Model the voltage across a capacitor in an RC circuit as it charges over time.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: supply voltage Vs = 5 V, resistance R = 1000 Ω, capacitance C = 0.001 F, initial voltage 0 V, time interval 0 to 5 s, and solver tolerances rtol = 10⁻⁹ and atol = 10⁻¹¹.
- Operation: `solve_ivp` integrates dV/dt = (Vs − V)/(R·C) with automatically chosen step sizes. The result is compared with the exact charging curve V = Vs·(1 − e^(−t/RC)).

## 3. Original output
```
Solver success: True
Capacitor voltage at 5 s: 4.9663 V
Maximum error against exact solution: 9.282e-10 V
```

![Original output graph](images/task_18_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The solver reports success and the capacitor voltage after 5 s is 4.9663 V, very close to the 5 V supply.
- The maximum difference from the exact formula is about 9 × 10⁻¹⁰ V, so on the graph the two curves lie on top of each other.
- The curve rises steeply at first and then flattens. The time constant is RC = 1 s, so after 1 s the capacitor has reached about 63 % of the supply (3.16 V), and after 5 time constants it has reached 99.3 % (4.966 V).

## 5. Changing a parameter (Requirement C)
- What I changed: I doubled the capacitance from 0.001 F to 0.002 F, so the time constant RC became 2 s.
- New output:

```
C = 0.001 F (RC = 1 s): V(1 s) = 3.161 V, V(5 s) = 4.966 V, time to 63.2 % = 1.00 s
C = 0.002 F (RC = 2 s): V(1 s) = 1.967 V, V(5 s) = 4.590 V, time to 63.2 % = 2.00 s
```

![Graph after the change](images/task_18_changed.png)

- What changed and why:
  - After 1 s the voltage is 1.967 V instead of 3.161 V, and after 5 s it is 4.590 V instead of 4.966 V.
  - The time to reach 63.2 % of the supply went from 1.00 s to 2.00 s, exactly the new time constant.
  - A larger capacitor has to store more charge through the same resistor, so it takes longer to fill. The curve has the same shape but is stretched along the time axis.

## 6. Modified real-world case (Requirement E)
- Scenario: An epidemic on a university campus of 5,000 students, modelled with the SIR equations (Susceptible, Infected, Recovered).
- Assumptions:
  - The population is fixed at 5,000, mixes evenly, and has no births or deaths.
  - 5 students are infected on day 0. Students stay infectious for about 10 days (γ = 0.1 per day), and recovered students are immune.
  - Equations: S′ = −β·S·I/N, I′ = β·S·I/N − γ·I and R′ = γ·I.
  - Two contact rates are compared: β = 0.4 per day (normal) and β = 0.2 per day (reduced contact). The numbers are illustrative, not real data.
- New input data: N = 5000, initial state (S, I, R) = (4995, 5, 0), γ = 0.1, β = 0.4 and 0.2, simulated for 160 days.
- New output:

```
beta = 0.4 (normal contact): R0 = 4.0, peak infected = 2018 students on day 27.2, total ever infected = 4901 (98.0%)
beta = 0.2 (reduced contact): R0 = 2.0, peak infected = 770 students on day 67.6, total ever infected = 3971 (79.4%)
```

![Modified case graph](images/task_18_modified.png)

- Interpretation:
  - With β = 0.4 (R₀ = β/γ = 4) the infection peaks with 2,018 students infected at once on day 27, and 98.0 % of students are infected in total.
  - With β = 0.2 (R₀ = 2) the peak is much lower, 770 students, and later, on day 68, and 79.4 % are infected in total.
  - Halving the contact rate therefore lowers and delays the peak ("flattening the curve"), which matters because it reduces the pressure on health services, but it does not stop the epidemic on its own.
  - Limitation: the model assumes a constant contact rate, no incubation period and no change of behaviour over time, so it is only a simple illustration.

## 7. Conclusion
`solve_ivp` solves differential equations without us writing each step, and it matched the exact RC circuit solution to about 10⁻⁹ V. The same tool handled the three-equation SIR system where there is no simple exact formula. The results depend on the parameters, such as the time constant or contact rate, so these must be estimated carefully.
