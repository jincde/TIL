N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A-B) + len(B-A))