with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

def bin_to_decimal(bin_num: str):
    result = 0
    for i in range(len(bin_num)):
        result += int(bin_num[-i-1])*2**i
    return result

def get_higher_oxygen(lista: list[str], index: int):
    zeros = []
    ones = []
    for binary in lista:
        if binary[index] == "0":
            zeros += [binary]
        else:
            ones += [binary]
    if len(zeros) > len(ones):
        return zeros
    return ones

def get_higher_CO2(lista: list[str], index: int):
    zeros = []
    ones = []
    for binary in lista:
        if binary[index] == "0":
            zeros += [binary]
        else:
            ones += [binary]
    if len(zeros) > len(ones):
        return ones
    return zeros

longitud = len(lines[0])

numeros1 = lines
numeros2 = lines
for i in range(longitud):
    if len(numeros1) > 1:
        numeros1 = get_higher_oxygen(numeros1, i)
    if len(numeros2) > 1:
        numeros2 = get_higher_CO2(numeros2, i)

oxyrate = bin_to_decimal(numeros1[0])
CO2rate = bin_to_decimal(numeros2[0])
print(oxyrate*CO2rate)
