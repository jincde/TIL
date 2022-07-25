T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    sum = int(a) + int(b)

    print(f'Case #{i}: {a} + {b} = {sum}')