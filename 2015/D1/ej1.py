with open('input.txt', 'r') as file:
    input = [line.strip() for line in file][0]
    
floor = sum([1 for i in input if i == "("]) + sum([-1 for i in input if i == ")"])

print(floor)