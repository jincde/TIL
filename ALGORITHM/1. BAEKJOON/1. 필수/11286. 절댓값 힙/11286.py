import heapq

N = int(input())
arr = []

for i in range(N):
    x = int(input())
    
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr)[1])