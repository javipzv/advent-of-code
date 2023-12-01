with open('input.txt', 'r') as file:
    input = [line.strip() for line in file][0]

moves = {"^": (lambda x, y: (x, y+1)),
               ">": (lambda x, y: (x+1, y)),
               "v": (lambda x, y: (x, y-1)),
               "<": (lambda x, y: (x-1, y))}

x_santa, y_santa, x_robosanta, y_robosanta = 0, 0, 0, 0
cjto = set()
cjto.add((0, 0))

for i, move in enumerate(input):
    if i % 2 == 0:
        x_santa, y_santa = moves[move](x_santa, y_santa)
        cjto.add((x_santa, y_santa))
    else:
        x_robosanta, y_robosanta = moves[move](x_robosanta, y_robosanta)
        cjto.add((x_robosanta, y_robosanta))

print(len(cjto))