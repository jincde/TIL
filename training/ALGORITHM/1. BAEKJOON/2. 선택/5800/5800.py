# 5800. 성적 통계

T = int(input())

for i in range(1, T+1):
    gap = []

    studentScore = list(map(int, input().split()))
    student = studentScore[0]
    score = sorted(studentScore[1::], reverse = True)

    for j in range(len(score)-1):
        gap.append(int(score[j] - score[j+1]))
        
    print(f'Class {i}')
    print(f'Max {score[0]}, Min {score[-1]}, Largest gap {max(gap)}')