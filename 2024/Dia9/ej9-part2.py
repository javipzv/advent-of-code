with open('input.txt', 'r') as file:
    input = [line.strip() for line in file][0]

file_ids = {}

file_id = 0
for i in range(0, len(input)):
    if i % 2 == 0:
        file_ids[file_id] = int(input[i])
        file_id += 1

original_file_ids = file_ids.copy()

index_last = len(file_ids) - 1
st = ""
checksum = 0
id_index = 0
multiplying_index = 0

for i in range(0, len(input)):
    # print(file_ids)
    if i % 2 == 0:
        if file_ids[id_index] > 0:
            for j in range(0, file_ids[id_index]):
                checksum += multiplying_index*id_index
                st += str(id_index)
                multiplying_index += 1
            file_ids[id_index] = 0
            id_index += 1
        else:
            for j in range(0, original_file_ids[id_index]):
                multiplying_index += 1
                st += "."
            id_index += 1

    else:
        free_space = int(input[i])
        done = False
        while free_space > 0 and index_last > 0:
            space_last = file_ids[index_last]
            if space_last != 0 and space_last <= free_space:
                for j in range(0, space_last):
                    checksum += multiplying_index*index_last
                    st += str(index_last)
                    multiplying_index += 1
                # for j in range(space_last, free_space):
                #     multiplying_index += 1
                #     st += "."
                file_ids[index_last] = 0
                free_space -= space_last
            else:
                index_last -= 1
        if free_space > 0:
            for j in range(0, free_space):
                multiplying_index += 1
                st += "."
        index_last = len(file_ids) - 1
    # print(st)
    # print()

# print(st)
print(checksum)