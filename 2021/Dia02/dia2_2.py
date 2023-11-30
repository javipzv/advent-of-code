with open('input.txt', 'r') as f:
    lines = f.readlines()

horzPos, depth, aim = 0, 0, 0
for command in lines:
    if 'forward' in command:
        value = int(command.replace("forward ", ""))
        horzPos += value
        depth += aim*value
    elif 'down' in command:
        aim += int(command.replace("down ", ""))
    else:
        aim -= int(command.replace("up ", ""))

print(horzPos*depth)