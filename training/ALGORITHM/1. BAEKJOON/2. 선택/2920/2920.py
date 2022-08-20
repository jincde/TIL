# 2920. 음계

T = list(input().split())

asc = ['1','2','3','4','5','6','7','8']
desc = ['8','7','6','5','4','3','2','1']

if T == asc:
    print('ascending')
elif T == desc:
    print('descending')
else:
    print('mixed')