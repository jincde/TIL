nums = int(input("리스트에 들어갈 숫자의 갯수는? "))
lst = []

for i in range(0, nums):
    numbers = int(input("숫자를 입력하세요 : "))
    lst.append(numbers)

avg = sum(lst) / nums

print(avg)