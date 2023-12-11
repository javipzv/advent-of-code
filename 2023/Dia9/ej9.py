with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

total = 0
for line in input:
    nums = [int(n) for n in line.split(" ")]
    last_pos = [nums[len(nums)-1]]
    while True:
        if nums.count(0) == len(nums):
            total += sum(last_pos)
            break
        else:
            copy = nums
            nums = []
            for i in range(len(copy)-1):
                nums.append(copy[i+1]-copy[i])
            last_pos = [nums[len(nums)-1]] + last_pos

print(total)    