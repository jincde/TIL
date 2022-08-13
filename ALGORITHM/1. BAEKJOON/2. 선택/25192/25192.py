# 25192. 인사성 밝은 곰곰이

from re import I


T = int(input())

arr = []
for _ in range(T):
    arr.append(input())
    
    for i in range(len(arr)):
        if 'ENTER' in arr:
            arr.pop()
        else:
            pass
        
print(len(set(arr)))