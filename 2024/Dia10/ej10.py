with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

nine_positions = set()
for i, row in enumerate(input):
    for j, height in enumerate(row):
        if height == "9":
            nine_positions.add((i, j))


directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

def calculate_trailhead(pos):
    starts = set()
    i, j = pos
    if input[i][j] != "0":
        for dir in directions:
            new_i, new_j = i + dir[0], j + dir[1]
            if 0 <= new_i < len(input) and 0 <= new_j < len(input[0]) and input[new_i][new_j] != ".":
                if int(input[new_i][new_j]) == int(input[i][j]) - 1:
                    if (new_i, new_j) in dp:
                        starts = starts | dp[(new_i, new_j)]
                    else:
                        starts = starts | calculate_trailhead((new_i, new_j))
    else:
        starts.add(pos)
    dp[pos] = starts
    return starts

result = 0
dp = {}
for m, n in nine_positions:
    result += len(calculate_trailhead((m, n)))

print(result)

