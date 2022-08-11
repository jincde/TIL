# 2857. FBI

agents = []
FBI = []
for _ in range(5):
    agents.append(input())

for i in range(len(agents)):
    if 'FBI' in agents[i]:
        print(i+1, end=' ')
        FBI.append(agents[i])

if not FBI:
    print('HE GOT AWAY!')