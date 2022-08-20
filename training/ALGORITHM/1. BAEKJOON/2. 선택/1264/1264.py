# 1264. 모음의 개수

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    cnt = 0
    word = input().lower()

    if word == '#':
        break
    
    for i in word:
        if i in vowels:
            cnt += 1
    print(cnt)