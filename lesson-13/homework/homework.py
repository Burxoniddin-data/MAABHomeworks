import numpy as np

# 1. Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)
print("Vector:", vector)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("3x3 Matrix:\n", matrix_3x3)

# 3. Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)

# 4. Create a 3x3x3 array with random values
random_array = np.random.random((3, 3, 3))
print("Random 3x3x3 Array:\n", random_array)

# 5. Create a 10x10 array with random values and find the min and max
random_matrix = np.random.random((10, 10))
print("Min:", random_matrix.min(), "Max:", random_matrix.max())

# 6. Create a random vector of size 30 and find the mean value
random_vector = np.random.random(30)
print("Mean Value:", random_vector.mean())

# 7. Normalize a 5x5 random matrix
random_matrix_5x5 = np.random.random((5, 5))
norm_matrix = (random_matrix_5x5 - random_matrix_5x5.min()) / (random_matrix_5x5.max() - random_matrix_5x5.min())
print("Normalized 5x5 Matrix:\n", norm_matrix)

# 8. Multiply a 5x3 matrix by a 3x2 matrix
matrix_a = np.random.random((5, 3))
matrix_b = np.random.random((3, 2))
product = np.dot(matrix_a, matrix_b)
print("Matrix Product:\n", product)

# 9. Compute the dot product of two 3x3 matrices
matrix_x = np.random.random((3, 3))
matrix_y = np.random.random((3, 3))
dot_product = np.dot(matrix_x, matrix_y)
print("Dot Product:\n", dot_product)

# 10. Find the transpose of a 4x4 matrix
matrix_4x4 = np.random.random((4, 4))
transpose_matrix = matrix_4x4.T
print("Transpose:\n", transpose_matrix)

# 11. Calculate the determinant of a 3x3 matrix
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)
print("Determinant:", determinant)

# 12. Compute the matrix product of A (3x4) and B (4x3)
matrix_A = np.random.random((3, 4))
matrix_B = np.random.random((4, 3))
matrix_product = np.dot(matrix_A, matrix_B)
print("Matrix A * Matrix B:\n", matrix_product)

# 13. Compute the matrix-vector product
matrix_3x3 = np.random.random((3, 3))
vector_3 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3, vector_3)
print("Matrix-Vector Product:\n", matrix_vector_product)

# 14. Solve the linear system Ax = b
A = np.random.random((3, 3))
b = np.random.random((3, 1))
x = np.linalg.solve(A, b)
print("Solution x:\n", x)

# 15. Find row-wise and column-wise sums of a 5x5 matrix
matrix_5x5 = np.random.random((5, 5))
row_sums = matrix_5x5.sum(axis=1)
col_sums = matrix_5x5.sum(axis=0)
print("Row-wise Sums:\n", row_sums)
print("Column-wise Sums:\n", col_sums)
