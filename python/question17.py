
"""17. Write a program to find product of two matrices."""


def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Number of columns in the first matrix should be equal to the number of rows in the second matrix."
    
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Product of matrices
print("\nProduct of matrices:")
print(multiply_matrices(matrix1, matrix2))