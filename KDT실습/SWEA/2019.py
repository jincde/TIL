# 더블더블 !!
# 1부터 주어진 횟수까지 2를 곱한 값

N = int(input())
i = 2

for j in range(N+1):
    number = i ** j
    print(number, end=" ")