import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

total = 0
for card in input:
    winning, available = re.findall(":(.*) \| (.*)$", card)[0]
    winning = [int(n) for n in winning.split(" ") if n != ""]
    available = [int(n) for n in available.split(" ") if n != ""]
    matches = len([n for n in available if n in winning])
    if matches > 0:
        total += 2**(matches-1)

print(total)
