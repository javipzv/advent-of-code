with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

original_input = [list(x) for x in input]

for i, row in enumerate(original_input):
    for j, col in enumerate(row):
        if col == "^":
            guard_i, guard_j = i, j

start_guard_i = guard_i
start_guard_j = guard_j

next_direction = {(-1, 0): (0, 1),
                  (0, 1): (1, 0),
                  (1, 0): (0, -1),
                  (0, -1): (-1, 0)}

positions = []
direction = (-1, 0)

girando = False
input = [list(x) for x in original_input]
while guard_i >= 0 and guard_i < len(input[0]) and \
      guard_j >= 0 and guard_j < len(input):
    
    # See if current position is '.'
    if input[guard_i][guard_j] in ["."]:
        input[guard_i][guard_j] = "X"
        positions.append((guard_i, guard_j))

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

def find_loop(input_map, starting_i, starting_j):
    positions_of_change = set()
    loop = False
    direction = (-1, 0)
    guard_i, guard_j = starting_i, starting_j
    while 0 <= guard_i + direction[0] < len(input_map) and \
          0 <= guard_j + direction[1] < len(input_map[0]):
        next_i, next_j = guard_i + direction[0], guard_j + direction[1]
        next = input_map[next_i][next_j]
        if next == "#":
            if (guard_i, guard_j, direction) in positions_of_change:
                loop = True
                break
            else:
                positions_of_change.add((guard_i, guard_j, direction))
            direction = next_direction[direction]
        elif next == ".":
            guard_i = next_i
            guard_j = next_j
    return loop
    
loops = 0
for i, j in positions:
    new_input = [list(x) for x in original_input]
    new_input[i][j] = "#"
    new_input[start_guard_i][start_guard_j] = "."
    if find_loop(new_input, start_guard_i, start_guard_j):
        loops += 1

print(loops)
