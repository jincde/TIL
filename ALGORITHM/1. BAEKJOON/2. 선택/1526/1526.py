# 1526. 가장 큰 금민수
# 500을 입력하면 477을 출력 (4와 7로만 이뤄진 숫자 중 가장 큰 수)

T = int(input())

for i in range(T, 0, -1):
    if i % 10 == 4 or i % 10 == 7:
        i /= 10
        break