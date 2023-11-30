with open('input.txt', 'r') as f:
    lines = f.readlines()

horzPos, depth = 0, 0
for command in lines:
    if 'forward' in command:
        horzPos += int(command.replace("forward ", ""))
    elif 'down' in command:
        depth += int(command.replace("down ", ""))
    else:
        depth -= int(command.replace("up ", ""))

print(horzPos*depth)