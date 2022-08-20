# 백준3052. 나머지
import sys
T = open('input.txt', 'r', encoding='utf-8')
result = []

for i in T:
    result.append(int(i) % 42)

print(len(set((result))))