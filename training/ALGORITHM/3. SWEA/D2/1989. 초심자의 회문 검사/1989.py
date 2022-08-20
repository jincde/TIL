# 초심자의 회문 검사

import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for i in range(1, T+1):
    s = input()

    if s == s[::-1]:
        print(f"#{i} {1}")
    else:
        print(f"#{i} {0}")