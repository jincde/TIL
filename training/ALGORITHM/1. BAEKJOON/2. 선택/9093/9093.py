# 9093. 단어 뒤집기

T = int(input())

for i in range(T):
    arr = list(input().split())
    for j in arr:
        print(j[::-1], end=' ')