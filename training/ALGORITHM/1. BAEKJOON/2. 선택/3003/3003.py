# 3003. 킹, 퀸, 룩, 비숍, 나이트, 폰
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개

# 2 1 2 1 2 1 input
# 1 1 2 2 2 8 total
# 1 0 0 0 0 1 output

chess = [1, 1, 2, 2, 2, 8]
T = list(map(int, input().split()))
needs = []

for i in range(len(T)):
    if chess[i] > T[i]:
        needs.append(int(chess[i]) - T[i])
    elif T[i] == chess[i]:
        needs.append(0)
    elif T[i] > chess[i]:
        needs.append(int(chess[i]) - T[i])

print(*needs)