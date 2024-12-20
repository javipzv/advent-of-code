from itertools import permutations
import re
with open('input.txt', 'r') as file:
    input_data = [line.strip() for line in file]

distances = {}
cities = set()
for travel in input_data:
    origin, destination, distance = re.findall("(\w*) to (\w*) = (\d*)", travel)[0]
    distances[(origin, destination)] = int(distance)
    distances[(destination, origin)] = int(distance)
    cities.add(origin)
    cities.add(destination)

min_cost = float("inf")
possibilities = list(permutations(cities))
for path in possibilities:
    valid = True
    path_cost = 0
    for i in range(len(path)-1):
        if (path[i], path[i+1]) in distances:
            path_cost += distances[(path[i], path[i+1])]
        else:
            valid = False
    if valid:
        min_cost = min(path_cost, min_cost)

print(min_cost)

