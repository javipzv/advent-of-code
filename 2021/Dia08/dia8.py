import re
with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

uniques = 0
for line in lines:
    parts = line.split(" | ")
    second = re.findall("[a-z]+", parts[1])
    for command in second:
        if len(command) == 2 or len(command) == 3 or len(command) == 4 or len(command) == 7:
            uniques += 1

print(uniques)