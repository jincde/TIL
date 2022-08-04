# 2592. 대표값
from collections import Counter
numbers = []

for i in range(10):
    numbers.append(int(input()))
    
cnt = Counter(numbers)
numbers_AVG = sum(numbers) // len(numbers)
mode = cnt.most_common(1) # 상위 요소 하나를 리턴 [입력값][빈도수]


# 최종 output
print(numbers_AVG)
print(mode[0][0])