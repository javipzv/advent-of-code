import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

names = []
data = {}
counters = {}

for line in input:
    name, speed, speed_time, rest_time = re.findall("(\w*) can fly (\d*) .* for (\d*)? .* for (\d*)", line)[0]
    names += [name]
    data[name] = [int(speed), int(speed_time), int(rest_time)]
    counters[name] = [0, int(speed_time), True]

for i in range(1, 2504):
    for reindeer in names:
        if counters[reindeer][2] and counters[reindeer][1] > 0:
            counters[reindeer][0] += data[reindeer][0]
            counters[reindeer][1] -= 1

        elif not counters[reindeer][2] and counters[reindeer][1] > 0:
            counters[reindeer][1] -= 1

        elif counters[reindeer][2] and counters[reindeer][1] == 0:
            counters[reindeer][2] = False
            counters[reindeer][1] = data[reindeer][2] - 1

        elif not counters[reindeer][2] and counters[reindeer][1] == 0:
            counters[reindeer][2] = True
            counters[reindeer][1] = data[reindeer][1] - 1
            counters[reindeer][0] += data[reindeer][0]

print(counters)