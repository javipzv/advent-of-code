import re

with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

input = "".join(input)
commands = re.findall("mul\(\d*,\d*\)|don't\(\)|do\(\)", input)

result = 0
doing = True
for com in commands:
    if com[0] == 'm' and doing:
        nums = re.findall("\d*,\d*", com)[0].split(",")
        result += int(nums[0])*int(nums[1])
    if com == "do()":
        doing = True
    elif com == "don't()":
        doing = False

print(result)