import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

l1 = []
l2 = []

for line in input:
    nums = [int(x) for x in re.findall(r'(\d*)\s*(\d*)', line)[0]]
    l1.append(nums[0])
    l2.append(nums[1])

l1 = sorted(l1)
l2 = sorted(l2)

d = 0

for i in range(len(l1)):
    d += abs(l1[i] - l2[i])

print(d)