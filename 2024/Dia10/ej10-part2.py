with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

nine_positions = set()
for i, row in enumerate(input):
    for j, height in enumerate(row):
        if height == "9":
            nine_positions.add((i, j))


directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

def calculate_trailhead(pos):
    count = 0
    i, j = pos
    if input[i][j] != "0":
        for dir in directions:
            new_i, new_j = i + dir[0], j + dir[1]
            if 0 <= new_i < len(input) and 0 <= new_j < len(input[0]) and input[new_i][new_j] != ".":
                if int(input[new_i][new_j]) == int(input[i][j]) - 1:
                    count += calculate_trailhead((new_i, new_j))
    else:
        count = 1
    return count

result = 0
for m, n in nine_positions:
    result += calculate_trailhead((m, n))

print(result)

