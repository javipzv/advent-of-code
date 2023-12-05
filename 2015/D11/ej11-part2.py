def get_next(password):
    new_password = list(password)
    last = len(password)-1
    if new_password[last] != 'z':
        pass
        new_password[last] = next_char(new_password[last])
    else:
        i = len(password)-1
        while new_password[i] == 'z':
            new_password[i] = 'a'
            i -= 1
        new_password[i] = next_char(new_password[i])[0]
    return new_password

def next_char(char):
    abc = "abcdefghijklmnopqrstuvwxyz"
    idx = abc.index(char)
    return abc[(idx+1)%26]

password = "hxbxxyzz"
password = get_next(password)
abc = "abcdefghijklmnopqrstuvwxyz"
while True:
    # Increasing characters
    increasing = False
    for i in range(len(password)-2):
        if (password[i]+password[i+1]+password[i+2]) in abc:
            increasing = True

    # Confusing characters
    contain_confusing = ('i' in password) or ('l' in password) or ('o' in password)
    
    # Doubled characters
    doubled = False
    double_characters = 0
    idx = 0
    while idx < len(password)-1:
        if (password[idx] == password[idx+1]):
            double_characters += 1
            idx += 2
        else:
            idx += 1
    if double_characters > 1:
        doubled = True

    valid = increasing and (not contain_confusing) and doubled
    if valid:
        print(''.join(password))
        break
    password = get_next(password)
