import re
with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

class Matrix:
    def __init__(self, matrix, transposed_matrix):
        self.matrix = matrix
        self.transposed_matrix = transposed_matrix

def transpose(matrix: list[list]):
    new = []
    for i in range(len(matrix)):
        row = [x[i] for x in matrix]
        new += [row]
    return new

def delete_num(matrix: Matrix, num):
    for row in matrix.matrix:
        for element in row:
            if element == num:
                del row[row.index(element)]

    for row in matrix.transposed_matrix:
        for element in row:
            if element == num:
                del row[row.index(element)]
    return matrix

def check_empty_row(matrix: Matrix):
    winner = False
    for row in matrix.matrix:
        if not row:
            winner = True
    
    for row in matrix.transposed_matrix:
        if not row:
            winner = True
    
    return winner

def remaining_elements(matrix: Matrix):
    sum = 0
    for row in matrix.matrix:
        for num in row:
            sum += num
    return sum

round = list(map(int, lines[0].split(',')))
matrix_set = []
matrix = []

for i in range(2, len(lines)):
    if lines[i] == "":
        new_matrix = Matrix(matrix, transpose(matrix))
        matrix_set += [new_matrix]
        matrix = []
        continue
    line = list(map(int, re.findall("[0-9]+", lines[i])))
    matrix += [line]

found = False
for num in round:
    unwanted = set()
    for matriz in matrix_set:
        delete_num(matriz, num)
        if check_empty_row(matriz):
            if len(matrix_set) == 1:
                remaining = remaining_elements(matriz)
                print(remaining*num)
            unwanted.add(matriz)
    matrix_set = [x for x in matrix_set if x not in unwanted]