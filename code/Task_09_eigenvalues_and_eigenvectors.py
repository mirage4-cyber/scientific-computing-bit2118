import numpy as np

# Undirected network adjacency matrix, nodes A-D
A = np.array([[0., 1., 1., 0.],
              [1., 0., 1., 1.],
              [1., 1., 0., 1.],
              [0., 1., 1., 0.]])
values, vectors = np.linalg.eig(A)
idx = np.argmax(values.real)
dominant_value = values[idx].real
scores = np.abs(vectors[:, idx].real)
scores /= scores.sum()
print("Dominant eigenvalue:", dominant_value)
for node, score in zip("ABCD", scores):
    print(f"Node {node} importance: {score:.4f}")
print("Verification norm:", np.linalg.norm(A @ vectors[:, idx] - dominant_value * vectors[:, idx]))

# Parameter variation: add an edge between A and D
A2 = A.copy(); A2[0, 3] = A2[3, 0] = 1
v2, w2 = np.linalg.eig(A2)
idx2 = np.argmax(v2.real)
score2 = np.abs(w2[:, idx2].real); score2 /= score2.sum()
print("Scores after adding A-D edge:", np.round(score2, 4))
