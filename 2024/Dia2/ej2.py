with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

reports = 0
for line in input:
    nums = [int(x) for x in line.split(" ")]
    safe = True
    if nums[0] > nums[1]:
        for i in range(0, len(nums) - 1):
            if not (nums[i] > nums[i+1] 
                    and 1 <= abs(nums[i] - nums[i+1]) 
                    and abs(nums[i] - nums[i+1]) <= 3):
                safe = False
                break

    elif nums[0] < nums[1]:
        for i in range(0, len(nums) - 1):
            if not (nums[i] < nums[i+1] 
                    and 1 <= abs(nums[i] - nums[i+1]) 
                    and abs(nums[i] - nums[i+1]) <= 3):
                safe = False
                break
    
    else:
        safe = False

    if safe:
        reports += 1
        

print(reports)