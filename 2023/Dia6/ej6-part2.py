with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

time = int("".join([t for t in input[0][5:] if t != " "]))
distance = int("".join([d for d in input[1][9:] if d != " "]))

half = time // 2
for i in range(half, time, 1000):
    if i*(time-i) <= distance:
        for j in range(i-1000, i):
            if j*(time-j) <= distance:
                print((j-1)-(time-(j-1))+1)
                break
        break