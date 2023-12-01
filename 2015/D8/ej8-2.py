with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

total = 0
for string in input:
    code_characters = len(string)

    # string = string[1:-1]
    
    # print(string, end=" -> ")

    for i in range(len(string)-1):
        print(string[i]+string[i+1], len(string)-1, i)
        if string[i]+string[i+1] == "\\x":
            string = string[:i] + "a" + string[i+3:]
    
    # print(string)


    # total += (code_characters - memory_characters)

print(total)
