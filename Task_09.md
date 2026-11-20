# Task 9: Eigenvalues and Eigenvectors

**Program files:** `code/Task_09_eigenvalues.py` (original program) and `code/Task_09_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
A small computer network needs to identify which nodes are structurally most influential from their pattern of connections.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: the adjacency matrix of a four-node undirected network with links A–B, A–C, B–C, B–D and C–D. A 1 means the two nodes are linked.
- Operation: `np.linalg.eig()` finds the eigenvalues and eigenvectors. The largest eigenvalue and its eigenvector are selected, and the vector is made positive and scaled so its entries add to 1. This gives an importance score for each node. Finally Av = λv is checked.

## 3. Original output
```
Dominant eigenvalue: 2.561552812808829
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 1.5059797815742444e-15
```

![Original output graph](images/task_09_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The dominant eigenvalue is 2.5616. The importance scores are A = 0.2192, B = 0.2808, C = 0.2808 and D = 0.2192.
- B and C have three links each while A and D have two, so B and C are more important. A and D are equal because they are in symmetric positions.
- The verification error is about 10⁻¹⁵, so Av = λv holds to round-off accuracy.
- The bar chart shows B and C taller than A and D.

## 5. Changing a parameter (Requirement C)
- What I changed: I added one more link, between nodes A and D.
- New output:

```
Original: dominant eigenvalue 2.5616, importance [0.2192, 0.2808, 0.2808, 0.2192]
With A-D link: dominant eigenvalue 3.0000, importance [0.25, 0.25, 0.25, 0.25]
```

![Graph after the change](images/task_09_changed.png)

- What changed and why:
  - The dominant eigenvalue rose from 2.5616 to exactly 3.0000.
  - All four nodes now have importance 0.25. Every node is linked to every other node, so none is more influential than another.
  - For a network where every node has the same number of links, the dominant eigenvalue equals that number of links (3 here).
  - This shows that one extra link can change the importance of every node.

## 6. Modified real-world case (Requirement E)
- Scenario: PageRank for a tiny website of five pages. A page is important if important pages link to it.
- Assumptions:
  - Links: Home → News and Shop; News → Shop; Shop → Home; Blog → Shop and Contact; Contact → Shop.
  - A page splits its importance equally among the pages it links to.
  - A damping factor of 0.85 is used, meaning that 15 % of the time a visitor jumps to a random page.
  - The site and its links are made up for illustration.
- New input data: A 5 × 5 Google matrix G = 0.85·M + 0.15/5, where M holds the link shares. The importance is the eigenvector of G for eigenvalue 1, found with `np.linalg.eig` and also by 100 steps of power iteration.
- New output:

```
Dominant eigenvalue of the Google matrix: 1.000000
Home     eigenvector rank = 0.3585, power iteration rank = 0.3585
News     eigenvector rank = 0.1823, power iteration rank = 0.1823
Shop     eigenvector rank = 0.3864, power iteration rank = 0.3864
Blog     eigenvector rank = 0.0300, power iteration rank = 0.0300
Contact  eigenvector rank = 0.0428, power iteration rank = 0.0428
Largest difference between the two methods: 1.1657341758564144e-15
```

![Modified case graph](images/task_09_modified.png)

- Interpretation:
  - The ranking is Shop (0.3864), Home (0.3585), News (0.1823), Contact (0.0428) and Blog (0.0300).
  - Shop is top because all four other pages link to it. Home is second even though only one page links to it, because that page is Shop, which passes on all of its importance to Home.
  - Blog has no incoming links, so it only receives the baseline share of (1 − 0.85)/5 = 0.03, which is why it ranks last.
  - The dominant eigenvalue of G is 1, as it must be when the columns add to 1. The eigenvector and power-iteration methods agree to about 10⁻¹⁵.
  - Limitation: real web graphs have billions of pages, so only power iteration is practical, and the damping factor of 0.85 is a modelling choice.

## 7. Conclusion
The dominant eigenvector of a network matrix gives a score for how influential each node is, and it depends on the whole pattern of links, not just the number of links. Adding or removing a single link can change every score. In the PageRank example the same idea ranked web pages, and power iteration gave the same answer as the full eigenvalue calculation.
