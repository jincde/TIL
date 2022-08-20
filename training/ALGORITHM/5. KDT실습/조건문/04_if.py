#조건 표현식
num = -10

if num >= 0:
    value = num
else:
    value = -num
print(num, value)

#조건 표현식으로 작성
value = num if num >=0 else -num
