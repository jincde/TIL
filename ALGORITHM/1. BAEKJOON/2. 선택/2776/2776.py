# 2776. 암기왕

T = int(input())

for _ in range(T):
    N = int(input())
    note_1 = list(input().split())

    M = int(input())
    note_2 = input().split()
    
    result = []
    for i in range(len(note_2)):
        if note_2[i] in note_1:
            result.append(1)
        else:
            result.append(0)

    for j in result:
        print(j)