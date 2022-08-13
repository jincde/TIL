# 6996. 에너그램
# abba = baab

T = int(input())

for _ in range(T):
    a, b = map(str, input().split())

    list_a = sorted(list(a)) # list를 왜 씌워야할까?
    list_b = sorted(list(b))

    if list_a == list_b:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')