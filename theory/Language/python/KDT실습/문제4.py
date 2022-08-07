# n = 5
n = int(input())


#==========
# while
i = 1
total = 1

while i <= n:
    total = total * i
    i = i + 1

print(total)


#==========
# for
i = 1
total = 1

for i in range(1, n+1):
    total = total * 1
    i = i + 1

print(total)