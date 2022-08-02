# T = '6471-6836-9525-5276'
# T2 = '3029192045012901'

# 34569로 시작
# 12 78
# print(len(T))
# print(len(T2))

T = int(input()) # 횟수

for i in range(1, T+1): # 입력받은 횟수만큼 반복
    Card_number = list(input()) # 문자열로 입력
    print(len(Card_number))
    if len(Card_number) != 16 or 19:
        print(f"{i} 0")
    elif int(Card_number[0]) == 1:
        print(f"#{i} 0")
    elif int(Card_number[0]) == 2:
        print(f"#{i} 0")
    elif int(Card_number[0]) == 7:
        print(f"#{i} 0")
    elif int(Card_number[0]) == 8:
        print(f"{i} 0")
    else:
        print(f"#{i} 1")