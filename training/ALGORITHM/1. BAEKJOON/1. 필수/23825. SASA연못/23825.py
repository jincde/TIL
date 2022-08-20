# 백준: 23825. SASA연못

# S와 A의 갯수를 입력받는 두 개 변수 선언
input_S, input_A = map(int, input().split())

# S와 A를 2로 나눈 값을 저장하는 두 개 변수 선언
result_S = input_S // 2
result_A = input_A // 2

# 두 개 변수 중 작은 값을 출력
print(min(result_S, result_A))