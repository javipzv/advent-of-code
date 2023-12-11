with open('input3.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

def next(i, j):
    if grid[i-1][j] == "|" or grid[i-1][j] == "F" or grid[i-1][j] == "7": 
        return (i-1, j)
    elif grid[i+1][j] == "|" or grid[i+1][j] == "L" or grid[i+1][j] == "J":
        return (i+1, j)
    elif grid[i][j+1] == "-" or grid[i][j+1] == "J" or grid[i][j+1] == "7":
        return (i, j+1)
    elif grid[i][j-1] == "-" or grid[i][j-1] == "L" or grid[i][j-1] == "F":
        return (i, j-1)

def create_path():
    for i in range(len(grid)-1):
        for j in range(len(grid[0])-1):
            if grid[i][j] == "S":
                starting_position = (i, j)

    a, b = next(starting_position[0], starting_position[1])
    c, d = next(a, b)
    path = [(a, b), (c, d)]

    i, j = c, d
    while (i, j) != (starting_position[0], starting_position[1]):
        if grid[i][j] == "|":
            if (i-1, j) == path[len(path)-2]:
                i, j = i+1, j
                path += [(i, j)]
            else:
                i, j = i-1, j
                path += [(i, j)]
        elif grid[i][j] == "-":
            if (i, j-1) == path[len(path)-2]:
                i, j = i, j+1
                path += [(i, j)]
            else:
                i, j = i, j-1
                path += [(i, j)]
        elif grid[i][j] == "7":
            if (i, j-1) == path[len(path)-2]:
                i, j = i+1, j
                path += [(i, j)]
            else:
                i, j = i, j-1
                path += [(i, j)]
        elif grid[i][j] == "J":
            if (i-1, j) == path[len(path)-2]:
                i, j = i, j-1
                path += [(i, j)]
            else:
                i, j = i-1, j
                path += [(i, j)]
        elif grid[i][j] == "F":
            if (i, j+1) == path[len(path)-2]:
                i, j = i+1, j
                path += [(i, j)]
            else:
                i, j = i, j+1
                path += [(i, j)]
        elif grid[i][j] == "L":            
            if (i-1, j) == path[len(path)-2]:
                i, j = i, j+1
                path += [(i, j)]
            else:
                i, j = i-1, j
                path += [(i, j)]
    return set([(starting_position[0], starting_position[1])] + path)

def merge_consecutives(lista_posiciones):
    posiciones_result = []
    consecutive = False
    for i in range(len(lista_posiciones)-1):
        if consecutive:
            if (not (abs(lista_posiciones[i][1] - lista_posiciones[i+1][1]) == 1)):
                consecutive = False
                posiciones_result += [lista_posiciones[i]]
        else:
            if abs(lista_posiciones[i][1] - lista_posiciones[i+1][1]) == 1:
                consecutive = True
                posiciones_result += [lista_posiciones[i]]
            else:
                posiciones_result += [lista_posiciones[i]]
    return posiciones_result + [lista_posiciones[len(lista_posiciones)-1]]

def get_inside_pos(lista_posiciones):
    result = set()
    for i in range(0, len(lista_posiciones)-1, 2):
        for j in range(lista_posiciones[i][1], lista_posiciones[i+1][1]+1):
            result.add((lista_posiciones[0][0], j))
    return result

path_positions = create_path()

def get_middle_tiles(path):
    total_pos = set()
    for i in range(len(grid)):
        path_positions_row = sorted([(px, py) for (px, py) in path if px == i], key=lambda x: x[1])
        path_positions_row = merge_consecutives(path_positions_row)
        total_pos = total_pos | get_inside_pos(path_positions_row)
    return total_pos

inside_positions = get_middle_tiles(path_positions)

total = path_positions - inside_positions

print(total)