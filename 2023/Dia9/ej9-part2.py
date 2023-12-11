with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

total = 0
for line in input:
    nums = [int(n) for n in line.split(" ")]
    first_pos = [nums[0]]
    while True:
        if nums.count(0) == len(nums):
            value = 0
            for n in first_pos[1:]:
                value = n-value
            total += value
            break
        else:
            copy = nums
            nums = []
            for i in range(len(copy)-1):
                nums.append(copy[i+1]-copy[i])
            first_pos = [nums[0]] + first_pos

print(total)    