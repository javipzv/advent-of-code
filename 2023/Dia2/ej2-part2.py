import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

total = 0
for game in input:
    min_quantities = {"red": 0, "green": 0, "blue": 0}
    id, sets = re.findall("Game(?<=) (\d*):(?<=) (.*)", game)[0]
    groups = re.findall("(\d* \w*)", " " + sets)

    for i in range(0, len(groups), 2):
        color = groups[i+1].strip()
        min_quantities[color] = max(int(groups[i]), min_quantities[color])

    total += min_quantities["red"]*min_quantities["green"]*min_quantities["blue"]

print(total)