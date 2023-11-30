import re
with open('input.txt', 'r') as f:
    lines = f.readlines()

def diagonal(p1, p2):
    pos = []
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    minimumX, maximumX = min(x1, x2), max(x1, x2)
    minimumY, maximumY = min(y1, y2), max(y1, y2)
    if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
        for i in range(0, abs(minimumX - maximumX) + 1):
            pos += [(minimumX + i, minimumY + i)]
    else:
        for i in range(0, abs(minimumX - maximumX) + 1):
            pos += [(minimumX + i, maximumY - i)]
    return pos

def introduce(dictionary, point):
    if point in dictionary:
        dictionary[point] += 1
    else:
        dictionary[point] = 1

lines = [x[:-1] for x in lines]

dict_nums = {}
for line in lines:
    points = list(map(int, re.findall("[0-9]+", line)))
    x_stt, y_stt, x_end, y_end = points[0], points[1], points[2], points[3]
    if x_stt == x_end:
        minimum, maximum = min(y_stt, y_end), max(y_stt, y_end)
        for num in range(minimum, maximum + 1):
            introduce(dict_nums, (x_stt, num))
    elif y_stt == y_end:
        minimum, maximum = min(x_stt, x_end), max(x_stt, x_end)
        for num in range(minimum, maximum + 1):
            introduce(dict_nums, (num, y_stt))
    else:
        pos = diagonal((x_stt, y_stt), (x_end, y_end))
        for point in pos:
            introduce(dict_nums, point)

overlappings = [valor for valor in dict_nums.values() if valor >= 2]
print(len(overlappings))