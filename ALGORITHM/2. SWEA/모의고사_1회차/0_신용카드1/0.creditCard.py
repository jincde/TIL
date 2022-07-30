T = int(input())
N = 0

for i in range(1, T+1):
    card_number = input().split()
    result_N = 0

    for j in range(15):
        if j % 2 == 0:
            result_N += int(card_number[j]) * 2 # 홀수 자리면 그냥 더하기

        else:
            result_N += int(card_number[j]) # 짝수 자리면 2곱하기

        q1 = result_N # 비교를 위한 변수
        for tc in range(11): # 0부터 10까지 하나하나 더하기
            q1 = result_N
            q1 = q1 + tc
            if q1 % 10 == 0: # 0부터 10까지 더했을때 10으로 나눠지면 그 값이 N
                break # break
            else: # 10으로 나눠지지 않으면 
                q1 = result_N + tc
    print(f'#{i} {tc}')

'''
4 5 2 0 0 2 0 0 1 9 0 0 4 0 6
6 9 0 9 7 0 1 9 9 8 6 3 0 8 7
'''