with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

order = input[0]
directions = {}
for trio in input[2:]:
    directions[trio[:3]] = (trio[7:10], trio[12:15])

actual_pos = "AAA"
i = 0
n_moves = 0
while actual_pos != "ZZZ":
    move = order[i]
    if move == "L":
        actual_pos = directions[actual_pos][0]
    elif move == "R":
        actual_pos = directions[actual_pos][1]
    if i == (len(order)-1):
        i = 0
    else:
        i += 1
    n_moves += 1

print(n_moves)