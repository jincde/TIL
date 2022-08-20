# 10101. 삼각형 외우기

triangle = []
for i in range(3):
    triangle.append(int(input()))

if sum(triangle) == 180:
    if len(set(triangle)) == 1:
        print('Equilateral')
    elif len(set(triangle)) == 2:
        print('Isosceles')
    elif len(set(triangle)) == 3:
        print('Scalene')
else:
    print('Error')