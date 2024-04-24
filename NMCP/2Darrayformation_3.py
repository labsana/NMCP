# 2D array Formation
import numpy as np

# Input section: Matrices
M1 = np.array([[1, 4], [5, 6]])
M2 = np.array([[1, -4], [3, -2]])

# Output section: Matrices
# Matrix Addition
print("[M1] + [M2] =", M1 + M2)

# Matrix Subtraction
print("[M1] - [M2] =", M1 - M2)

# Matrix Multiplication
print("[M1] [M2] =", M1.dot(M2))

# Matrix Transpose
print("Transpose of [M1] =", M1.transpose())