with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

total = 0
for string in input:
    code_characters = len(string)
    memory_characters = len(string) - 2
    
    for i in range(len(string)-1):
        if string[i]+string[i+1] == "\\x" and string[i-1] != "\\":
            memory_characters -= 3
        elif string[i]+string[i+1] == "\\\\":
            memory_characters -= 1
        elif string[i]+string[i+1] == "\\\"":
            memory_characters -= 1

    print(code_characters-memory_characters)
    total += (code_characters - memory_characters)

print(total)
