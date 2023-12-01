import hashlib

counter = 0
found = False
while not found:
    input = "ckczppom" + str(counter)
    result = hashlib.md5(input.encode())
    first_five = result.hexdigest()[:5]
    if first_five == "00000":
        print(counter)
        break
    counter += 1