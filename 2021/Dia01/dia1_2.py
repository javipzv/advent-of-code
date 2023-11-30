with open('input.txt', 'r') as f:
    lines = f.readlines()

num_incremento = 0
for i in range(len(lines)):
    sum1 = sum([int(x) for x in lines[i: i + 3]])
    sum2 = sum([int(x) for x in lines[i + 1: i + 4]])
    if sum1 < sum2:
        num_incremento += 1

print(num_incremento)