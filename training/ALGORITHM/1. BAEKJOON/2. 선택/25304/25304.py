# 25304. 영수증

Total = int(input())
N = int(input())

arr = []
for i in range(N):
    price, M = map(int, input().split())
    arr.append(price * M)

if Total == sum(arr):
    print('Yes')
else:
    print('No')