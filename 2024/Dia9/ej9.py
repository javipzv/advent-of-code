with open('input.txt', 'r') as file:
    input = [line.strip() for line in file][0]

file_ids = {}

file_id = 0
for i in range(0, len(input)):
    if i % 2 == 0:
        file_ids[file_id] = int(input[i])
        file_id += 1

index_last = len(file_ids)-1
st = ""
checksum = 0
id_index = 0
multiplying_index = 0

for i in range(0, len(input)):
    if i % 2 == 0:
        for j in range(0, file_ids[id_index]):
            checksum += multiplying_index*id_index
            st += str(id_index)
            multiplying_index += 1
        file_ids[id_index] = 0
        id_index += 1

    else:
        free_space = int(input[i])
        while free_space > 0:
            if index_last < 0:
                break
            space_last = file_ids[index_last]
            if free_space < space_last:
                for j in range(0, free_space):
                    checksum += multiplying_index*index_last
                    st += str(index_last)
                    multiplying_index += 1
                file_ids[index_last] = space_last - free_space
                free_space = 0
            
            elif free_space >= space_last:
                for j in range(0, space_last):
                    checksum += multiplying_index*index_last
                    st += str(index_last)
                    multiplying_index += 1
                file_ids[index_last] = 0
                free_space -= space_last
                index_last -= 1

print(checksum)