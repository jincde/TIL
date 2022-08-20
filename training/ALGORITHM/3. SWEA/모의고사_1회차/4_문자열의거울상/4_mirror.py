'''
b --> d
d --> b
p --> q
q --> p
'''

T = int(input()) # 테스트 케이스 개수 입력

for i in range(1, T+1): # 테스트 케이스만큼 반복
    input_str = input()[::-1]
    mirror_str = ''

    for j in range(len(input_str)):
        if input_str[j] == 'b':
            mirror_str += 'd'
        elif input_str[j] == 'd':
            mirror_str += 'b'
        elif input_str[j] == 'p':
            mirror_str += 'q'
        else:
            mirror_str += 'p'
    print(f'#{i} {mirror_str}')
