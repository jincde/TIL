# 10769. 행복한지 슬픈지

'''
어떤 이모티콘도 포함되어 있지 않으면, none 을 출력한다.
행복한 이모티콘과 슬픈 이모티콘의 수가 동일하게 포함되어 있으면, unsure 를 출력한다.
행복한 이모티콘이 슬픈 이모티콘보다 많이 포함되어 있으면, happy 를 출력한다.
슬픈 이모티콘이 행복한 이모티콘보다 많이 포함되어 있으면, sad 를 출력한다.
'''

S = input()

happy_cnt = S.count(':-)')
unhappy_cnt = S.count(':-(')

if happy_cnt > unhappy_cnt:
    print('happy')
elif happy_cnt == unhappy_cnt:
    print('unsure')
elif unhappy_cnt > happy_cnt:
    print('sad')
elif happy_cnt == 0 and unhappy_cnt == 0:
    print('none')