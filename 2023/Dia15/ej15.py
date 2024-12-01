with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

input = input[0].split(",")
total = 0
current = 0
for string in input:
    current = 0
    for l in string:
        current += ord(l)
        current *= 17
        current %= 256
    total += current

print(total)