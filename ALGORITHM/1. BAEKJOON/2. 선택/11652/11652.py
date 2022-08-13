# 11652. 카드
from collections import Counter
'''
N = int(input())

card = []
for i in range(N):
    card.append(input())

cntCard = sorted(Counter(card).most_common(1))
print(cntCard)
'''

N = int(input())
cards = set()

for _ in range(N):
    card = input()

    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1

# 풀이중
