import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

sum = 0

for word in input:
    regex = re.findall("(\d).*(\d).*$", word)
    if regex:
        nums = int(regex[0][0]+regex[0][1])
    else:
        regex = re.findall("\d", word)[0]
        nums = int(regex+regex)
    sum += nums

print(sum)