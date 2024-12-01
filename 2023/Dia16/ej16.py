with open('input2.txt', 'r') as file:
    grid = [line.strip() for line in file]

next_pos = {'right': lambda i, j: (i, j+1),
            'left': lambda i, j: (i, j-1),
            'up': lambda i, j: (i-1, j),
            'down': lambda i, j: (i+1, j)}

# def beams_path(grid, actual_pos, direction, positions):
#     if actual_pos[0] < 0 or actual_pos[0] >= len(grid) or actual_pos[1] < 0 or actual_pos[1] >= len(grid[0]):
#         return positions
#     else:
#         if (actual_pos[0], actual_pos[1], direction) in past:
#             return positions
#         else:
#             positions.add((actual_pos[0], actual_pos[1]))
#             past.add((actual_pos[0], actual_pos[1], direction))
#             now = grid[actual_pos[0]][actual_pos[1]]
#             if (now == ".") or (now == "-" and direction == 'right') or (now == "-" and direction == 'left') \
#                                 or (now == "|" and direction == 'up') or (now == "|" and direction == 'down'):
#                 next_p = next_pos[direction](actual_pos[0], actual_pos[1])
#                 return positions | beams_path(grid, next_p, direction, positions)

#             elif now == "\\":
#                 if direction == "right":
#                     return positions | beams_path(grid, (actual_pos[0]+1, actual_pos[1]), "down", positions)
#                 elif direction == "left":
#                     return positions | beams_path(grid, (actual_pos[0]-1, actual_pos[1]), "up", positions)
#                 elif direction == "up":
#                     return positions | beams_path(grid, (actual_pos[0], actual_pos[1]-1), "left", positions)
#                 elif direction == "down":
#                     return positions | beams_path(grid, (actual_pos[0], actual_pos[1]+1), "right", positions)
                
#             elif now == "/":
#                 if direction == "right":
#                     return positions | beams_path(grid, (actual_pos[0]-1, actual_pos[1]), "up", positions)
#                 elif direction == "left":
#                     return positions | beams_path(grid, (actual_pos[0]+1, actual_pos[1]), "down", positions)
#                 elif direction == "up":
#                     return positions | beams_path(grid, (actual_pos[0], actual_pos[1]+1), "right", positions)
#                 elif direction == "down":
#                     return positions | beams_path(grid, (actual_pos[0], actual_pos[1]-1), "left", positions)
                
#             elif now == "-" and (direction == 'up' or direction == 'down'):
#                 return positions | beams_path(grid, (actual_pos[0], actual_pos[1]-1), "left", positions) | beams_path(grid, (actual_pos[0], actual_pos[1]+1), "right", positions)
            
#             elif now == "|" and (direction == 'left' or direction == 'right'):
#                 return positions | beams_path(grid, (actual_pos[0]-1, actual_pos[1]), "up", positions) | beams_path(grid, (actual_pos[0]+1, actual_pos[1]), "down", positions)

# past = set()
# pos = beams_path(grid, (0, 0), 'right', set())

# print(len(pos))

## Second part

from collections import deque

cola = deque()
past = set()
positions = set()
actual_pos = (0, 0)
direction = 'right'
# while cola is not empty
while len(cola) > 0:
    if actual_pos[0] < 0 or actual_pos[0] >= len(grid) or actual_pos[1] < 0 or actual_pos[1] >= len(grid[0]):
        actual_pos = cola.popleft()
        break
    else:
        if (actual_pos[0], actual_pos[1], direction) in past:
            break
        else:
            positions.add((actual_pos[0], actual_pos[1]))
            past.add((actual_pos[0], actual_pos[1], direction))
            now = grid[actual_pos[0]][actual_pos[1]]
            if (now == ".") or (now == "-" and direction == 'right') or (now == "-" and direction == 'left') \
                                or (now == "|" and direction == 'up') or (now == "|" and direction == 'down'):
                actual_pos = next_pos[direction](actual_pos[0], actual_pos[1])

            elif now == "\\":
                if direction == "right":
                    actual_pos = (actual_pos[0]+1, actual_pos[1])
                    direction = "down"
                elif direction == "left":
                    actual_pos = (actual_pos[0]-1, actual_pos[1])
                    direction = "up"
                elif direction == "up":
                    actual_pos = (actual_pos[0], actual_pos[1]-1)
                    direction = "left"
                elif direction == "down":
                    actual_pos = (actual_pos[0], actual_pos[1]+1)
                    direction = "right"
                
            elif now == "/":
                if direction == "right":
                    actual_pos = (actual_pos[0]-1, actual_pos[1])
                    direction = "up"
                elif direction == "left":
                    actual_pos = (actual_pos[0]+1, actual_pos[1])
                    direction = "down"
                elif direction == "up":
                    actual_pos = (actual_pos[0], actual_pos[1]+1)
                    direction = "right"
                elif direction == "down":
                    actual_pos = (actual_pos[0], actual_pos[1]-1)
                    direction = "left"
                
            elif now == "-" and (direction == 'up' or direction == 'down'):
                actual_pos = (actual_pos[0], actual_pos[1]-1)
                cola.append((actual_pos[0], actual_pos[1]+1))
                direction = "left"
            elif now == "|" and (direction == 'left' or direction == 'right'):
                actual_pos = (actual_pos[0]-1, actual_pos[1])
                cola.append((actual_pos[0]+1, actual_pos[1]))
                direction = "up"