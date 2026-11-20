# Task 5: Matrix Algebra and Matrix Operations

**Program files:** `code/Task_05_matrix_algebra.py` (original program) and `code/Task_05_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
A graphics program needs to rotate and scale a set of 2-D points that make up an object. We use matrices so that every point is transformed in the same way.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: the four corners of a unit square, (0,0), (1,0), (1,1) and (0,1); a rotation of 45°; and a scaling matrix that stretches x by 2 and y by 1.5.
- Operation: build the rotation matrix R and scaling matrix S, combine them as T = R @ S (scale first, then rotate), and transform the points with `points @ T.T`. The determinant of T is also calculated.

## 3. Original output
```
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 2.9999999999999996
```

![Original output graph](images/task_05_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The transformation matrix is [[1.414, −1.061], [1.414, 1.061]]. The point (1, 0) becomes (1.414, 1.414): it is first stretched to (2, 0) and then rotated 45° anticlockwise.
- The determinant is 3.0, which equals 2 × 1.5. The determinant is the factor by which areas are multiplied, so the unit square (area 1) becomes a rectangle of area 3.
- The graph shows the original square and a larger rectangle tilted at 45° about the origin.

## 5. Changing a parameter (Requirement C)
- What I changed: I changed the rotation from 45° to 90° and the scaling from (2, 1.5) to (3, 1).
- New output:

```
Transformation matrix:
 [[ 0. -1.]
 [ 3.  0.]]
Transformed points:
 [[ 0.  0.]
 [ 0.  3.]
 [-1.  3.]
 [-1.  0.]]
Determinant: 3.0
```

![Graph after the change](images/task_05_changed.png)

- What changed and why:
  - The transformation matrix became [[0, −1], [3, 0]], and the corners moved to (0,0), (0,3), (−1,3) and (−1,0).
  - The shape is now a rectangle 1 unit wide and 3 units tall to the left of the origin. A 3 × 1 rectangle turned through 90° becomes 1 × 3.
  - The determinant is still 3.0 because the area is 3 × 1 = 3. Rotation never changes area, so only the scaling affects the determinant.

## 6. Modified real-world case (Requirement E)
- Scenario: A two-link robot arm lies in a plane. Given the two joint angles, we find where the elbow and the hand (end of the arm) are.
- Assumptions:
  - The first link is 0.5 m long and the second is 0.4 m long, both rigid.
  - The base is fixed at the origin. Joint angle θ1 = 40° is measured from the x-axis, and θ2 is measured relative to the first link.
  - Angles are positive anticlockwise, and the arm moves only in a flat plane.
  - We test θ2 = 0°, 30° and 60°.
- New input data: L1 = 0.5 m, L2 = 0.4 m, θ1 = 40°, θ2 = 0°, 30° and 60°. Hand position = R(θ1)·[L1, 0] + R(θ1+θ2)·[L2, 0].
- New output:

```
theta2 = 0: elbow=(0.383, 0.321) m, tip=(0.689, 0.579) m, reach=0.900 m (law of cosines: 0.900 m)
theta2 = 30: elbow=(0.383, 0.321) m, tip=(0.520, 0.697) m, reach=0.870 m (law of cosines: 0.870 m)
theta2 = 60: elbow=(0.383, 0.321) m, tip=(0.314, 0.715) m, reach=0.781 m (law of cosines: 0.781 m)
```

![Modified case graph](images/task_05_modified.png)

- Interpretation:
  - The elbow is at (0.383, 0.321) m in all three cases because only the second joint changes.
  - With θ2 = 0° the arm is fully stretched and the hand is 0.900 m from the base, which is L1 + L2. Bending the second joint to 30° and 60° pulls the hand in to reach 0.870 m and 0.781 m.
  - The matrix results agree with the law of cosines, √(L1² + L2² + 2·L1·L2·cos θ2), which is a good check.
  - Limitation: this only finds the hand position from known angles (forward kinematics). Finding the angles for a wanted position needs more work, and real joints have angle limits.

## 7. Conclusion
Matrix multiplication lets one combined matrix transform every point consistently, and the determinant tells how much areas change. Rotation matrices can also be chained to describe a robot arm. The order of multiplication matters, because scaling then rotating is not the same as rotating then scaling.
