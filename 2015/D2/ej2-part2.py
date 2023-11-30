with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

sum = 0
for present in input:
    present = present.split("x")
    l, w, h = int(present[0]), int(present[1]), int(present[2])
    maxi = max([l, w, h])
    wrap = l*2+w*2+h*2-maxi*2
    bow = l*w*h
    sum += wrap + bow

print(sum)