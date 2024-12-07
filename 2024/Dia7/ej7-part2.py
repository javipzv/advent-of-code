with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

total = 0
for line in input:
    sep = line.split(": ")
    target = int(sep[0])
    nums = [int(x) for x in sep[1].split(" ")]
    
    keep = [nums[0]]
    for i in range(len(nums)):
        if i == 0:
            new_keep = [nums[0]]

        else:
            new_keep = []
            for n in keep:
                new_keep.append(n+nums[i])
                new_keep.append(n*nums[i])
                new_keep.append(int(str(n) + str(nums[i])))

        keep = new_keep

    if target in new_keep:
        total += target

print(total)