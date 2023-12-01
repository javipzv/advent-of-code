import re
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

dic_wires = {}

for instruction in input:
    wire = re.findall("(\w\w?)$", instruction)[0]
    dic_wires[wire] = None

while None in dic_wires.values():
    for instruction in input:
        if "NOT" in instruction:
            inp, output = re.findall("(\w\w?) -> (\w\w?)", instruction)[0]
            if dic_wires[inp] is not None:
                dic_wires[output] = ~dic_wires[inp]
            
        elif "OR" in instruction:
            inp1, inp2, output = re.findall("(\w\w?) OR (\w\w?) -> (\w\w?)", instruction)[0]
            if inp1 in dic_wires and inp2 in dic_wires and dic_wires[inp1] is not None and dic_wires[inp2] is not None:
                dic_wires[output] = dic_wires[inp1] | dic_wires[inp2]
            elif inp1 not in dic_wires and inp2 in dic_wires and dic_wires[inp2] is not None:
                dic_wires[output] = inp1 | dic_wires[inp2]

        elif "AND" in instruction:
            inp1, inp2, output = re.findall("(\w\w?) AND (\w\w?) -> (\w\w?)", instruction)[0]
            if inp1 in dic_wires and inp2 in dic_wires and dic_wires[inp1] is not None and dic_wires[inp2] is not None:
                dic_wires[output] = dic_wires[inp1] & dic_wires[inp2]
            elif inp1 not in dic_wires and inp2 in dic_wires and dic_wires[inp2] is not None:
                dic_wires[output] = int(inp1) & dic_wires[inp2]

        elif "RSHIFT" in instruction:
            inp1, inp2, output = re.findall("(\w\w?) RSHIFT (\d*) -> (\w\w?)", instruction)[0]
            if inp1 in dic_wires and dic_wires[inp1] is not None:
                dic_wires[output] = dic_wires[inp1] >> int(inp2)
            else:
                dic_wires[output] = None

        elif "LSHIFT" in instruction:
            inp1, inp2, output = re.findall("(\w\w?) LSHIFT (\d*) -> (\w\w?)", instruction)[0]
            if inp1 in dic_wires and dic_wires[inp1] is not None:
                dic_wires[output] = dic_wires[inp1] << int(inp2)
            else:
                dic_wires[output] = None
        else:
            num = re.findall("\d", instruction)
            if num:
                val, output = re.findall("(\d*) -> (\w\w?)", instruction)[0]
                dic_wires[output] = int(val)
            else:
                inp, output = re.findall("(\w\w?) -> (\w\w?)", instruction)[0]
                if inp in dic_wires and dic_wires[inp] is not None:
                    dic_wires[output] = dic_wires[inp]
                else:
                    dic_wires[output] = None

print(dic_wires["a"])