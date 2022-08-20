# 17388. 와글와글 숭고한

list = list(map(int, input().split()))

if sum(list) >= 100:
    print('OK')
else:
    if min(list) == list[0]:
        print('Soongsil')
    elif min(list) == list[1]:
        print('Korea')
    else:
        print("Hanyang")