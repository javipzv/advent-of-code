import numpy as np
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

def get_result(matrix):
    for i in range(matrix.shape[1] - 1):
        minimo = min(i, matrix.shape[1]-(i+2))
        submatrix = matrix[:, i-minimo:i+2+minimo]
        list_inverted = list(range(0, submatrix.shape[1]))
        inverse_submatrix = submatrix[:, list_inverted[::-1]]
        m = submatrix-inverse_submatrix
        all_zeros = not np.any(m)
        if all_zeros:
            return i+1, 0
    
    for i in range(matrix.shape[0] - 1):
        minimo = min(i, matrix.shape[0]-(i+2))
        submatrix = matrix[i-minimo:i+2+minimo, :]
        list_inverted = list(range(0, submatrix.shape[0]))
        inverse_submatrix = submatrix[list_inverted[::-1], :]
        m = submatrix-inverse_submatrix
        all_zeros = not np.any(m)
        if all_zeros:
            return i+1, 1

matrix = []
total = 0
for line in input:
    if line == "":
        matrix = np.hstack(matrix).reshape((len(matrix), len(matrix[0])))
        res = get_result(matrix)
        if res[1] == 0:
            total += res[0]
        else:
            total += 100*res[0]
        matrix = []
    else:
        line = line.replace(".", "0").replace("#", "1")
        matrix += [[int(n) for n in line]]

print(total)
    
