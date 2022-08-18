-- **문자열 합치기**, (성+이름) 출력, 5명만

```sql
SELECT last_name || first_name AS 이름,
age,
country,
phone,
balance
FROM users LIMIT 5;
```

```
이름   age  country  phone          balance
---  ---  -------  -------------  -------
유정호  40   전라북도     016-7280-2855  370    
이경희  36   경상남도     011-9854-5133  5900   
구정자  37   전라남도     011-4177-8170  3100   
장미경  40   충청남도     011-9079-4419  250000 
차영환  30   충청북도     011-2921-4284  220    
```



**-- 문자열 길이 LENGTH**

```sql
SELECT LENGTH(first_name) AS 길이, first_name AS 이름 FROM users LIMIT 1;
```

```
길이  이름
--  --
2   정호
```





-- **문자열 변경 REPLACE** -- 016-7280-2855 => 01672802855

```sql
SELECT first_name, REPLACE(phone, '-', '') AS phone FROM users LIMIT 5;
```

```
first_name  phone      
----------  -----------
정호          01672802855
경희          01198545133
정자          01141778170
미경          01190794419
영환          01129214284
```



-- **숫자 활용** (나머지 값)

```sql
SELECT MOD(5, 2) FROM users LIMIT 1;
```



-- **숫자 활용** (올림, 내림, 반올림)

```sql
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
FROM users
LIMIT 1;
```



-- **9의 제곱근**

```sql
SELECT SQRT(9)
FROM users
LIMIT 1;
```



-- **9^2**

```sql
SELECT POWER(9, 2)
FROM users
LIMIT 1;
```



-- **성(이름) 개수**

```sql
SELECT last_name AS 성, COUNT(*) AS 개수 
FROM users 
GROUP BY last_name LIMIT 5;
```

```
성  개수
-  --
강  23
고  10
곽  4 
구  2 
권  17
```



-- GROUP BY에서 활용하는 **컬럼 제외, 집계함수** 사용

```sql
SELECT last_name, ROUND(AVG(age),2), COUNT(*)
FROM users
GROUP BY last_name LIMIT 5;
```

```
last_name  ROUND(AVG(age),2)  COUNT(*)
---------  -----------------  --------
강          28.61              23      
고          27.2               10      
곽          24.5               4       
구          27.0               2       
권          25.41              17   
```



-- 곽씨의 나이 출력

```sql
SELECT last_name, age
FROM users
WHERE last_name = '곽';
```
```sql
SELECT last_name, age
FROM users
WHERE last_name LIKE '곽%';
```
```
last_name  age
---------  ---
곽          25 
곽          30 
곽          28 
곽          15 
```



-- GROUP BY만으로는 결과 정렬이 되지 않음



-- 100번 이상의 값을 갖고 있는 성만 출력

```sql
SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name HAVING COUNT(last_name) >= 100;
```

```
last_name  COUNT(last_name)
---------  ----------------
김          268             
이          179             
```





