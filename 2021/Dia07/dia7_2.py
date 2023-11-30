import math
with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]
crabs = list(map(int, lines[0].split(",")))
maximo, minimo, media = max(crabs), min(crabs), round(sum(crabs) / len(crabs))
min_sum = math.inf
pos = -1
suma = 0

for i in range(media - 10, media + 10):
    suma = 0
    for crab in crabs:
        dist = abs(crab - i)
        suma += int(dist*(dist+1) / 2) # Fórmula de Gauss
    if suma < min_sum:
        min_sum = suma
        pos = i

print(min_sum, pos) # Coincide con la media