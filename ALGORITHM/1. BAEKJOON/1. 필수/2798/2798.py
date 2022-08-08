N, M = map(int, input().split()) # N장, 최대점수M
card = list(map(int, input().split()))
answer = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(i+2, N):
            if card[i] + card[j] + card[k] > M:
                continue
            else:
                answer = max(answer, card[i]+card[j]+card[k])

print(answer)