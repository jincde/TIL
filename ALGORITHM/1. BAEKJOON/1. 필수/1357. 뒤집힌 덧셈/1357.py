num1, num2 = input().split()

num1 = int(num1[::-1])
num2 = int(num2[::-1])

print(int((str(num1+num2)[::-1])))