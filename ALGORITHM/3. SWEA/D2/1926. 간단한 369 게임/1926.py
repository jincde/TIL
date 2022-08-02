# 간단한 369 게임

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    i = str(i)
    c = i.count('3') + i.count('6') + i.count('9')

    if c == 0:
        print(i, end=' ')
    else:
        print('-' * c, end=' ')