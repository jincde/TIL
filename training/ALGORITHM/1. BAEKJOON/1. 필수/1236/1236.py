# 백준
# 1236. 성지키기

N, M = map(int, input().split())
cnt_row = 0 # 행 마다 최소 1명씩
cnt_col = 0

matrix = [list(input()) for i in range(N)]

for i in matrix:
    if 'X' not in i:
        cnt_row += 1
    else:
        pass

for i in range(M):
    col = []
    for j in range(N):
        col.append(matrix[j][i])
    if 'X' not in col:
        cnt_col += 1


print(max(cnt_row, cnt_col))