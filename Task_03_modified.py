import numpy as np
import timeit
import matplotlib.pyplot as plt
from _helpers import finish

rng = np.random.default_rng(42)

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: number of latency readings N (10,000 / 100,000 / 1,000,000)
sizes = [10_000, 100_000, 1_000_000]
loop_times, vec_times = [], []
for n in sizes:
    data = rng.uniform(5, 250, n)

    def loop_version():
        out = []
        for v in data:
            out.append((v / 1000.0) ** 2)
        return out

    def vector_version():
        return (data / 1000.0) ** 2

    lt = min(timeit.repeat(loop_version, number=1, repeat=5))
    vt = min(timeit.repeat(vector_version, number=20, repeat=5)) / 20
    loop_times.append(lt)
    vec_times.append(vt)
    print(f"N={n:>9,}: loop={lt:.5f} s, vectorized={vt:.6f} s, speed-up={lt / vt:.1f}x")

plt.loglog(sizes, loop_times, marker="o", label="Python loop")
plt.loglog(sizes, vec_times, marker="o", label="NumPy vectorized")
plt.xlabel("Number of readings N")
plt.ylabel("Time (s)")
plt.title("Run time against data size")
plt.legend()
plt.grid(True, which="both")
finish("task_03_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# Soil-moisture sensors: flag readings more than 3 standard deviations from the mean.
n = 500_000
moisture = rng.normal(35.0, 5.0, n)            # percent
spike_positions = rng.choice(n, 50, replace=False)
moisture[spike_positions] += rng.choice([-1, 1], 50) * 40   # 50 faulty spikes
mean, std = moisture.mean(), moisture.std()


def loop_flags():
    return [abs((v - mean) / std) > 3 for v in moisture]


def vector_flags():
    return np.abs((moisture - mean) / std) > 3


lt = min(timeit.repeat(loop_flags, number=1, repeat=3))
vt = min(timeit.repeat(vector_flags, number=10, repeat=3)) / 10
same = np.array_equal(np.array(loop_flags()), vector_flags())

print(f"Readings: {n:,}, mean={mean:.2f} %, std={std:.2f} %")
print(f"Outliers found (|z| > 3): {vector_flags().sum()}")
print(f"Loop and vectorized results identical: {same}")
print(f"Loop time: {lt:.4f} s, vectorized time: {vt:.5f} s, speed-up: {lt / vt:.1f}x")

plt.bar(["Python loop", "NumPy vectorized"], [lt, vt])
plt.yscale("log")
plt.ylabel("Time (s, log scale)")
plt.title("Outlier detection on 500,000 soil-moisture readings")
plt.grid(True, axis="y")
finish("task_03_modified.png")
