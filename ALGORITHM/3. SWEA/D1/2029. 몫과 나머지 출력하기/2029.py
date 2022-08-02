import sys
sys.stdin = open("input.txt", "r")

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print("#%d %d %d" % (i+1, a//b, a%b))