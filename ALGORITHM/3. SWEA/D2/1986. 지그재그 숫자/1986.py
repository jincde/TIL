# 지그재그 숫자

T = int(input())
for tc in range(1,T+1):
    a = int(input())
    total = 0

    for i in range(1,a+1):
        if i % 2:
            total += i
        else:
            total -=i
    
    print(f'#{tc} {total}')