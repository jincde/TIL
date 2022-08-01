T = int(input())

for i in range(T):
    cnt, S = input().split()
    
    for j in S:
        print(j * int(cnt), end='')
    print()