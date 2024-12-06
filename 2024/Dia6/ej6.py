with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

input = [list(x) for x in input]

for i, row in enumerate(input):
    for j, col in enumerate(row):
        if col == "^":
            guard_i, guard_j = i, j

next_direction = {(-1, 0): (0, 1),
                  (0, 1): (1, 0),
                  (1, 0): (0, -1),
                  (0, -1): (-1, 0)}

positions = 0
direction = (-1, 0)

girando = False
while guard_i >= 0 and guard_i < len(input[0]) and \
      guard_j >= 0 and guard_j < len(input):
    
    # See if current position is '.'
    if input[guard_i][guard_j] in [".", "^"]:
        input[guard_i][guard_j] = "X"
        positions += 1

    # See if next position is '#'
    next_i, next_j = guard_i + direction[0], guard_j + direction[1]

    if 0 <= next_i < len(input[0]) and 0 <= next_j < len(input):
        next = input[next_i][next_j]
        if next == "#":
            direction = next_direction[direction]
            if input[guard_i + direction[0]][guard_j + direction[1]] == '#':
                direction = next_direction[direction]

        guard_i = guard_i + direction[0]
        guard_j = guard_j + direction[1]
    else:
        break

print(positions)


