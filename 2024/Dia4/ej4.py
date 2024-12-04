with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

times = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "X":
            if j+3 < len(input[i]) and input[i][j:j+4] == "XMAS":
                    times += 1
            if j-3 >= 0 and input[i][j-3:j+1][::-1] == "XMAS":
                    times += 1
            if i+3 < len(input) and (input[i][j]+input[i+1][j]+input[i+2][j]+input[i+3][j]) == "XMAS":
                    times += 1
            if i-3 >= 0 and (input[i][j]+input[i-1][j]+input[i-2][j]+input[i-3][j]) == "XMAS":
                    times += 1
            if j-3 >= 0 and i+3 < len(input) and (input[i][j]+input[i+1][j-1]+input[i+2][j-2]+input[i+3][j-3]) == "XMAS":
                    times += 1
            if j-3 >= 0 and i-3 >= 0 and (input[i][j]+input[i-1][j-1]+input[i-2][j-2]+input[i-3][j-3]) == "XMAS":
                    times += 1
            if i-3 >= 0 and j+3 < len(input[i]) and (input[i][j]+input[i-1][j+1]+input[i-2][j+2]+input[i-3][j+3]) == "XMAS":
                    times += 1
            if i+3 < len(input) and j+3 < len(input[i]) and (input[i][j]+input[i+1][j+1]+input[i+2][j+2]+input[i+3][j+3]) == "XMAS":
                    times += 1
                    
print(times)

