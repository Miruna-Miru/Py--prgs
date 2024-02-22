import numpy as np

# Define x1 and x2 as numpy arrays
x1 = np.array([1, -2, 1])
x2 = np.array([0, 1, 3, -2])

# Create a matrix A with x1 and x2 as rows
A = np.vstack([x1, x2])

# Calculate the null space of A
null_space = np.linalg.null_space(A)

# Print the basis vectors for S perp
print("Basis vectors for S perp:")
for vector in null_space.T:
    print(vector)