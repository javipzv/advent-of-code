import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

source = [int(s) for s in input[0][7:].split(" ")]
tuples_ranges = [(source[i], source[i+1]) for i in range(0, len(source)-1, 2)]
dic_maps = {}

for i in range(len(input)):
    if 'map' in input[i]:
        name = re.findall("(.*) map", input[i])[0]
        triples = []
        for j in range(i+1, len(input)):
            if input[j] == "":
                break
            else:
                dest_start, source_start, range_len  = [int(x) for x in input[j].split(" ")]
                triples += [(dest_start, source_start, range_len)]
        dic_maps[name] = triples

def add_range(nums, values):
    result = []
    for inicio, fin in nums:
        added = False            
        for dest_init, source_init, range_length in values:
            if inicio >= source_init and fin < (source_init+range_length):
                result += [(dest_init + inicio - source_init, dest_init + fin - source_init)]
                added = True
            elif inicio >= source_init and inicio < (source_init+range_length) and fin >= (source_init+range_length):
                limit = source_init+range_length-1
                result += [(dest_init + inicio - source_init, dest_init + limit - source_init)]
                nums.append((limit+1, fin))
                added = True
            elif inicio < source_init and fin >= source_init and fin < (source_init+range_length):
                limit = source_init
                result += [(dest_init + limit - source_init, dest_init + fin - source_init)]
                nums.append((inicio, limit-1))
                added = True
        if not added:
            result += [(inicio, fin)] 
    return list(set(result))

minimo = float("inf")
for inicio, longitud in tuples_ranges:
    res = [(inicio, inicio+longitud-1)]
    for mapping, values in dic_maps.items():
        nums = res
        res = add_range(nums, values)
    for i, f in res:
        minimo = min(minimo, i)

print(minimo)