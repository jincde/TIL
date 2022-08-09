# 2587. 대표값2

arr = []
for i in range(5):
    arr.append(int(input()))

arr.sort()

print(sum(arr) // 5)
print(arr[2])