import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file][0]

numbers = re.findall("(-?\d+)", input)
total = sum([int(n) for n in numbers])

print(total)

# total = 0
# for i in range(len(input)):
#     if input[i].isdigit() and not input[i-1].isdigit():
#         number = input[i]
#         if input[i-1] == "-":
#             number = "-" + number
#         while input[i+1].isdigit():
#             number += input[i+1]
#             i += 1
#         total += int(number)

# print(total)