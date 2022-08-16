# 2615. 오목
import sys
from pprint import pprint

sys.stdin = open('input.txt')

BLACK = 1
WHITE = 2
N = 19

# 우, 하, 우상, 우하
dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]

board = []

for _ in range(N):
    temp_list = list(map(int,input().split()))
    board.append(temp_list)

for x in range(N):
    for y in range(N):
        # 델타 탐색
        for d in range(4):
            stone_count = 0
            # 다음 좌표 탐색
            nx = x + dx[d]
            ny = y + dy[d]

            while True:
                # 예외처리
                if not(ny -1 < ny < N and -1 < nx < N):
                    break
                if not(board[x][y] == board[nx][ny]):
                    break

                stone_count += 1

                nx = nx + dx[d]
                ny = ny + dy[d]

            if stone_count == 5:
                prev_x = x - dx[d]
                prev_y = y - dx[d]

                # if not(-1 < prev_x < N and -1 < prev_y < N):
                # if board[x][y] != board[prev_x][prev_y]:

                if not(-1 < prev_x < N and -1 < prev_y < N) or board[x][y] != board[prev_x][prev_y] 