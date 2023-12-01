import hashlib

counter = 0
found = False
while not found:
    input = "ckczppom" + str(counter)
    result = hashlib.md5(input.encode())
    first_six = result.hexdigest()[:6]
    if first_six == "000000":
        print(counter)
        break
    counter += 1