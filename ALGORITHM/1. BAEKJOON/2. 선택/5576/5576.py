# 5576. 콘테스트
import sys
sys.stdin = open('input.txt', )

W = []
K = []

for _ in range(10):
    W.append(int(input()))

for _ in range(10):
    K.append(int(input()))

W.sort(reverse=True)
K.sort(reverse=True)

W_SUM = 0
K_SUM = 0
for i in range(3):
    W_SUM += W[i]
    K_SUM += K[i]

print(W_SUM, K_SUM)