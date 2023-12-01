with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

nice_strings = 0
disallowed_strings = ["ab", "cd", "pq", "xy"]

for word in input:
    # PAIR TWICE
    pair_twice = False
    i = 0
    for i in range(len(word)-1):
        pair = word[i] + word[i+1]
        for j in range(len(word)-1):
            if j != i and j != (i+1) and j != (i-1):
                if word[j] + word[j+1] == pair:
                    pair_twice = True
                    break
        if pair_twice:
            break
    if not pair_twice:
        continue

    # LETTER TWICE
    letter_twice = False
    i = 0
    while i < (len(word) - 2):
        if word[i] == word[i+2]:
            letter_twice = True
            break
        i += 1 
    if not letter_twice:
        continue

    nice_strings += 1

print(nice_strings)
