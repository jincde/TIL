# 1302. 베스트셀러

''' 첫번째 코드 '''
# T = int(input())
# arr = []
# hash = {}

# for i in range(T):
#     arr.append(input())

# for i in arr:
#     if i in hash:
#         hash[i] += 1
#     else:
#         hash[i] = 1

# print(max(hash.keys()))

''' 두번째 코드 '''
T = int(input())

hash = {}

for i in range(T):
    book = input()
    if book in hash:
        hash[book] += 1
    else:
        hash[book] = 1
max_ = max(hash.values())

arr = []
for i in hash:
    if max_ == hash[i]:
        arr.append(i)

arr.sort()
print(arr[0])