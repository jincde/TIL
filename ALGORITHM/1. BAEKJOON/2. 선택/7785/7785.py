# 7785. 회사에 있는 사람

T = int(input())
hash = {}

for i in range(T):
    name, work = input().split()
    if work == 'enter':
        hash[name] = ''
    else:
        del(hash[name])

for i in sorted(hash.keys(), reverse=True):
    print(i)