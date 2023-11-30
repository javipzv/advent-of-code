with open('input.txt', 'r') as f:
    lines = f.readlines()

gamma = ""
dict_sums = {n:0 for n in range(12)}

for bin in lines:
    for i in range(12):
        dict_sums[i] += int(bin[i])

gamma = "".join(["1" if value > 500 else "0" for value in dict_sums.values()])
epsilon = ["0" if value == "1" else "1" for value in gamma]

def bin_to_decimal(num):
    result = 0
    for i in range(len(num)):
        result += int(num[-i-1])*2**i
    return result

print(bin_to_decimal(gamma)*bin_to_decimal(epsilon))



