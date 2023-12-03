import re
with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file]

def around(x, y):
    return [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]

def checkAround(grid, i, j):
    points = around(i, j)
    for x, y in points:
        if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]):
            if grid[x][y] not in nums and grid[x][y] != ".":
                return True
    return False

def getNumbers(grid, i, j):
    total = 0
    if checkAround(grid, i, j):
        start = re.findall("(\d+)$", grid[i][:j])
        if not start:
            start = [""]
        num = start[0] + grid[i][j]
        end = re.findall("^(\d+)", grid[i][j+1:])
        if not end:
            end = [""]
        num += end[0]
        num = int(num)
        total += num
    return total

nums = [str(i) for i in range(0, 10)]
sum = 0
for i in range(len(grid)):
    same_number = False
    for j in range(len(grid[0])):
        char = grid[i][j]
        if char in nums and not same_number:
            n = getNumbers(grid, i, j)
            if n > 0:
                same_number = True
            sum += n
        else:
            if char in nums:
                same_number = True
            else:
                same_number = False

print(sum)