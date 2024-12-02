with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

def create_combs(numbers):
    result = []
    for i in range(len(numbers)):
        result.append(numbers[:i] + numbers[i+1:])
    return result

reports = 0
for line in input:
    nums = [int(x) for x in line.split(" ")]
    combs = create_combs(nums)
    for c in combs:
        safe = True
        if c[0] > c[1]:
            for i in range(0, len(c) - 1):
                if not (c[i] > c[i+1] 
                        and 1 <= abs(c[i] - c[i+1]) 
                        and abs(c[i] - c[i+1]) <= 3):
                    safe = False
                    break

        elif c[0] < c[1]:
            for i in range(0, len(c) - 1):
                if not (c[i] < c[i+1] 
                        and 1 <= abs(c[i] - c[i+1]) 
                        and abs(c[i] - c[i+1]) <= 3):
                    safe = False
                    break
        
        else:
            safe = False

        if safe:
            reports += 1
            break
        

print(reports)