from math import lcm

with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

order = input[0]
directions = {}
actual_positions = []
for trio in input[2:]:
    directions[trio[:3]] = (trio[7:10], trio[12:15])
    if trio[2] == "A":
        actual_positions += [trio[:3]]

first_z = {i:None for i in range(len(actual_positions))}

n_moves = 0
j = 0
while True:
    move = order[j]
    for i in range(len(actual_positions)):
        if not first_z[i] and actual_positions[i][2] == "Z":
            first_z[i] = n_moves

    ended = True
    for i in range(len(first_z)):
        if not first_z[i]:
            ended = False
    
    if ended:
        break
    else:
        for i in range(len(actual_positions)):
            if move == "L":
                actual_positions[i] = directions[actual_positions[i]][0]
            elif move == "R":
                actual_positions[i] = directions[actual_positions[i]][1]

    if j == (len(order)-1):
        j = 0
    else:
        j += 1
    n_moves += 1

def apply_lcm(values):
    return lcm(values[0], values[1], values[2], values[3], values[4], values[5])

print(apply_lcm(list(first_z.values())))

