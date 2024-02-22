import numpy as np

# Define the pairs of vectors x and y
x_list = [np.array([3, 4]), np.array([3, 2]), np.array([2, 4, 3]), np.array([2, -5, 4])]
y_list = [np.array([1]), np.array([1, 1]), np.array([1, 1, 1]), np.array([1, 2, -1])]

# Loop over each pair of vectors
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    
    # Calculate the vector projection of x onto y
    p = (np.dot(x, y)/np.dot(y, y)) * y
    
    # Verify that p and x - p are orthogonal
    if np.dot(p, x - p) == 0:
        print(f"Pair {i+1}: p = {p}, x - p = {x-p} are orthogonal.")
    else:
        print(f"Pair {i+1}: p = {p}, x - p = {x-p} are not orthogonal.")