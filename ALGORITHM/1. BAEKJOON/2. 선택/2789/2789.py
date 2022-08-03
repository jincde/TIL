# # 2789. 유학금지

T = list(input())
cancer = 'CAMBRIDGE'

for i in cancer:
    for j in range(len(T)):
        if i == T[j]:
            T[j] = ''

for i in T:
    print(i, end='')