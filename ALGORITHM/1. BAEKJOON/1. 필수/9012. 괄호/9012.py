T = int(input()) # 테스트케이스 개수 입력

for i in range(T):
    PS_input = input() # 괄호 입력
    VPS_list = [] # 스택생성
    
    for j in PS_input: # 입력 문자열 순회
        if j == '(': # '('가 나오면 스택에 푸시
            VPS_list.append(j)
        elif j == ')': 
            if VPS_list: # ')'가 나오면 스택에서 팝
                VPS_list.pop()
            else: # 괄호가 없다면 ')'만 남기때문에 NO
                print('NO')
                break
    else:
        if VPS_list: # 스택에 괄호가 남아있다면 NO
            print('NO')
        else: # 스택이 비어있다면 YES
            print('YES')