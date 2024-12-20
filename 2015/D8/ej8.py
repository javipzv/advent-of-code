with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

total = 0
for string in input:
    code_characters = len(string)
    len_new_string = 0
    continuations = 0

    for i in range(len(string)-1):
        if continuations > 0:
            continuations -= 1
            continue
        if (string[i] + string[i+1]) == "\\x":
            len_new_string += 1
            continuations = 3
        elif (string[i] + string[i+1]) == "\\\\" or (string[i] + string[i+1]) == "\\\"":
            len_new_string += 1
            continuations = 1
        else:
            len_new_string += 1
    
    total += (code_characters - (len_new_string - 1))

print(total)
