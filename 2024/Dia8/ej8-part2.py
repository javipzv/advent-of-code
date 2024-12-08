with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

positions = {}
for i, row in enumerate(input):
    for j, char in enumerate(row):
        if char != "." and char not in positions: 
            positions[char] = [(i, j)]
        elif char in positions:
            positions[char].append((i, j))

antenna_positions = set()
for letter, pos in positions.items():
    for i in range(len(pos) - 1):
        for j in range(i, len(pos) - 1):
            p1, p2 = pos[i], pos[j+1]
            antenna_positions.add(p1)
            antenna_positions.add(p2)
            diff_i = abs(p1[0] - p2[0])
            diff_j = abs(p1[1] - p2[1])
            min_i, max_i = min(p1[0], p2[0]), max(p1[0], p2[0])
            min_j, max_j = min(p1[1], p2[1]), max(p1[1], p2[1])

            if p1[1] >= p2[1]:
                ant1 = (min_i - diff_i, max_j + diff_j)
                while 0 <= ant1[0] < len(input) and 0 <= ant1[1] < len(input):
                    antenna_positions.add(ant1)
                    ant1 = (ant1[0] - diff_i, ant1[1] + diff_j)

                ant2 = (max_i + diff_i, min_j - diff_j)
                while 0 <= ant2[0] < len(input) and 0 <= ant2[1] < len(input):
                    antenna_positions.add(ant2)
                    ant2 = (ant2[0] + diff_i, ant2[1] - diff_j)

            else:
                ant1 = (min_i - diff_i, min_j - diff_j)
                while 0 <= ant1[0] < len(input) and 0 <= ant1[1] < len(input):
                    antenna_positions.add(ant1)
                    ant1 = (ant1[0] - diff_i, ant1[1] - diff_j)

                ant2 = (max_i + diff_i, max_j + diff_j)
                while 0 <= ant2[0] < len(input) and 0 <= ant2[1] < len(input):
                    antenna_positions.add(ant2)
                    ant2 = (ant2[0] + diff_i, ant2[1] + diff_j)

print(len(antenna_positions))
