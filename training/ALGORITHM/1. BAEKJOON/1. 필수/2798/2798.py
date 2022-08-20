# 2798. 블랙잭

N, M = map(int, input().split())
card = list(map(int, input().split()))
answer = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] > M:
                continue
            else:
                answer = max(answer, card[i]+card[j]+card[k])

print(answer)