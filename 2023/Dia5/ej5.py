with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

for i in range(len(input)):
    if 'seeds' in input[i]:
        source = [int(s) for s in input[i][7:].split(" ")]
    elif 'map' in input[i]:
        triples = []
        for j in range(i+1, len(input)):
            if input[j] == "":
                break
            else:
                dest_start, source_start, range_len  = [int(x) for x in input[j].split(" ")]
                triples += [(dest_start, source_start, range_len)]
        result = []
        for s in source:
            added  = False
            for trip in triples:
                if s >= trip[1] and s < trip[1]+trip[2]:
                    result += [trip[0] + (s - trip[1])]
                    added = True
            if not added:
                result += [s]
        source = result

print(min(source))
