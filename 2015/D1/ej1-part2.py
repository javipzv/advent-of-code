with open('input.txt', 'r') as file:
    input = [line.strip() for line in file][0]

floor = 0

for indice, instruction in enumerate(input):
    if instruction == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print("The instruction is:", indice + 1)
        break