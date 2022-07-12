numbers = [0, 20, 100, 11, 22]
num1 = numbers[0]
num2 = numbers[1]

if num1 < num2:
    temp = num1
    num1 = num2
    num2 = temp

for i in numbers:
    if i > num1:
        num2 = num1
        num1 = i
    elif i == num1:
        continue
    else:
        if num1 >= num2:
            num2 = i
print(num2)