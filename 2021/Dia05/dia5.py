import re
with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

def introduce(dictionary, point):
    if point in dictionary:
        dictionary[point] += 1
    else:
        dictionary[point] = 1

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

overlappings = [valor for valor in dict_nums.values() if valor >= 2]
print(len(overlappings))