with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

posterior = {}
result = 0
for line in input:
    if "|" in line:
        nums = [int(x) for x in line.split("|")]
        if nums[0] in posterior:
            posterior[nums[0]].append(nums[1])
        else:
            posterior[nums[0]] = [nums[1]]
    elif line == "":
        pass
    else:
        correct_update = True
        update = [int(x) for x in line.split(",")]
        for i in range(len(update)):
            for j in range(i, len(update)):
                if update[i] in posterior[update[j]]:
                    correct_update = False
                    break
            if not correct_update:
                break
        if correct_update:
            result += update[(len(update) - 1) // 2]

print(result)

