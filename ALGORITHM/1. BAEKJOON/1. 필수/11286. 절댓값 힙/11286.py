import heapq
import sys

N = int(input())
arr = []

for i in range(N):
    x = int(sys.stdin.readline())
    
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr)[1])