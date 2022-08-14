# 15953. 상금 헌터

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    rewards = []

    if a == 1:
        rewards.append(500)
    elif 2 <= a <= 3:
        rewards.append(300)
    elif 4 <= a <= 6:
        rewards.append(200)
    elif 7 <= a <= 10:
        rewards.append(50)
    elif 11 <= a <= 15:
        rewards.append(30)
    elif 16 <= a <= 21:
        rewards.append(10)
    
    if b == 1:
        rewards.append(512)
    elif 2 <= b <= 3:
        rewards.append(256)
    elif 4 <= b <= 7:
        rewards.append(128)
    elif 8 <= b <= 15:
        rewards.append(64)
    elif 16 <= b <= 31:
        rewards.append(32)

    print(sum(rewards) * 10000)