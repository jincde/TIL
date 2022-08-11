# 20001. 고무오리 디버깅

# 고무오리 디버깅 시작
# '문제'가 들어오면 스택에 append
# '고무오리'가 들어오면 스택에서 pop
# '고무오리 디버깅 끝'
# 스택이 비어있으면 - 고무오리야 사랑해 else: 힝구


duck = input()
stack = []

while duck != '고무오리 디버깅 끝':
    duck = input()
    
    if duck == '문제':
        stack.append(duck)
    elif duck == '고무오리':
        if stack:
            stack.pop()
        else: 
            stack.append('문제')
            stack.append('문제')

if not stack:
    print('고무오리야 사랑해')
else:
    print('힝구')