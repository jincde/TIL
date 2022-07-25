a = int(input())
b = int(input())
c = int(input())

result = a * b * c

for i in range(10):
    print(str(result).count(str(i)))