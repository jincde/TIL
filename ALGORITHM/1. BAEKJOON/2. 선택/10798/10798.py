# 10798. 세로읽기
matrix = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(matrix[i]):
            print(matrix[i][j], end='')

# 틀린 코드
# 10798. 세로읽기
# matrix = [list(input().split()) for i in range(5)]
# result = []

# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         result.append(matrix[j][i])
#     if " " in result:
#         result.pop(matrix[j][i])

# print(result)