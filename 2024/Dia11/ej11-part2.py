with open('input.txt', 'r') as file:
    input = [line.strip() for line in file][0]

numbers = [int(x) for x in input.split(" ")]

blinks = 25
for n in range(blinks):
    new = []
    for x in numbers:
        if x == 0:
            new.append(1)
        elif len(str(x)) % 2 == 0:
            new.append(int(str(x)[: len(str(x)) // 2 ]))
            new.append(int(str(x)[ len(str(x)) // 2 :]))
        else:
            new.append(x*2024)
    numbers = new

print(len(numbers))