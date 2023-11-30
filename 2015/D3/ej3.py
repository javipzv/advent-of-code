with open('input.txt', 'r') as file:
    input = [line.strip() for line in file][0]

moves_santa = {"^": (lambda x, y: (x, y+1)),
               ">": (lambda x, y: (x+1, y)),
               "v": (lambda x, y: (x, y-1)),
               "<": (lambda x, y: (x-1, y))}

x, y  = 0, 0
cjto = set()
cjto.add((x, y))

for move in input:
    x, y = moves[move](x, y)
    cjto.add((x, y))

print(len(cjto))