# 2x2 Matrix Addition

def add_matrices(a, b):
    result = [
        [a[0][0] + b[0][0], a[0][1] + b[0][1]],
        [a[1][0] + b[1][0], a[1][1] + b[1][1]]
    ]
    return result

# Example usage:
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

sum_matrix = add_matrices(matrix1, matrix2)
print("Sum of matrices:")
for row in sum_matrix:
    print(row)