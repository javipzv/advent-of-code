with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

fish = list(map(int, lines[0].split(",")))

for i in range(80):
    for j in range(len(fish)):
        if fish[j] == 0:
            fish[j] = 6
            fish.append(8)
        else:
            fish[j] -= 1

print(len(fish))