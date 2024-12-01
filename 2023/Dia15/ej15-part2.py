import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

input = input[0].split(",")

boxes = {i:[] for i in range(0, 256)}

total = 0
current = 0
for string in input:
    current = 0
    label, sign, num = re.findall("(.*)(=|-)(\d*)", string)[0]
    if sign == "=":
        num = int(num)
    for l in label:
        current += ord(l)
        current *= 17
        current %= 256
    
    if sign == "-":
        last = [x for x in boxes[current] if x[0] == label]
        if last:
            idx = boxes[current].index(last[0])
            del boxes[current][idx]
    elif sign == "=":
        last = [x for x in boxes[current] if x[0] == label]
        if last:
            idx = boxes[current].index(last[0])
            boxes[current][idx] = (label, num)
        else:
            boxes[current].append((label, num))

total = 0
for key, value in boxes.items():
    for i, v in enumerate(value):
        total += (key+1)*(i+1)*v[1]

print(total)
