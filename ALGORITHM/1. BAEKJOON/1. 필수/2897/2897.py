'''

..XX.
.#XX.
..#..
.....

'''

# 2897. 몬스터 트럭

R, C = map(int, input().split()) # 행과 열의 개수 입력
arr = []

for i in range(R): # R*C 행렬
    arr.append(input())

car0 = 0 # 0대 주차RM
car1 = 0 # 1대 주차
car2 = 0 # 2대 주차
car3 = 0 # 3대 주차
car4 = 0 # 4대 주차

for r in range(R):
    for c in range(C):
        if r + 1 == R or c + 1 == C: # 행 또는 열의 끝에 break
            break

        w = arr[r][c] # 2 x 2 행렬 선택을 위한 값
        x = arr[r][c+1]
        y = arr[r+1][c]
        z = arr[r+1][c+1]

        twoXtwo = w+x+y+z # 2 x 2 행렬의 값들을 저장
                          # ex) ...X, XX..

        if '#' in twoXtwo: # 빌딩을 만나면 continue
            continue
        else:
            parkingCar = twoXtwo.count('X') # X의 개수를 count
            if parkingCar == 0:
                car0 += 1
            elif parkingCar == 1: # X가 한 개면 주차되어 있는 차 한 대를 파괴
                car1 += 1
            elif parkingCar == 2:
                car2 += 1
            elif parkingCar == 3:
                car3 += 1
            elif parkingCar == 4:
                car4 += 1

print(car0)
print(car1)
print(car2)
print(car3)
print(car4)