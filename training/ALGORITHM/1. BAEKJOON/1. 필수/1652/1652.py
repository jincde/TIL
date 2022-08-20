# 1652. 누울 자리를 찾아라

N = int(input()) # N값 입력
matrix = [list(map(str, input())) for _ in range(N)] # N * N 크기의 정사각형 

row = 0 # 가로 - 행
col = 0 # 세로 - 열

# 행 개수
for i in range(N):
    cnt = 0
    for j in range(N):
        if matrix[i][j] == '.': # 순회 중 .을 만나면 cnt += 1
            cnt += 1
        elif matrix[i][j] == 'X': # 순회 중 X를 만나면 
            if cnt >= 2: # cnt가 2보다 크거나 같다면
                row += 1 # 행의 개수를 추가
            cnt = 0 # cnt는 0으로 초기화
    if cnt >= 2: # ..X..의 경우를 위한 if문
        row += 1
    cnt = 0

# 열 개수
for j in range(N):
    cnt = 0
    for i in range(N):
        if matrix[i][j] == '.':
            cnt += 1
        elif matrix[i][j] == 'X':
            if cnt >= 2:
                col += 1
            cnt = 0
    if cnt >= 2:
        col += 1
    cnt =0

print(row, col)