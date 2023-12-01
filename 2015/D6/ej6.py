import re

with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for instruction in input:
    positions = re.findall("(\d\d?\d?,\d\d?\d?)", instruction)
    x_initial, y_initial = tuple(map(lambda x: int(x), positions[0].split(",")))
    x_end, y_end = tuple(map(lambda x: int(x), positions[1].split(",")))
    
    if "turn off" in instruction:
        for i in range(x_initial, x_end+1):
            for j in range(y_initial, y_end+1):
                grid[i][j] = 0

    elif "turn on" in instruction:
        for i in range(x_initial, x_end+1):
            for j in range(y_initial, y_end+1):
                grid[i][j] = 1

    else:
        for i in range(x_initial, x_end+1):
            for j in range(y_initial, y_end+1):
                if grid[i][j] == 1: 
                    grid[i][j] = 0
                else: 
                    grid[i][j] = 1

lit = sum([sum(x) for x in grid])

print(lit)

