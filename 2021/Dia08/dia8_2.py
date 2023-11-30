import re
with open('input.txt', 'r') as f:
    lines = f.readlines()

def find_value(dic, string):
    uniques = {2: 1, 4: 4, 3: 7, 7: 8}
    if len(string) in uniques:
        value = uniques[len(string)]
    else:
        for x in dic:
            letters = [l for l in string if l in x]
            if len(letters) == len(x):
                value = dic[x]
                break
    return value

lines = [x[:-1] for x in lines]
dict_commands = {"acedgfb": 8, "cdfbe": 5, "gcdfa": 2, "fbcad": 3, "dab": 7, 
                "cefabd": 9, "cdfgeb": 6, "eafb": 4, "cagedb": 0, "ab": 1}

lines = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe']

sum = 0
for line in lines:
    parts = line.split(" | ")
    second = re.findall("[a-z]+", parts[1])
    i = 1000
    for command in second:
        value = find_value(dict_commands, command)
        print(value)
        sum += value*i
        i /= 10
    print(sum)