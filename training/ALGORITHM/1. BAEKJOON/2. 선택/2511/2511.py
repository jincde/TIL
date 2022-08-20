# 2511. 카드놀이

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_score = 0
B_score = 0
winner = ''

for i in range(10):
    if A[i] > B[i]:
        A_score += 3
    elif B[i] > A[i]:
        B_score += 3
    else:
        A_score += 1
        B_score += 1
        winner = 'D'

if A_score > B_score:
    winner = 'A'
elif B_score > A_score:
    winner = 'B'
else:
    for j in reversed(range(10)):
        if A[j] == B[j]:
            continue
        elif A[j] > B[j]:
            winner = 'A'
            break
        elif B[j] > A[j]:
            winner = 'B'
            break
        else:
            winner = 'D'

print(A_score, B_score)
print(winner)