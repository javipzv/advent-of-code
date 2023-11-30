with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

sum = 0
for present in input:
    present = present.split("x")
    l, w, h = int(present[0]), int(present[1]), int(present[2])
    sq_feet = 2*l*w + 2*w*h + 2*h*l
    maxi = max([l, w, h])
    smallest_side = l*w*h//maxi
    sum += sq_feet+smallest_side

print(sum)