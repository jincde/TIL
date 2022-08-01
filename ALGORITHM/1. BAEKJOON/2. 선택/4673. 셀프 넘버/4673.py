def selfNumber(n):
    number = n

    for i in list(str(n)):
        number += int(i)
    return number

arr = []

for i in range(1, 10001):
    arr.append(selfNumber(i))

for j in range(1, 10001):
    if j not in arr:
        print(j)