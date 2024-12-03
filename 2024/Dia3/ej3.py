import re

with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

input = "".join(input)
mults = re.findall("mul\((\d*),(\d*)\)", input)
result = sum(list(map(lambda x: int(x[0])*int(x[1]), mults)))

print(result)