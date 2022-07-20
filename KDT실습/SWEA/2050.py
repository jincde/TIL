import sys
sys.stdin = open('input.txt', 'r')

abc_list = sys.stdin.readline()

for i in range(len(abc_list)):
    print(ord(abc_list[i])-64, end = ' ')