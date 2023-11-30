def find_value(dic, string):
    uniques = {2: 1, 4: 4, 3: 7, 7: 8}
    if len(string) in uniques:
        value = uniques[len(string)]
    else:
        possible = [command for command in dic if len(command) == len(string)]
        for command in possible:
            lets = 0
            if found:
                break
            for letter in string:
                if letter not in string:
                    break
                lets += 1
                if lets == len(command):
                    value = dic[command]
                    found = True
                    break
    return value

dict_commands = {"acedgfb": 8, "cdfbe": 5, "gcdfa": 2, "fbcad": 3, "dab": 7, 
                "cefabd": 9, "cdfgeb": 6, "eafb": 4, "cagedb": 0, "ab": 1}

print(find_value(dict_commands, "cefbda"))