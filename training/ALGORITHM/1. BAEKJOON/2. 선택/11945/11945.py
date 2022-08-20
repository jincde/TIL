from audioop import reverse


N, M = map(int, input().split())

for i in range(N):
    digit = list(input())
    digit.reverse()
    print(*digit, sep='')