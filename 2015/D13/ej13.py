import re
from itertools import permutations
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

input = [line.replace("gain ", "").replace("lose ", "-") for line in input]
people_happiness = {}
people = set()

for line in input:
    p1, happiness, p2 = re.findall("^(\w*) would (\-?\d*) .* (\w*).$", line)[0]
    people_happiness[(p1, p2)] = int(happiness)
    people.add(p1)
    people.add(p2)

max_happiness = float("-inf")
for perm in list(permutations(people)):
    total_happiness = 0

    for i in range(len(perm)-1):
        total_happiness += people_happiness[(perm[i], perm[i+1])]
    total_happiness += people_happiness[(perm[len(perm)-1], perm[0])]

    for i in range(len(perm)-1, -1, -1):
        total_happiness += people_happiness[(perm[i], perm[i-1])]
    
    max_happiness = max(total_happiness, max_happiness)

print(max_happiness)