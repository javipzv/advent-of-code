import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

sum = 0
dic_nums = {"one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9"}

for word in input:
    first = re.findall("(one|two|three|four|five|six|seven|eight|nine|\d).*", word)[0]
    second = re.findall(".*(one|two|three|four|five|six|seven|eight|nine|\d).*$", word)[0]
    sum += int(dic_nums[first] + dic_nums[second])

print(sum)