# 9325. 얼마?

T = int(input())

for i in range(T):
    price = int(input())
    option = int(input())

    # if option == 0:
    #     print(price)

    total = []
    for j in range(option):
        number, optionPrice = map(int, input().split())
        total.append(number * optionPrice)
    print(price + sum(total))

'''
2
10000
2
1 2000
3 400
50000
0
'''