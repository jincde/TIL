import heapq

N = int(input())
arr = []

for i in range(N):
    number = int(input())
    heapq.heappush(arr, number)
    
for j in range(N):
    print(heapq.heappop(arr))