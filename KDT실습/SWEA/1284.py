# 수도 요금 경쟁

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    value_A = W * P # 리터당 가격
    value_B = Q
    if R < W: # 기본 사용량보다 많을 때
        value_B += S * (W - R)

    result = min(value_A, value_B)

    print(f'#{i} {result}')