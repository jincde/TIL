# 2864. 5와 6의 차이

n, m = input().split()

min = int(n.replace('6', '5')) + int(m.replace('6', '5'))
max = int(n.replace('5', '6')) + int(m.replace('5', '6'))

print(min, max)