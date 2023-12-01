with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

total = 0
for string in input:
    code_characters = len(string)
    len_new_string = 0
    continuations = 0

    for i in range(len(string)):
        if continuations > 0:
            continuations -= 1
            continue
        # INITIAL ESCAPE
        if i == 0:
            len_new_string += 2
        # END ESCAPE
        elif i == (len(string) - 1):
            len_new_string += 2
        # SPECIAL CASES
        elif (string[i] + string[i+1]) == "\\x":
            len_new_string += 1
        elif (string[i] + string[i+1]) == "\\\\" or (string[i] + string[i+1]) == "\\\"":
            len_new_string += 2
            continuations = 1
    
    total += len_new_string

print(total)
