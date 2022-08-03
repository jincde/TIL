T = int(input())

for i in range(T):
    N, S = input().split()
    N = int(N)
    S_list = []

    for j in S:
        S_list.append(j)
    S_list.pop(N-1)

    print(*S_list, sep='')