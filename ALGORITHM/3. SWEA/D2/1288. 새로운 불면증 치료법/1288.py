# 새로운 불면증 치료법

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    N = input()
    value = int(N)
    data = [0] * 10

    while True:
        for j in range(len(N)):
            data[int(N[j])] += 1
        
        if not data.count(0):
            print(f"#{i} {int(N)}")
            break

        N = str(value + int(N))