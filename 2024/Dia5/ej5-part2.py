with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

posterior = {}
incorrect_updates = []
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
        if not correct_update:
            corr_update = update
            i = 0
            while i < len(corr_update):
                j = i + 1
                correction = False
                while j < len(corr_update):
                    if corr_update[i] in posterior[corr_update[j]]:
                        corr_update[i], corr_update[j] = corr_update[j], corr_update[i]
                        correction = True
                        continue
                    j = j + 1

                if not correction:
                    i += 1

            result += corr_update[(len(corr_update) - 1) // 2]

print(result)