from functools import reduce
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

times = [int(t) for t in input[0][5:].split(" ") if t != ""]
distances = [int(d) for d in input[1][9:].split(" ") if d != ""]

n_ways = []
for i in range(len(times)):
    half = times[i] // 2
    for j in range(half, times[i]):
        if j*(times[i]-j) <= distances[i]:
            n_ways += [(j-1)-(times[i]-(j-1))+1]
            break

result = reduce(lambda x, y: x*y, n_ways)
print(result)