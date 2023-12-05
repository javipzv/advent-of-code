import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

copies = {i:1 for i in range(1, len(input)+1)}

total = 0
for card in input:
    n_card = int(re.findall("Card\s*(\d*):", card)[0])
    winning, available = re.findall(":(.*) \| (.*)$", card)[0]
    winning = [int(n) for n in winning.split(" ") if n != ""]
    available = [int(n) for n in available.split(" ") if n != ""]
    matches = len([n for n in available if n in winning])
    if matches > 0:
        adding = 2**(matches-1)
        for i in range(n_card+1, n_card+matches+1):
            copies[i] += copies[n_card]
        total += adding*copies[n_card]

sum = sum(list(copies.values()))
print(sum)