dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

input_dial = input()
result_sum = 0

for i in input_dial:
    for j in dial_list:
        if i in j:
            result_sum += dial_list.index(j)+3

print(result_sum)