# 태보태보 총난타

T = list(input().split('(^0^)'))

left_hook = 0
right_hook = 0

for i in T[0]:
    if i == '@':
        left_hook += 1

for i in T[1]:
    if i == '@':
        right_hook += 1

print(left_hook, right_hook)