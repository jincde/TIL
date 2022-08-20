# 4949. 균형잡힌 세상

while True:
    a = input()
    stack = []

    if a == '.':
        break

    for i in a:
        if i == '[' or '(':
            stack.append(i)
        else:
            
            # 풀이중