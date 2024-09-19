import numpy as np

k = 12
s = 0.02 * k

def gauss_method(matrix):
    n = len(matrix)
    aug_matrix = np.hstack((matrix, np.identity(n)))

    for i in range(n):
        max_row = np.argmax(abs(aug_matrix[i:, i])) + i
        aug_matrix[[i, max_row]] = aug_matrix[[max_row, i]]

        aug_matrix[i] = aug_matrix[i] / aug_matrix[i, i]

        for j in range(n):
            if i != j:
                aug_matrix[j] = aug_matrix[j] - aug_matrix[j, i] * aug_matrix[i]

    inverse_matrix = aug_matrix[:, n:]
    return inverse_matrix


matrix = np.array([
    [8.3, 2.62 + s, 4.1, 1.9],
    [3.92, 8.45, 7.78 - s, 2.46],
    [3.77, 7.21 + s, 8.04, 2.28],
    [2.21, 3.65 - s, 1.69, 6.69]
])

inverse_matrix = gauss_method(matrix)
print(inverse_matrix)
