# 10816. 숫자 카드 2


N = int(input())
arr_N = list(map(int, input().split()))

M = int(input())
arr_M = list(map(int, input().split()))

hash = {}

for i in arr_N:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in arr_M:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')