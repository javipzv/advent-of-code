import re
import numpy as np

with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

grid = np.array([[0 for _ in range(1000)] for _ in range(1000)])

for instruction in input:
    positions = re.findall("(\d\d?\d?,\d\d?\d?)", instruction)
    x_initial, y_initial = tuple(map(lambda x: int(x), positions[0].split(",")))
    x_end, y_end = tuple(map(lambda x: int(x), positions[1].split(",")))
    
    if "turn off" in instruction:
        grid[x_initial:x_end+1, y_initial:y_end+1] -= 1
        grid[x_initial:x_end+1, y_initial:y_end+1] = np.where(grid[x_initial:x_end+1, y_initial:y_end+1] < 0, 0, grid[x_initial:x_end+1, y_initial:y_end+1])

    elif "turn on" in instruction:
        grid[x_initial:x_end+1, y_initial:y_end+1] += 1

    else:
        grid[x_initial:x_end+1, y_initial:y_end+1] += 2

print(grid.sum())
