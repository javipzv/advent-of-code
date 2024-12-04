with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

times = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "A":
            if i-1 >= 0 and i+1 < len(input) and j-1 >= 0 and j+1 < len(input[i]):
                first_diagonal = input[i-1][j-1]+"A"+input[i+1][j+1]
                second_diagonal = input[i+1][j-1]+"A"+input[i-1][j+1]
                if (first_diagonal == "MAS" or first_diagonal == "SAM") and \
                   (second_diagonal == "MAS" or second_diagonal == "SAM"):
                    times += 1
print(times)