# # 2669. 직사각형 네개의 합집합의 면적 구하기

# # 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고 
# # 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다. 
# # 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.

# rec = []
# # 직사각형 면적 = 가로 * 세로
# for i in range(4):
#     a, b, x, y = map(int, input().split())
#     rec.append((a+x) * (b+y))
#     #가로길이 = 첫번째 + 세번째
#     #세로길이 = 두번째 + 네번째

# print(rec)

arr = [[0]*100 for _ in range(100)] # 100 * 100 행렬 (0행렬)
for _ in range(4): # 4개의 사각형
    x1, y1, x2, y2 = map(int, input().split()) # 각각 값을 입력
    for i in range(x1, x2): 
        for j in range(y1, y2):
            arr[i][j] = 1 # 좌표로 찍힌 부분(인덱스)를 전부 1로 바꿔줌
print(sum(sum(arr,[]))) # 0행렬 전부의 값을 더한다