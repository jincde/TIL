# 1543. 문서 검색

s = input()
target = input()

i = 0
cnt = 0

while i <= len(s) - len(target):
    if s[i:i + len(target)] == target:
        cnt += 1
        i += len(target)
    else:
        i += 1

print(cnt)