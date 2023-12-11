with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file]

galaxies_pos = []
empty_rows = []
empty_cols = []

for i in range(len(grid)):
    n_galaxies = 0
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            galaxies_pos += [(i, j)]
            n_galaxies += 1
    if n_galaxies == 0:
        empty_rows += [i]

cols_aux = [y for x, y in galaxies_pos]
for j in range(len(grid[0])):
    if j not in cols_aux:
        empty_cols += [j]

total = 0
for i in range(len(galaxies_pos)-1):
    x, y = galaxies_pos[i]
    for j in range(i+1, len(galaxies_pos)):
        u, v = galaxies_pos[j]
        diff = abs(x-u)+abs(y-v)
        min_x, max_x, min_y, max_y = min(x, u), max(x, u), min(y, v), max(y, v)
        double_rows = len([row for row in empty_rows if min_x < row < max_x])
        double_cols = len([col for col in empty_cols if min_y < col < max_y])
        total += diff+double_cols+double_rows

print(total)