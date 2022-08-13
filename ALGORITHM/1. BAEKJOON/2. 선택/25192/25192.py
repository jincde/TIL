# 25192. 인사성 밝은 곰곰이

N = int(input())

cnt = 0
dic = {}

for _ in range(N):
    user = input()

    if user == 'ENTER': # ENTER가 들어오면
        for key, value in dic.items(): # 튜플 (key, value)
            if value == 1: # value마다 카운트
                cnt += 1
        dic = {} # 딕셔너리 초기화
        
    else:
        if user not in dic: # user ID가 딕셔너리에 없다면
            dic[user] = 1 # 딕셔너리에 추가

for key, value in dic.items():
    if value == 1:
        cnt += 1

print(cnt)
    
    
'''
7
ENTER
pjshwa
chansol
chogahui05
ENTER
pjshwa
chansol
'''