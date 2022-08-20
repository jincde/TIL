# 1371. 가장 많은 글자

import sys

sentence = sys.stdin.read()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
answer = []

for i in alphabet:
    answer.append(sentence.count(i))

max_ = max(answer)
for j in range(len(answer)):
    if max_ == answer[j]:
        print(chr(i+97), end = ' ')