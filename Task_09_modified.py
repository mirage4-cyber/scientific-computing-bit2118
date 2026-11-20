import numpy as np
import matplotlib.pyplot as plt
from _helpers import finish

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: add one extra link between nodes A and D
nodes = ["A", "B", "C", "D"]
A = np.array([[0., 1., 1., 0.], [1., 0., 1., 1.], [1., 1., 0., 1.], [0., 1., 1., 0.]])
A_new = A.copy()
A_new[0, 3] = A_new[3, 0] = 1.0


def importance(M):
    vals, vecs = np.linalg.eig(M)
    k = np.argmax(np.real(vals))
    v = np.abs(np.real(vecs[:, k]))
    return np.real(vals[k]), v / v.sum()


val_old, c_old = importance(A)
val_new, c_new = importance(A_new)
print(f"Original: dominant eigenvalue {val_old:.4f}, importance {np.round(c_old, 4).tolist()}")
print(f"With A-D link: dominant eigenvalue {val_new:.4f}, importance {np.round(c_new, 4).tolist()}")

idx = np.arange(4)
plt.bar(idx - 0.2, c_old, 0.4, label="Original network")
plt.bar(idx + 0.2, c_new, 0.4, label="With extra A-D link")
plt.xticks(idx, nodes)
plt.ylabel("Importance (share of total)")
plt.title("Effect of adding one link")
plt.legend()
plt.grid(True, axis="y")
finish("task_09_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# PageRank for a tiny website with 5 pages. links[i] = pages that page i links to.
pages = ["Home", "News", "Shop", "Blog", "Contact"]
links = {0: [1, 2], 1: [2], 2: [0], 3: [2, 4], 4: [2]}
n = len(pages)
M = np.zeros((n, n))
for i, outs in links.items():
    for j in outs:
        M[j, i] = 1.0 / len(outs)       # column-stochastic link matrix
d = 0.85                                 # damping factor
G = d * M + (1 - d) / n * np.ones((n, n))

vals, vecs = np.linalg.eig(G)
k = np.argmax(np.real(vals))
rank_eig = np.abs(np.real(vecs[:, k]))
rank_eig /= rank_eig.sum()

rank = np.full(n, 1.0 / n)               # power iteration
for _ in range(100):
    rank = G @ rank

print(f"Dominant eigenvalue of the Google matrix: {np.real(vals[k]):.6f}")
for p, re, rp in zip(pages, rank_eig, rank):
    print(f"{p:<8} eigenvector rank = {re:.4f}, power iteration rank = {rp:.4f}")
print("Largest difference between the two methods:", np.max(np.abs(rank_eig - rank)))

plt.bar(pages, rank_eig)
plt.ylabel("PageRank (share of total)")
plt.title("PageRank of a five-page website")
plt.grid(True, axis="y")
finish("task_09_modified.png")
