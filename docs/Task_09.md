# Task 9 – Eigenvalues and Eigenvectors

## 1. Mathematical Concept

The program represents connections between four network nodes using an adjacency matrix. It calculates eigenvalues and eigenvectors, selects the dominant eigenvector and normalizes its entries into relative importance scores.

## 2. Inputs and Mathematical Operation

The input is the network adjacency matrix. The main operation is eigenvalue decomposition, followed by selecting the eigenvector associated with the largest eigenvalue and normalizing its components.

## 3. Output and Interpretation

The dominant eigenvalue describes the strongest eigenvalue scale of the network matrix. The normalized eigenvector scores indicate relative structural influence of the nodes in this example.

**Output verification:** Run the listed Python program and insert its actual console output here. For tasks that produce a graph, include a screenshot of the graph and explain its main trend. Do not use estimated or invented output values.

## 4. Changing an Input or Parameter

Change the adjacency matrix by adding or removing a connection. The eigenvalues and node-importance scores may change because the network structure has changed.

## 5. Modified Real-World Case

**Application:** Identifying influential nodes in a small network.

Network analysis can use eigenvector-based scores to identify influential or highly connected nodes.

**Modified-case documentation:** Record the new input data, assumptions, actual output and interpretation after implementing the modified case in the Python program.

## Program File

`code/Task_09_eigenvalues_eigenvectors.py`
