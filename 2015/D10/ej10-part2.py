input = "1113222113"

for _ in range(50):
    result = ""
    for i in range(len(input)):
        if i == 0:
            n = input[0]
            last_n = n
            counter = 1
        else:
            if input[i] == last_n:
                counter += 1
            else:
                result += str(counter) + last_n
                last_n = input[i]
                counter = 1

    result += str(counter) + last_n
    input = result

print(len(result))