T = int(input()) # 테스트 케이스 개수
d = 0 # 구하고자 하는 변의 길이

for i in range(1, T+1): # 테스트 케이스 개수만큼 반복
    a, b, c = map(int, input().split()) # 세 변의 길이를 입력
    
    if a == b: # a와 b의 길이가 같다면 c와 d의 길이가 같다
        d = c
        print(f'#{i} {d}')
    elif b == c: # b와 c의 길이가 같다면 a와 d의 길이가 같다
        d = a
        print(f'#{i} {d}')
    else:
        d = b
        print(f'#{i} {d}')