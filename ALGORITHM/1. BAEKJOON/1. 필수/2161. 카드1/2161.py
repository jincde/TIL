from collections import deque

N = int(input()) # N장의 카드
stack_N = []
pop_N = []

for i in range(1, N+1): # 1이 맨위로 적재될 수 있게끔 반복문 작성
    stack_N.append(i)

while 1:
    pop_N.append(stack_N.pop(0)) # pop_N리스트에 stack_N리스트 첫번째를 추가
    if not stack_N:
        break
    stack_N.append(stack_N.pop(0)) # 두번째를 맨뒤로 이동
        
print(*pop_N) 