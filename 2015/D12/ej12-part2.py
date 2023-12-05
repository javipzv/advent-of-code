import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file][0]

numbers = re.findall("(-?\d+)", input)
total = sum([int(n) for n in numbers])

for i in range(len(input)-2):
    pass