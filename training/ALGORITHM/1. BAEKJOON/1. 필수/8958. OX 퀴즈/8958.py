T = int(input())

for i in range(T):
    input_ox = list(map(str, input()))
    cnt = 1
    result = 0

    for i in input_ox:
        if i == 'O':
            result += cnt
            cnt += 1
        else:
            cnt = 1

    print(result)