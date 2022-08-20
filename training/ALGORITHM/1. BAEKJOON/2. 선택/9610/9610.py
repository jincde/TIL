# 9610. 사분면

T = int(input())

x_y = []
for i in range(T):
    x_y.append(list(map(int, input().split())))
    Q1 = 0
    Q2 = 0
    Q3 = 0
    Q4 = 0
    Axis = 0

    for j in x_y:
        if j[0] == 0 or j[1] == 0:  # (0, 0)
            Axis += 1
        elif j[0] > 0 and j[1] > 0: # (+x, +y)
            Q1 += 1
        elif j[0] < 0 and j[1] > 0: # (-x, +y)
            Q2 += 1
        elif j[0] < 0 and j[1] < 0: # (-x, -y)
            Q3 += 1
        elif j[0] > 0 and j[1] < 0: # (+x, -y)
            Q4 += 1

print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AXIS: {Axis}')
