import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

l1 = []
l2 = {}

for line in input:
    nums = [int(x) for x in re.findall(r'(\d*)\s*(\d*)', line)[0]]
    l1.append(nums[0])
    if nums[1] not in l2:
        l2[nums[1]] = 1
    else:
        l2[nums[1]] += 1

d = 0

for i in l1:
    if i in l2:
        d += i*l2[i]

print(d)