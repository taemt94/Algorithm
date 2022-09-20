line = input()
numbers = []
operators = []
number = ''
for i, char in enumerate(line):
    if char.isnumeric() and i < len(line) - 1:
        number += char
    else:
        if char == '+' or char == '-':
            operators.append(char)
        else:
            number += char
        numbers.append(int(number))
        number = ''
        
i = 0
answer = numbers[i]
i += 1
if '+' not in operators:
    answer -= sum(numbers[i:])
    print(answer)
elif '-' not in operators:
    answer = sum(numbers)
    print(answer)
else:
    j = 0
    while True:
        if operators[j] == '+':
            answer += numbers[i]
            i += 1
            j += 1
        else:
            tmp_sum = numbers[i]
            i += 1
            if j+1 < len(operators) and operators[j+1] == '-':
                j += 1
            else:
                while j+1 < len(operators) and operators[j+1] == '+':
                    tmp_sum += numbers[i]
                    i += 1
                    j += 1
                j += 1                    
            answer -= tmp_sum
        if j == len(operators):
            break            
    print(answer)
            