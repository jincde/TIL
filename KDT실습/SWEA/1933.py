# 간단한 N의 약수!!
N = int(input())
result = []

for i in range(1, N+1):
    if N % i == 0:
        result.append(i)
        i += 1
    else:
        i += 1
        continue


print(result)