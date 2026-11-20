import numpy as np
import timeit

rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 100_000)

def loop_calculation():
    result = []
    for value in latency_ms:
        seconds = value / 1000
        result.append(seconds ** 2)
    return result

def vectorized_calculation():
    seconds = latency_ms / 1000
    return seconds ** 2

loop_time = timeit.timeit(loop_calculation, number=1)
vector_time = timeit.timeit(vectorized_calculation, number=10) / 10
result = vectorized_calculation()
print("First five squared latency values:", result[:5])
print(f"Loop: {loop_time:.5f} s")
print(f"Vectorized average: {vector_time:.5f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.2f}x")
