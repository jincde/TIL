# 10995. 별찍기-20

T = int(input())

for i in range(1, T+1):
    if i % 2 == 0:
        print(' *' * T)
    else:
        print('* ' * T)