# 1764. 듣보잡

N, M = map(int, input().split())
listen, see = set(), set()
both = []

for _ in range(N):
    listen.add(input())
for _ in range(M):
    see.add(input())

both = sorted(listen & see)

print(len(both))
for i in both:
    print(i)