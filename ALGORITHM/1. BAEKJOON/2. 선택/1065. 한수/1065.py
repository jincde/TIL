T = int(input())
result = 0

for i in range(1, T+1):
    if i < 100:
        result += 1
    else:
        split_num = list(map(int, str(i)))
        
        if split_num[0] - split_num[1] == split_num[1] - split_num[2]:
            result += 1

print(result)