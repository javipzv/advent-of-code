with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

def next(i, j):
    if grid[i-1][j] == "|" or grid[i-1][j] == "F" or grid[i-1][j] == "7": 
        return (i-1, j)
    elif grid[i+1][j] == "|" or grid[i+1][j] == "L" or grid[i+1][j] == "J":
        return (i+1, j)
    elif grid[i][j+1] == "-" or grid[i][j+1] == "J" or grid[i][j+1] == "7":
        return (i, j+1)
    elif grid[i][j-1] == "-" or grid[i][j-1] == "L" or grid[i][j-1] == "F":
        return (i, j-1)

def create_path():
    for i in range(len(grid)-1):
        for j in range(len(grid[0])-1):
            if grid[i][j] == "S":
                starting_position = (i, j)

    a, b = next(starting_position[0], starting_position[1])
    c, d = next(a, b)
    path = [(a, b), (c, d)]

    i, j = c, d
    while (i, j) != (starting_position[0], starting_position[1]):
        if grid[i][j] == "|":
            if (i-1, j) == path[len(path)-2]:
                i, j = i+1, j
                path += [(i, j)]
            else:
                i, j = i-1, j
                path += [(i, j)]
        elif grid[i][j] == "-":
            if (i, j-1) == path[len(path)-2]:
                i, j = i, j+1
                path += [(i, j)]
            else:
                i, j = i, j-1
                path += [(i, j)]
        elif grid[i][j] == "7":
            if (i, j-1) == path[len(path)-2]:
                i, j = i+1, j
                path += [(i, j)]
            else:
                i, j = i, j-1
                path += [(i, j)]
        elif grid[i][j] == "J":
            if (i-1, j) == path[len(path)-2]:
                i, j = i, j-1
                path += [(i, j)]
            else:
                i, j = i-1, j
                path += [(i, j)]
        elif grid[i][j] == "F":
            if (i, j+1) == path[len(path)-2]:
                i, j = i+1, j
                path += [(i, j)]
            else:
                i, j = i, j+1
                path += [(i, j)]
        elif grid[i][j] == "L":            
            if (i-1, j) == path[len(path)-2]:
                i, j = i, j+1
                path += [(i, j)]
            else:
                i, j = i-1, j
                path += [(i, j)]
    return set([(starting_position[0], starting_position[1])] + path)

path = create_path()

import numpy as np
import matplotlib.pyplot as plt

g = np.empty((len(grid), len(grid[0])))
for x, y in path:
    g[x, y] = 1

plt.imshow(g)
plt.show()
