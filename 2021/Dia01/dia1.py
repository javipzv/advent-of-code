with open('input.txt', 'r') as f:
    lines = f.readlines()

num_incrementos = len([int(lines[i]) for i in range(len(lines) - 1) if int(lines[i]) < int(lines[i + 1])])
print(num_incrementos)