import sys
sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())

for i in range(1, T + 1):
    numbers = list(map(int, input().split()))
    avg = sum(numbers) / len(numbers)
    avg = round(avg)
    print("#%d %d" % (i, avg))