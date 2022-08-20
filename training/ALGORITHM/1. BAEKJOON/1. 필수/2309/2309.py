# 2309. 일곱 난쟁이
# 브루트포스

person = []
sum = 0

for i in range(9):
    person.append(int(input()))
    sum += person[i]

for i in range(9):
    for j in range(i+1, 9):
        if sum - (person[i] + person[j]) == 100:
            p1, p2 = person[i], person[j]
            break
    
person.remove(p1)
person.remove(p2)
person.sort()

for i in person:
    print(i)