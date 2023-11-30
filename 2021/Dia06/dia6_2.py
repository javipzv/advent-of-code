from functools import reduce
with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

fish = list(map(int, lines[0].split(",")))
dict_fish = {i:0 for i in range(0, 9)}
new_dict = dict_fish

for timer in fish:
    dict_fish[timer] += 1

for i in range(256):
    new_dict = {i:0 for i in range(0, 9)}
    for x in dict_fish:
        if x == 0:
            new_dict[6] += dict_fish[x]
            new_dict[8] += dict_fish[x]    
        else:
            new_dict[x - 1] += dict_fish[x]
    dict_fish = new_dict

fishes = reduce(lambda a, b: a + b, (x for x in dict_fish.values()))

print(fishes)