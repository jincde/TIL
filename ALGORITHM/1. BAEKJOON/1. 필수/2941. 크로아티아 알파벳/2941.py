HR_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
t = input()

for i in HR_alphabet:
    t = t.replace(i, '*')

print(len(t))