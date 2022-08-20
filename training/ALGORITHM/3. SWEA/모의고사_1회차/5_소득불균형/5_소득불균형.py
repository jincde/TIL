T = int(input()) # 전체 테스트 케이스
cnt = 0

for i in range(1, T+1): # 전체 테스트 케이스 개수만큼 반복
    tc = int(input()) # 각 테스트 케이스 개수 입력
    cnt = 0
    income = list(map(int, input().split()))
    result_income = sum(income)/tc

    for j in income:
        if int(j) <= result_income:
            cnt += 1
        else:
            continue

    print(f'#{i} {int(cnt)}')