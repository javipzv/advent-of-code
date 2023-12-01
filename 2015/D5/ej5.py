with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

nice_strings = 0
disallowed_strings = ["ab", "cd", "pq", "xy"]

for word in input:
    # VOWELS
    vowels = len([x for x in word if x in "aeiou"])
    if vowels <= 2:
        continue
    
    # TWICE
    twice = False
    i = 0
    while i < (len(word) - 1):
        if word[i] == word[i+1]:
            twice = True
            break
        i += 1 
    if not twice:
        continue

    # DISALLOWED STRINGS
    disallowed_counter = len([x for x in disallowed_strings if x in word])
    if disallowed_counter:
        continue

    nice_strings += 1

print(nice_strings)
