dust = int(input())

if dust >= 151 :
    print('미세먼지 매우나쁨')

elif dust >= 81 and dust <= 150 :
    print('미세먼지 나쁨')

elif dust >= 31 and dust <= 80 :
    print('미세먼지 보통')

else :
    print('미세먼지 좋음')