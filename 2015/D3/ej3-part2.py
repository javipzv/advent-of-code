with open('input.txt', 'r') as file:
    input = [line.strip() for line in file][0]

moves = {"^": (lambda x, y: (x, y+1)),
         ">": (lambda x, y: (x+1, y)),
         "v": (lambda x, y: (x, y-1)),
         "<": (lambda x, y: (x-1, y))}