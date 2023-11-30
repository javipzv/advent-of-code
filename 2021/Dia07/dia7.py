import math
with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]
crabs = list(map(int, lines[0].split(",")))
maximo, minimo, median = max(crabs), min(crabs), sorted(crabs)[round(len(crabs) / 2)]
min_sum = math.inf
pos = -1

for i in range(median - 10, median + 10):
    sum = 0
    for crab in crabs:
        dist = abs(crab - i)
        sum += dist
    if sum < min_sum:
        min_sum = sum
        pos = i

print(min_sum, pos) # Coincide con la mediana
