# 백준
# 2167. 2차원 배열의 합

N, M = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for i in range(N)]
result = []
# print(matrix)

K = int(input())
for _ in range(K):
    i, j, x, y = list(map(int, input().split()))
    result = matrix[i-1][j-1] + matrix[x-1][y-1]
    print(result)

for i in result:
    print(i)