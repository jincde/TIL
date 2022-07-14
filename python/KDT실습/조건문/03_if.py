# # 중첩 조건문

# dust = int(input())

# if dust > 150:
#     print('미세먼지 매우나쁨')
    
# elif dust > 80:
#     print('미세먼지 나쁨')

# elif dust > 30:
#     print('미세먼지 보통')

# else:
#     if dust < 0:
#         print('음수 값')
#     else:
#         print('미세먼지 좋음')

#         # 중첩 조건문


# # 300이상인 경우 2개 문장 출력
# dust = int(input())

# if dust > 150:
#     if dust > 300:
#         print('실외활동 자제바랍니다.')
#     print('미세먼지 매우나쁨')
    
# elif dust > 80:
#     print('미세먼지 나쁨')

# elif dust > 30:
#     print('미세먼지 보통')

# else:
#     if dust < 0:
#         print('음수 값')
#     else:
#         print('미세먼지 좋음')


# # 300이상인 경우 1개만 출력

# dust = int(input())

# if dust > 150:
#     if dust > 300:
#         print('실외활동 자제바랍니다.')
#     else: 
#         print('미세먼지 매우나쁨')
    
# elif dust > 80:
#     print('미세먼지 나쁨')

# elif dust > 30:
#     print('미세먼지 보통')

# else:
#     if dust < 0:
#         print('음수 값')
#     else:
#         print('미세먼지 좋음')

# #3번째 문항 코드 가독성 향상
dust = int(input())

if dust > 300:
    print('실외활동은 자제바랍니다.')

elif dust > 150:
    print('미세먼지 매우나쁨')
    
elif dust > 80:
    print('미세먼지 나쁨')

elif dust > 30:
    print('미세먼지 보통')

else:
    if dust < 0:
        print('음수 값')
    else:
        print('미세먼지 좋음')