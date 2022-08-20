t = input().upper()
t_list = list(set(t))
cnt_list = []

for i in t_list:
    cnt = t.count(i)
    cnt_list.append(cnt)
    
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_result = cnt_list.index(max(cnt_list))
    print(t_list[max_result])