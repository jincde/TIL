num1, num2 = map(int, input().split())
result_gcd = []

#최대 공약수
for i in range(min(num1, num2), 1, -1):
    if num1 % int(i) == 0 and num2 % int(i) == 0:
        result_gcd.append(i)

print(max(result_gcd)) 
print(num1 * num2 / max(result_gcd))

#최소 공배수
# for i in range(max(num1, num2), (num1 * num2)+1):
#     if i % num1 == 0 and i % num2 == 0:
#         print(i)
#         break   