from functools import reduce
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

def n_ways_binary_search(begin, end, time, distance):
    mid = begin+(end-begin)//2
    if mid == begin:
        return begin-(time-begin)+1
    if mid*(time-mid) <= distance:
        return n_ways_binary_search(begin, mid, time, distance)
    else:
        return n_ways_binary_search(mid, end, time, distance)

times = [int(t) for t in input[0][5:].split(" ") if t != ""]
distances = [int(d) for d in input[1][9:].split(" ") if d != ""]

time = int("".join([t for t in input[0][5:] if t != " "]))
distance = int("".join([d for d in input[1][9:] if d != " "]))

n_ways = []
for i in range(len(times)):
    n_ways += [n_ways_binary_search(times[i]/2, times[i], times[i], distances[i])]

print("Part 1:", reduce(lambda x, y: int(x*y), n_ways))
print("Part 2:", n_ways_binary_search(time//2, time, time, distance))
