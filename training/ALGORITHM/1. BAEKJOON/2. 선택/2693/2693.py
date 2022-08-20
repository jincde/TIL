# 2693. N번째 큰 수

N = int(input())

for i in range(N):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr[2])